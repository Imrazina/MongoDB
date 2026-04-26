# Kategorie 1: Propojovani Dat A Vazeb Mezi Datasety

Vsechny dotazy v teto kategorii propojuji minimalne dve kolekce podle `iso3 + year`. Vetsina z nich pouziva `aggregate`, `lookup`, `unwind`, `project`, `group`, `sort` a filtrovani v pipeline.

## Dotaz 1
Najit country-year zaznamy s vysokym `happiness_score`, vysokym `GDP per capita` a soucasne vyssimi emisemi `CO2 per capita`.

**Kolekce:** `happiness_country_year`, `co2_country_year`, `wdi_selected_long`

```javascript
db = db.getSiblingDB("worlddb");

db.happiness_country_year.aggregate([
  // Nejdřív si omezím období jen na roky, které řeším v práci.
  {
    $match: {
      year: { $gte: 2015, $lte: 2019 },
      happiness_score: { $ne: null }
    }
  },
  // K záznamu happiness připojím CO2 data za stejný stát a rok.
  {
    $lookup: {
      from: "co2_country_year",
      let: { iso3: "$iso3", year: "$year" },
      pipeline: [
        {
          $match: {
            $expr: {
              $and: [
                { $eq: ["$iso3", "$$iso3"] },
                { $eq: ["$year", "$$year"] }
              ]
            }
          }
        },
        { $project: { _id: 0, co2_per_capita_t: 1, co2_total_mt: 1 } }
      ],
      as: "co2"
    }
  },
  // Po unwindu mám z páru stát-rok zase jeden plochý záznam.
  { $unwind: "$co2" },
  // Druhý lookup vytáhne jen GDP per capita z WDI dlouhého formátu.
  {
    $lookup: {
      from: "wdi_selected_long",
      let: { iso3: "$iso3", year: "$year" },
      pipeline: [
        {
          $match: {
            $expr: {
              $and: [
                { $eq: ["$iso3", "$$iso3"] },
                { $eq: ["$year", "$$year"] },
                { $eq: ["$indicator", "gdp_per_capita_usd"] }
              ]
            }
          }
        },
        { $project: { _id: 0, value: 1 } }
      ],
      as: "gdp"
    }
  },
  { $unwind: "$gdp" },
  // Tady si nechávám jen sloupce, které chci opravdu ukázat ve výsledku.
  {
    $project: {
      _id: 0,
      iso3: 1,
      country: 1,
      year: 1,
      happiness_score: { $round: ["$happiness_score", 3] },
      gdp_per_capita_usd: { $round: ["$gdp.value", 2] },
      co2_per_capita_t: { $round: ["$co2.co2_per_capita_t", 3] },
      co2_total_mt: { $round: ["$co2.co2_total_mt", 3] }
    }
  },
  // Ve finále mě zajímají jen bohatší ekonomiky s vyšší uhlíkovou stopou.
  {
    $match: {
      gdp_per_capita_usd: { $gte: 20000 },
      co2_per_capita_t: { $gte: 5 }
    }
  },
  // Nahoru chci dostat nejšťastnější země, při shodě rozhodne vyšší GDP.
  { $sort: { happiness_score: -1, gdp_per_capita_usd: -1 } },
  { $limit: 10 }
])
```

**Komentář:** Dotaz propojuje happiness, CO2 a WDI GDP data pres spolecny klic iso3 + year. Na konkretnich datech ukazuje bohatsi a soucasne emisne narocne zeme s vysokym happiness score.

## Dotaz 2
Overit kvalitu propojeni mezi tremi datasety v letech 2015-2017, tedy v obdobi, kde se prekryvaji happiness data s vybranymi WDI indikatory. Dotaz ukazuje nejslabsi vazby, konkretni chybejici WDI indikatory a souhrn pokryti podle roku.

**Kolekce:** `happiness_country_year`, `co2_country_year`, `wdi_selected_long`

```javascript
db = db.getSiblingDB("worlddb");

db.happiness_country_year.aggregate([
  // WDI vybrane indikatory maji v tomto projektu nejsmysluplnejsi prekryv s happiness v letech 2015-2017.
  {
    $match: {
      year: { $gte: 2015, $lte: 2017 },
      happiness_score: { $ne: null }
    }
  },
  // Zjistim, jestli pro dany stat a rok existuje CO2 zaznam.
  {
    $lookup: {
      from: "co2_country_year",
      let: { iso3: "$iso3", year: "$year" },
      pipeline: [
        {
          $match: {
            $expr: {
              $and: [
                { $eq: ["$iso3", "$$iso3"] },
                { $eq: ["$year", "$$year"] }
              ]
            }
          }
        }
      ],
      as: "co2_link"
    }
  },
  // Z WDI nacitam jen tri indikatory, ktere se pak v dalsich dotazech opravdu pouzivaji.
  {
    $lookup: {
      from: "wdi_selected_long",
      let: { iso3: "$iso3", year: "$year" },
      pipeline: [
        {
          $match: {
            $expr: {
              $and: [
                { $eq: ["$iso3", "$$iso3"] },
                { $eq: ["$year", "$$year"] },
                {
                  $in: [
                    "$indicator",
                    [
                      "gdp_per_capita_usd",
                      "life_expectancy_years",
                      "internet_users_pct"
                    ]
                  ]
                }
              ]
            }
          }
        },
        { $project: { _id: 0, indicator: 1 } }
      ],
      as: "wdi_link"
    }
  },
  // Dopocitam, co presne chybi. To je citelnejsi nez jen samotny pocet.
  {
    $addFields: {
      required_wdi_indicators: [
        "gdp_per_capita_usd",
        "life_expectancy_years",
        "internet_users_pct"
      ],
      present_wdi_indicators: "$wdi_link.indicator",
      has_co2: { $gt: [{ $size: "$co2_link" }, 0] }
    }
  },
  {
    $addFields: {
      missing_wdi_indicators: {
        $setDifference: ["$required_wdi_indicators", "$present_wdi_indicators"]
      },
      wdi_indicator_count: { $size: "$present_wdi_indicators" }
    }
  },
  {
    $addFields: {
      linkage_score: {
        $add: [
          { $cond: ["$has_co2", 1, 0] },
          "$wdi_indicator_count"
        ]
      }
    }
  },
  // Facet vraci detail problematickych radku i souhrn kvality propojeni.
  {
    $facet: {
      weakest_links: [
        {
          $match: {
            $or: [
              { has_co2: false },
              { wdi_indicator_count: { $lt: 3 } }
            ]
          }
        },
        {
          $project: {
            _id: 0,
            iso3: 1,
            country: 1,
            year: 1,
            happiness_score: { $round: ["$happiness_score", 3] },
            has_co2: 1,
            wdi_indicator_count: 1,
            missing_wdi_indicators: 1,
            linkage_score: 1
          }
        },
        { $sort: { linkage_score: 1, year: 1, country: 1 } },
        { $limit: 20 }
      ],
      coverage_by_year: [
        {
          $group: {
            _id: "$year",
            total_rows: { $sum: 1 },
            rows_with_co2: { $sum: { $cond: ["$has_co2", 1, 0] } },
            rows_with_all_3_wdi: {
              $sum: { $cond: [{ $eq: ["$wdi_indicator_count", 3] }, 1, 0] }
            },
            fully_linked_rows: {
              $sum: {
                $cond: [
                  { $and: ["$has_co2", { $eq: ["$wdi_indicator_count", 3] }] },
                  1,
                  0
                ]
              }
            }
          }
        },
        {
          $project: {
            _id: 0,
            year: "$_id",
            total_rows: 1,
            rows_with_co2: 1,
            rows_with_all_3_wdi: 1,
            fully_linked_rows: 1,
            full_link_rate_pct: {
              $round: [
                { $multiply: [{ $divide: ["$fully_linked_rows", "$total_rows"] }, 100] },
                2
              ]
            }
          }
        },
        { $sort: { year: 1 } }
      ],
      coverage_summary: [
        {
          $group: {
            _id: null,
            total_rows: { $sum: 1 },
            rows_with_co2: { $sum: { $cond: ["$has_co2", 1, 0] } },
            rows_with_all_3_wdi: {
              $sum: { $cond: [{ $eq: ["$wdi_indicator_count", 3] }, 1, 0] }
            },
            fully_linked_rows: {
              $sum: {
                $cond: [
                  { $and: ["$has_co2", { $eq: ["$wdi_indicator_count", 3] }] },
                  1,
                  0
                ]
              }
            }
          }
        },
        {
          $project: {
            _id: 0,
            total_rows: 1,
            rows_with_co2: 1,
            rows_with_all_3_wdi: 1,
            fully_linked_rows: 1,
            full_link_rate_pct: {
              $round: [
                { $multiply: [{ $divide: ["$fully_linked_rows", "$total_rows"] }, 100] },
                2
              ]
            }
          }
        }
      ]
    }
  }
]).toArray()
```

**Komentář:** Dotaz je kontrola kvality propojeni dat, ale bere jen spolecne obdobi 2015-2017, aby vysledek nebyl zaplneny radky z let, kde WDI prirozene chybi. Na vystupu je videt konkretni problemove vazby, chybejici indikatory a souhrnne pokryti podle roku.

## Dotaz 3
Najit staty, kde mezi dvema po sobe jdoucimi roky rostla `life_expectancy_years`, ale klesal `happiness_score`.

**Kolekce:** `happiness_country_year`, `wdi_selected_long`

```javascript
db = db.getSiblingDB("worlddb");

db.happiness_country_year.aggregate([
  // Nejprve si k happiness dotáhnu life expectancy za stejný stát a rok.
  {
    $lookup: {
      from: "wdi_selected_long",
      let: { iso3: "$iso3", year: "$year" },
      pipeline: [
        {
          $match: {
            $expr: {
              $and: [
                { $eq: ["$iso3", "$$iso3"] },
                { $eq: ["$year", "$$year"] },
                { $eq: ["$indicator", "life_expectancy_years"] }
              ]
            }
          }
        },
        { $project: { _id: 0, value: 1 } }
      ],
      as: "life"
    }
  },
  { $unwind: "$life" },
  // Připravím si čistý mezivýsledek jen s poli, která budu porovnávat mezi roky.
  {
    $project: {
      _id: 0,
      iso3: 1,
      country: 1,
      year: 1,
      happiness_score: 1,
      life_expectancy_years: "$life.value"
    }
  },
  // U každé země si posunu předchozí hodnotu happiness i life expectancy.
  {
    $setWindowFields: {
      partitionBy: "$iso3",
      sortBy: { year: 1 },
      output: {
        prev_happiness: { $shift: { by: -1, output: "$happiness_score" } },
        prev_life: { $shift: { by: -1, output: "$life_expectancy_years" } }
      }
    }
  },
  // Zajímají mě jen případy, kdy životní délka roste, ale štěstí klesá.
  {
    $match: {
      prev_happiness: { $ne: null },
      prev_life: { $ne: null },
      $expr: {
        $and: [
          { $lt: ["$happiness_score", "$prev_happiness"] },
          { $gt: ["$life_expectancy_years", "$prev_life"] }
        ]
      }
    }
  },
  // Výstup nechám čitelný, aby bylo hned vidět srovnání mezi dvěma sousedními roky.
  {
    $project: {
      country: 1,
      iso3: 1,
      year: 1,
      happiness_score: { $round: ["$happiness_score", 3] },
      prev_happiness: { $round: ["$prev_happiness", 3] },
      life_expectancy_years: { $round: ["$life_expectancy_years", 2] },
      prev_life: { $round: ["$prev_life", 2] }
    }
  },
  { $sort: { year: 1, country: 1 } },
  { $limit: 20 }
])
```

**Komentář:** Dotaz porovnava mezirocni zmenu happiness a life expectancy. Na datech hleda situace, kdy se objektivni zdravotni ukazatel zlepsil, ale subjektivni happiness ve stejne zemi klesl.

## Dotaz 4
Najit staty s nejlepsi `wellbeing efficiency`, tedy vysokym `happiness_score` pri nizsich emisich `CO2 per capita`, ale pouze mezi ekonomikami nad danym prahem.

**Kolekce:** `happiness_country_year`, `co2_country_year`, `wdi_selected_long`

```javascript
db = db.getSiblingDB("worlddb");

db.happiness_country_year.aggregate([
  // Pracuju jen s vybraným obdobím.
  { $match: { year: { $gte: 2015, $lte: 2019 } } },
  // Ke každému happiness řádku připojím CO2 per capita.
  {
    $lookup: {
      from: "co2_country_year",
      let: { iso3: "$iso3", year: "$year" },
      pipeline: [
        {
          $match: {
            $expr: {
              $and: [
                { $eq: ["$iso3", "$$iso3"] },
                { $eq: ["$year", "$$year"] }
              ]
            }
          }
        },
        { $project: { _id: 0, co2_per_capita_t: 1 } }
      ],
      as: "co2"
    }
  },
  { $unwind: "$co2" },
  // Z WDI si vytáhnu GDP per capita, abych mohla filtrovat jen srovnatelné ekonomiky.
  {
    $lookup: {
      from: "wdi_selected_long",
      let: { iso3: "$iso3", year: "$year" },
      pipeline: [
        {
          $match: {
            $expr: {
              $and: [
                { $eq: ["$iso3", "$$iso3"] },
                { $eq: ["$year", "$$year"] },
                { $eq: ["$indicator", "gdp_per_capita_usd"] }
              ]
            }
          }
        },
        { $project: { _id: 0, value: 1 } }
      ],
      as: "gdp"
    }
  },
  { $unwind: "$gdp" },
  // Slabé ekonomiky vyřadím a zároveň si hlídám, aby CO2 nebylo nulové kvůli dělení.
  {
    $match: {
      "gdp.value": { $gte: 15000 },
      "co2.co2_per_capita_t": { $gt: 0 }
    }
  },
  // Wellbeing efficiency chápu jako kolik happiness připadá na jednotku CO2 per capita.
  {
    $addFields: {
      wellbeing_efficiency: {
        $divide: ["$happiness_score", "$co2.co2_per_capita_t"]
      }
    }
  },
  // Na konci si jen uklidím výstup do čitelné podoby.
  {
    $project: {
      _id: 0,
      country: 1,
      iso3: 1,
      year: 1,
      happiness_score: { $round: ["$happiness_score", 3] },
      gdp_per_capita_usd: { $round: ["$gdp.value", 2] },
      co2_per_capita_t: { $round: ["$co2.co2_per_capita_t", 3] },
      wellbeing_efficiency: { $round: ["$wellbeing_efficiency", 4] }
    }
  },
  { $sort: { wellbeing_efficiency: -1, happiness_score: -1 } },
  { $limit: 15 }
])
```

**Komentář:** Dotaz pocita pomer happiness score k CO2 per capita a filtruje jen ekonomiky nad zvolenym GDP prahem. Vysledek ukazuje zeme, ktere dosahuji relativne vysokeho wellbeing pri nizsi uhlikove stope.

## Dotaz 5
Rozdelit country-year zaznamy do GDP bucketu a v kazdem bucketu najit zeme, ktere maji vyrazne vyssi `happiness_score` nez jejich ekonomicky srovnatelni vrstevnici.

**Kolekce:** `country_year_master`

```javascript
db = db.getSiblingDB("worlddb");

db.country_year_master.aggregate([
  // Beru jen roky z hlavního období a jen řádky, kde mám všechny tři potřebné hodnoty.
  {
    $match: {
      year: { $gte: 2015, $lte: 2019 },
      gdp_per_capita_usd: { $ne: null },
      happiness_score: { $ne: null },
      co2_per_capita_t: { $ne: null },
      $expr: {
        $and: [
          { $ne: [{ $toString: "$gdp_per_capita_usd" }, "NaN"] },
          { $ne: [{ $toString: "$happiness_score" }, "NaN"] },
          { $ne: [{ $toString: "$co2_per_capita_t" }, "NaN"] }
        ]
      }
    }
  },
  // Bucket rozděluje záznamy do skupin podle ekonomické úrovně.
  {
    $bucket: {
      groupBy: "$gdp_per_capita_usd",
      boundaries: [0, 5000, 10000, 20000, 40000, 80000, 200000],
      default: ">=200000",
      output: {
        peer_avg_happiness: { $avg: "$happiness_score" },
        peer_avg_co2: { $avg: "$co2_per_capita_t" },
        peer_count: { $sum: 1 },
        docs: {
          $push: {
            country: "$country",
            iso3: "$iso3",
            year: "$year",
            gdp_per_capita_usd: "$gdp_per_capita_usd",
            happiness_score: "$happiness_score",
            co2_per_capita_t: "$co2_per_capita_t"
          }
        }
      }
    }
  },
  // Rozbalím si jednotlivé země zpátky vedle průměrů jejich peer-group.
  { $unwind: "$docs" },
  // Dopočítám, o kolik je konkrétní země nad nebo pod průměrem své skupiny.
  {
    $project: {
      _id: 0,
      gdp_bucket: "$_id",
      peer_count: 1,
      country: "$docs.country",
      iso3: "$docs.iso3",
      year: "$docs.year",
      gdp_per_capita_usd: { $round: ["$docs.gdp_per_capita_usd", 2] },
      happiness_score: { $round: ["$docs.happiness_score", 3] },
      co2_per_capita_t: { $round: ["$docs.co2_per_capita_t", 3] },
      peer_avg_happiness: { $round: ["$peer_avg_happiness", 3] },
      peer_avg_co2: { $round: ["$peer_avg_co2", 3] },
      happiness_gap_vs_peers: {
        $round: [
          { $subtract: ["$docs.happiness_score", "$peer_avg_happiness"] },
          3
        ]
      },
      co2_gap_vs_peers: {
        $round: [
          { $subtract: ["$docs.co2_per_capita_t", "$peer_avg_co2"] },
          3
        ]
      }
    }
  },
  { $sort: { happiness_gap_vs_peers: -1, co2_gap_vs_peers: 1 } },
  { $limit: 20 }
]).toArray()
```

**Komentář:** Dotaz rozdeluje zaznamy do GDP skupin a porovnava kazdy country-year zaznam s prumerem jeho ekonomickych vrstevniku. Na datech ukazuje, kdo je v happiness nad prumerem sve GDP skupiny.

## Dotaz 6
Najit staty, ktere mezi prvnim a poslednim pozorovanym rokem soucasne zvysily `happiness_score`, zvysily `GDP per capita` a snizily `CO2 per capita`.

**Kolekce:** `happiness_country_year`, `co2_country_year`, `wdi_selected_long`

```javascript
db = db.getSiblingDB("worlddb");

db.happiness_country_year.aggregate([
  // Nejprve omezím data na společné období a vyřadím prázdné happiness.
  {
    $match: {
      year: { $gte: 2015, $lte: 2019 },
      happiness_score: { $ne: null }
    }
  },
  // Ke každému řádku připojím CO2 za stejný stát a rok.
  {
    $lookup: {
      from: "co2_country_year",
      let: { iso3: "$iso3", year: "$year" },
      pipeline: [
        {
          $match: {
            $expr: {
              $and: [
                { $eq: ["$iso3", "$$iso3"] },
                { $eq: ["$year", "$$year"] }
              ]
            }
          }
        },
        { $project: { _id: 0, co2_per_capita_t: 1 } }
      ],
      as: "co2"
    }
  },
  { $unwind: "$co2" },
  // Z WDI doplním GDP per capita.
  {
    $lookup: {
      from: "wdi_selected_long",
      let: { iso3: "$iso3", year: "$year" },
      pipeline: [
        {
          $match: {
            $expr: {
              $and: [
                { $eq: ["$iso3", "$$iso3"] },
                { $eq: ["$year", "$$year"] },
                { $eq: ["$indicator", "gdp_per_capita_usd"] }
              ]
            }
          }
        },
        { $project: { _id: 0, value: 1 } }
      ],
      as: "gdp"
    }
  },
  { $unwind: "$gdp" },
  // Udělám si jednoduchý pracovní tvar s třemi sledovanými ukazateli.
  {
    $project: {
      iso3: 1,
      country: 1,
      year: 1,
      happiness_score: 1,
      gdp_per_capita_usd: "$gdp.value",
      co2_per_capita_t: "$co2.co2_per_capita_t"
    }
  },
  // Tady rovnou odstřihnu technicky špatné numerické hodnoty.
  {
    $match: {
      $expr: {
        $and: [
          { $ne: [{ $toString: "$happiness_score" }, "NaN"] },
          { $ne: [{ $toString: "$gdp_per_capita_usd" }, "NaN"] },
          { $ne: [{ $toString: "$co2_per_capita_t" }, "NaN"] }
        ]
      }
    }
  },
  // Seřazení je důležité, protože v dalším kroku beru první a poslední dostupný rok.
  { $sort: { iso3: 1, year: 1 } },
  // Na úrovni země si připravím začátek a konec sledovaného období.
  {
    $group: {
      _id: { iso3: "$iso3", country: "$country" },
      years_observed: { $sum: 1 },
      first_year: { $first: "$year" },
      last_year: { $last: "$year" },
      first_happiness: { $first: "$happiness_score" },
      last_happiness: { $last: "$happiness_score" },
      first_gdp: { $first: "$gdp_per_capita_usd" },
      last_gdp: { $last: "$gdp_per_capita_usd" },
      first_co2: { $first: "$co2_per_capita_t" },
      last_co2: { $last: "$co2_per_capita_t" }
    }
  },
  // Chci jen země, kde mám aspoň trochu souvislý časový úsek.
  {
    $match: {
      years_observed: { $gte: 3 },
      $expr: { $gt: ["$last_year", "$first_year"] }
    }
  },
  // Dopočítám změnu happiness, růst GDP a změnu CO2 mezi prvním a posledním rokem.
  {
    $addFields: {
      happiness_delta: { $subtract: ["$last_happiness", "$first_happiness"] },
      gdp_growth_pct: {
        $multiply: [
          {
            $divide: [
              { $subtract: ["$last_gdp", "$first_gdp"] },
              "$first_gdp"
            ]
          },
          100
        ]
      },
      co2_change_pct: {
        $multiply: [
          {
            $divide: [
              { $subtract: ["$last_co2", "$first_co2"] },
              "$first_co2"
            ]
          },
          100
        ]
      }
    }
  },
  // Ve výsledku nechávám jen země se zlepšením ve všech třech směrech.
  {
    $match: {
      happiness_delta: { $gt: 0 },
      gdp_growth_pct: { $gt: 0 },
      co2_change_pct: { $lt: 0 }
    }
  },
  {
    $project: {
      _id: 0,
      iso3: "$_id.iso3",
      country: "$_id.country",
      first_year: 1,
      last_year: 1,
      years_observed: 1,
      happiness_delta: { $round: ["$happiness_delta", 3] },
      gdp_growth_pct: { $round: ["$gdp_growth_pct", 2] },
      co2_change_pct: { $round: ["$co2_change_pct", 2] }
    }
  },
  // Nahoře chci země s největším růstem happiness a zároveň co největším poklesem CO2.
  { $sort: { happiness_delta: -1, co2_change_pct: 1, gdp_growth_pct: -1 } },
  { $limit: 20 }
]).toArray()
```

**Komentář:** Dotaz sleduje zmenu mezi prvnim a poslednim dostupnym rokem. Vysledek ukazuje zeme, kde se soucasne zlepsilo happiness i GDP a zaroven klesly emise CO2 na osobu.

---

# Kategorie 2: Agregacni A Analyticke Dotazy

Tato kategorie je postavena hlavne nad kolekci `country_year_master`, protoze ta spojuje `happiness`, `CO2` a vybrane `WDI` indikatory na urovni `stat-rok`. Dotazy zde pouzivaji hlavne `aggregate`, `setWindowFields`, `bucket`, vicefazove `project`, `group` a odvozene analyticke metriky.

## Dotaz 1
Najit country-year zaznamy s nejsilnejsim kratkodobym momentum, tedy kombinaci vysokeho aktualniho `happiness_score`, rustu proti predchozimu roku a vysokeho trileteho rolling average.

**Kolekce:** `country_year_master`

```javascript
db = db.getSiblingDB("worlddb");

db.country_year_master.aggregate([
  // Nejdřív si nechám jen období, kde chci momentum sledovat.
  {
    $match: {
      year: { $gte: 2015, $lte: 2019 },
      happiness_score: { $ne: null },
      gdp_per_capita_usd: { $ne: null },
      co2_per_capita_t: { $ne: null },
      $expr: {
        $and: [
          { $ne: [{ $toString: "$happiness_score" }, "NaN"] },
          { $ne: [{ $toString: "$gdp_per_capita_usd" }, "NaN"] },
          { $ne: [{ $toString: "$co2_per_capita_t" }, "NaN"] }
        ]
      }
    }
  },
  // Pro každou zemi počítám klouzavý průměr happiness a GDP a zároveň tahám předchozí happiness.
  {
    $setWindowFields: {
      partitionBy: "$iso3",
      sortBy: { year: 1 },
      output: {
        rolling_happiness_3y: {
          $avg: "$happiness_score",
          window: { documents: [-2, 0] }
        },
        rolling_gdp_3y: {
          $avg: "$gdp_per_capita_usd",
          window: { documents: [-2, 0] }
        },
        prev_happiness: {
          $shift: { by: -1, output: "$happiness_score" }
        }
      }
    }
  },
  // Bez předchozího roku nebo bez rolling průměru by momentum nedávalo smysl.
  {
    $match: {
      prev_happiness: { $ne: null },
      rolling_happiness_3y: { $ne: null },
      rolling_gdp_3y: { $ne: null }
    }
  },
  // Momentum score kombinuje aktuální skok happiness s delším kontextem happiness a GDP.
  {
    $addFields: {
      happiness_delta: { $subtract: ["$happiness_score", "$prev_happiness"] },
      momentum_score: {
        $add: [
          { $multiply: [{ $subtract: ["$happiness_score", "$prev_happiness"] }, 100] },
          { $multiply: ["$rolling_happiness_3y", 10] },
          { $divide: ["$rolling_gdp_3y", 10000] }
        ]
      }
    }
  },
  // Výstup nechávám čitelný, aby bylo hned vidět, z čeho se skóre skládá.
  {
    $project: {
      _id: 0,
      iso3: 1,
      country: 1,
      year: 1,
      happiness_score: { $round: ["$happiness_score", 3] },
      prev_happiness: { $round: ["$prev_happiness", 3] },
      happiness_delta: { $round: ["$happiness_delta", 3] },
      rolling_happiness_3y: { $round: ["$rolling_happiness_3y", 3] },
      rolling_gdp_3y: { $round: ["$rolling_gdp_3y", 2] },
      momentum_score: { $round: ["$momentum_score", 3] }
    }
  },
  // Nahoru jdou země s nejsilnějším krátkodobým impulsem.
  { $sort: { momentum_score: -1, happiness_score: -1 } },
  { $limit: 15 }
]).toArray()
```

**Komentář:** Dotaz pocita kratkodobe momentum pomoci predchoziho roku a trileteho rolling average. Na datech zvysuje vahu zemi, kde neni vysoke jen aktualni skore, ale i jeho nedavny rust.

## Dotaz 2
Najit staty s nejstabilnejsi kombinaci vysokeho `happiness_score` a nizke volatility v letech 2015-2019.

**Kolekce:** `country_year_master`

```javascript
db = db.getSiblingDB("worlddb");

db.country_year_master.aggregate([
  // Vstup tvoří jen záznamy s platným happiness a CO2 v hlavním období.
  {
    $match: {
      year: { $gte: 2015, $lte: 2019 },
      happiness_score: { $ne: null },
      co2_per_capita_t: { $ne: null },
      $expr: {
        $and: [
          { $ne: [{ $toString: "$happiness_score" }, "NaN"] },
          { $ne: [{ $toString: "$co2_per_capita_t" }, "NaN"] }
        ]
      }
    }
  },
  // Na úrovni země si spočítám základní statistiky pro happiness.
  {
    $group: {
      _id: { iso3: "$iso3", country: "$country" },
      years_observed: { $sum: 1 },
      avg_happiness: { $avg: "$happiness_score" },
      std_happiness: { $stdDevSamp: "$happiness_score" },
      min_happiness: { $min: "$happiness_score" },
      max_happiness: { $max: "$happiness_score" },
      avg_co2: { $avg: "$co2_per_capita_t" }
    }
  },
  // Potřebuju aspoň čtyři pozorování, aby stabilita nebyla postavená na náhodě.
  {
    $match: {
      years_observed: { $gte: 4 },
      std_happiness: { $ne: null }
    }
  },
  // Přidám si rozsah, koeficient variability a jednoduchý stability index.
  {
    $addFields: {
      happiness_range: { $subtract: ["$max_happiness", "$min_happiness"] },
      coeff_variation: {
        $cond: [
          { $gt: ["$avg_happiness", 0] },
          { $divide: ["$std_happiness", "$avg_happiness"] },
          null
        ]
      },
      stability_index: {
        $cond: [
          { $gt: ["$std_happiness", 0] },
          { $divide: ["$avg_happiness", "$std_happiness"] },
          999
        ]
      }
    }
  },
  // Ve výsledku chci mít po ruce jak samotnou stabilitu, tak i základní kontext.
  {
    $project: {
      _id: 0,
      iso3: "$_id.iso3",
      country: "$_id.country",
      years_observed: 1,
      avg_happiness: { $round: ["$avg_happiness", 3] },
      std_happiness: { $round: ["$std_happiness", 3] },
      happiness_range: { $round: ["$happiness_range", 3] },
      coeff_variation: { $round: ["$coeff_variation", 4] },
      avg_co2: { $round: ["$avg_co2", 3] },
      stability_index: { $round: ["$stability_index", 3] }
    }
  },
  // Nahoře skončí země s nejvyšší stabilitou happiness.
  { $sort: { stability_index: -1, avg_happiness: -1 } },
  { $limit: 15 }
]).toArray()
```

**Komentář:** Dotaz meri stabilitu happiness v case pomoci smerodatne odchylky, rozsahu a stability indexu. Na datech ukazuje zeme, kde je vysoke nebo stabilni happiness dlouhodobe, ne jen v jednom roce.

## Dotaz 3
Najit staty, kde silne rostl `GDP per capita`, ale `happiness_score` stagnoval nebo klesal.

**Kolekce:** `happiness_country_year`, `wdi_selected_long`

```javascript
db = db.getSiblingDB("worlddb");

db.happiness_country_year.aggregate([
  // Porovnávám jen dva pevné body v čase, aby bylo srovnání mezi státy jednotné.
  {
    $match: {
      year: { $in: [2015, 2017] },
      happiness_score: { $ne: null },
      $expr: { $ne: [{ $toString: "$happiness_score" }, "NaN"] }
    }
  },
  // GDP tahám z WDI dlouhého formátu vždy pro stejnou zemi a rok.
  {
    $lookup: {
      from: "wdi_selected_long",
      let: { iso3: "$iso3", year: "$year" },
      pipeline: [
        {
          $match: {
            $expr: {
              $and: [
                { $eq: ["$iso3", "$$iso3"] },
                { $eq: ["$year", "$$year"] },
                { $eq: ["$indicator", "gdp_per_capita_usd"] },
                { $ne: [{ $toString: "$value" }, "NaN"] }
              ]
            }
          }
        },
        { $project: { _id: 0, value: 1 } }
      ],
      as: "gdp"
    }
  },
  { $unwind: "$gdp" },
  // Přeložím oba roky do jedné řádky za stát, abych mohla porovnat změnu.
  {
    $group: {
      _id: { iso3: "$iso3", country: "$country" },
      y2015_happiness: {
        $max: {
          $cond: [{ $eq: ["$year", 2015] }, "$happiness_score", null]
        }
      },
      y2017_happiness: {
        $max: {
          $cond: [{ $eq: ["$year", 2017] }, "$happiness_score", null]
        }
      },
      y2015_gdp: {
        $max: {
          $cond: [{ $eq: ["$year", 2015] }, "$gdp.value", null]
        }
      },
      y2017_gdp: {
        $max: {
          $cond: [{ $eq: ["$year", 2017] }, "$gdp.value", null]
        }
      }
    }
  },
  // Zůstávají jen země, kde opravdu existují obě srovnávané časové značky.
  {
    $match: {
      y2015_happiness: { $ne: null },
      y2017_happiness: { $ne: null },
      y2015_gdp: { $ne: null },
      y2017_gdp: { $ne: null }
    }
  },
  // Dopočítám změnu happiness i růst GDP mezi roky 2015 a 2017.
  {
    $addFields: {
      happiness_delta: { $subtract: ["$y2017_happiness", "$y2015_happiness"] },
      gdp_growth_pct: {
        $multiply: [
          {
            $divide: [
              { $subtract: ["$y2017_gdp", "$y2015_gdp"] },
              "$y2015_gdp"
            ]
          },
          100
        ]
      },
      divergence_score: {
        $subtract: [
          {
            $multiply: [
              {
                $divide: [
                  { $subtract: ["$y2017_gdp", "$y2015_gdp"] },
                  "$y2015_gdp"
                ]
              },
              100
            ]
          },
          {
            $multiply: [
              { $subtract: ["$y2017_happiness", "$y2015_happiness"] },
              100
            ]
          }
        ]
      }
    }
  },
  // Divergence score zvýrazní případy, kde ekonomika rostla bez stejné reakce happiness.
  {
    $project: {
      _id: 0,
      iso3: "$_id.iso3",
      country: "$_id.country",
      y2015_happiness: { $round: ["$y2015_happiness", 3] },
      y2017_happiness: { $round: ["$y2017_happiness", 3] },
      happiness_delta: { $round: ["$happiness_delta", 3] },
      y2015_gdp: { $round: ["$y2015_gdp", 2] },
      y2017_gdp: { $round: ["$y2017_gdp", 2] },
      gdp_growth_pct: { $round: ["$gdp_growth_pct", 2] },
      divergence_score: { $round: ["$divergence_score", 2] }
    }
  },
  // Nahoru jdou státy s největším rozdílem mezi ekonomickým růstem a změnou happiness.
  { $sort: { divergence_score: -1, gdp_growth_pct: -1 } },
  { $limit: 15 }
]).toArray()
```

**Komentář:** Dotaz porovnava GDP a happiness mezi roky 2015 a 2017. Vysledek ukazuje zeme, kde ekonomicky ukazatel rostl, ale happiness nerostlo stejnym tempem nebo klesalo.

## Dotaz 4
Najit staty s nejlepsim `green growth score`, tedy rustem `GDP`, rustem `happiness` a poklesem `CO2 per capita`.

**Kolekce:** `country_year_master`

```javascript
db = db.getSiblingDB("worlddb");

db.country_year_master.aggregate([
  // Vstup tvoří jen řádky se všemi třemi validními indikátory.
  {
    $match: {
      year: { $gte: 2015, $lte: 2019 },
      happiness_score: { $ne: null },
      gdp_per_capita_usd: { $ne: null },
      co2_per_capita_t: { $ne: null },
      $expr: {
        $and: [
          { $ne: [{ $toString: "$happiness_score" }, "NaN"] },
          { $ne: [{ $toString: "$gdp_per_capita_usd" }, "NaN"] },
          { $ne: [{ $toString: "$co2_per_capita_t" }, "NaN"] }
        ]
      }
    }
  },
  // Přes window si pro každou zemi připravím začátek a konec sledovaného období.
  {
    $setWindowFields: {
      partitionBy: "$iso3",
      sortBy: { year: 1 },
      output: {
        first_year: {
          $first: "$year",
          window: { documents: ["unbounded", "unbounded"] }
        },
        last_year: {
          $last: "$year",
          window: { documents: ["unbounded", "unbounded"] }
        },
        first_gdp: {
          $first: "$gdp_per_capita_usd",
          window: { documents: ["unbounded", "unbounded"] }
        },
        last_gdp: {
          $last: "$gdp_per_capita_usd",
          window: { documents: ["unbounded", "unbounded"] }
        },
        first_happiness: {
          $first: "$happiness_score",
          window: { documents: ["unbounded", "unbounded"] }
        },
        last_happiness: {
          $last: "$happiness_score",
          window: { documents: ["unbounded", "unbounded"] }
        },
        first_co2: {
          $first: "$co2_per_capita_t",
          window: { documents: ["unbounded", "unbounded"] }
        },
        last_co2: {
          $last: "$co2_per_capita_t",
          window: { documents: ["unbounded", "unbounded"] }
        }
      }
    }
  },
  // Na úrovni země z toho poskládám jeden souhrnný řádek.
  {
    $group: {
      _id: { iso3: "$iso3", country: "$country" },
      years_observed: { $sum: 1 },
      first_year: { $max: "$first_year" },
      last_year: { $max: "$last_year" },
      first_gdp: { $max: "$first_gdp" },
      last_gdp: { $max: "$last_gdp" },
      first_happiness: { $max: "$first_happiness" },
      last_happiness: { $max: "$last_happiness" },
      first_co2: { $max: "$first_co2" },
      last_co2: { $max: "$last_co2" }
    }
  },
  // Chci jen země, kde dává přepočet změn smysl a nic se nedělí nulou.
  {
    $match: {
      years_observed: { $gte: 3 },
      first_gdp: { $ne: null },
      last_gdp: { $ne: null },
      first_happiness: { $ne: null },
      last_happiness: { $ne: null },
      first_co2: { $ne: null },
      last_co2: { $ne: null },
      $expr: {
        $and: [
          { $gt: ["$first_gdp", 0] },
          { $gt: ["$first_co2", 0] },
          { $gt: ["$last_year", "$first_year"] },
          { $ne: [{ $toString: "$first_gdp" }, "NaN"] },
          { $ne: [{ $toString: "$last_gdp" }, "NaN"] },
          { $ne: [{ $toString: "$first_happiness" }, "NaN"] },
          { $ne: [{ $toString: "$last_happiness" }, "NaN"] },
          { $ne: [{ $toString: "$first_co2" }, "NaN"] },
          { $ne: [{ $toString: "$last_co2" }, "NaN"] }
        ]
      }
    }
  },
  // Tady už přepočítávám ekonomickou, sociální i ekologickou změnu.
  {
    $addFields: {
      gdp_growth_pct: {
        $multiply: [
          {
            $divide: [
              { $subtract: ["$last_gdp", "$first_gdp"] },
              "$first_gdp"
            ]
          },
          100
        ]
      },
      happiness_delta: { $subtract: ["$last_happiness", "$first_happiness"] },
      co2_change_pct: {
        $multiply: [
          {
            $divide: [
              { $subtract: ["$last_co2", "$first_co2"] },
              "$first_co2"
            ]
          },
          100
        ]
      }
    }
  },
  // Green growth score skládá všechny tři směry do jednoho čísla.
  {
    $addFields: {
      green_growth_score: {
        $add: [
          "$gdp_growth_pct",
          { $multiply: ["$happiness_delta", 20] },
          { $multiply: ["$co2_change_pct", -1] }
        ]
      }
    }
  },
  // Zůstávají jen státy, které splnily pozitivní vývoj ve všech třech dimenzích.
  {
    $match: {
      gdp_growth_pct: { $gt: 0 },
      happiness_delta: { $gt: 0 },
      co2_change_pct: { $lt: 0 }
    }
  },
  {
    $project: {
      _id: 0,
      iso3: "$_id.iso3",
      country: "$_id.country",
      first_year: 1,
      last_year: 1,
      years_observed: 1,
      gdp_growth_pct: { $round: ["$gdp_growth_pct", 2] },
      happiness_delta: { $round: ["$happiness_delta", 3] },
      co2_change_pct: { $round: ["$co2_change_pct", 2] },
      green_growth_score: { $round: ["$green_growth_score", 2] }
    }
  },
  // Nahoře chci země s nejlepším celkovým souběhem všech tří změn.
  { $sort: { green_growth_score: -1 } },
  { $limit: 15 }
]).toArray()
```

**Komentář:** Dotaz sklada ekonomickou, socialni a ekologickou zmenu do jednoho green growth score. Na datech hleda zeme, kde se soucasne zvedlo GDP, zlepsilo happiness a snizily emise na osobu.

## Dotaz 5
Rozdelit country-year zaznamy do GDP bucketu a v kazdem bucketu porovnat prumerny `happiness`, `CO2`, velikost vzorku a odchylku jednotlivych zaznamu od vrstevniku.

**Kolekce:** `country_year_master`

```javascript
db = db.getSiblingDB("worlddb");

db.country_year_master.aggregate([
  // Vstup připravím jen z řádků, kde dávají všechny tři veličiny smysl.
  {
    $match: {
      year: { $gte: 2015, $lte: 2019 },
      gdp_per_capita_usd: { $ne: null },
      happiness_score: { $ne: null },
      co2_per_capita_t: { $ne: null },
      $expr: {
        $and: [
          { $ne: [{ $toString: "$gdp_per_capita_usd" }, "NaN"] },
          { $ne: [{ $toString: "$happiness_score" }, "NaN"] },
          { $ne: [{ $toString: "$co2_per_capita_t" }, "NaN"] }
        ]
      }
    }
  },
  // Bucket rozděluje země podle ekonomické úrovně, aby srovnání bylo férovější.
  {
    $bucket: {
      groupBy: "$gdp_per_capita_usd",
      boundaries: [0, 5000, 10000, 20000, 40000, 80000, 200000],
      default: ">=200000",
      output: {
        peer_avg_happiness: { $avg: "$happiness_score" },
        peer_avg_co2: { $avg: "$co2_per_capita_t" },
        peer_count: { $sum: 1 },
        docs: {
          $push: {
            country: "$country",
            iso3: "$iso3",
            year: "$year",
            gdp_per_capita_usd: "$gdp_per_capita_usd",
            happiness_score: "$happiness_score",
            co2_per_capita_t: "$co2_per_capita_t"
          }
        }
      }
    }
  },
  // Po rozbalení mám u každé země i průměr její peer-group.
  { $unwind: "$docs" },
  // Vypočtu, o kolik je konkrétní řádek nad nebo pod vrstevníky.
  {
    $project: {
      _id: 0,
      gdp_bucket: "$_id",
      peer_count: 1,
      country: "$docs.country",
      iso3: "$docs.iso3",
      year: "$docs.year",
      gdp_per_capita_usd: { $round: ["$docs.gdp_per_capita_usd", 2] },
      happiness_score: { $round: ["$docs.happiness_score", 3] },
      co2_per_capita_t: { $round: ["$docs.co2_per_capita_t", 3] },
      peer_avg_happiness: { $round: ["$peer_avg_happiness", 3] },
      peer_avg_co2: { $round: ["$peer_avg_co2", 3] },
      happiness_gap_vs_peers: {
        $round: [
          { $subtract: ["$docs.happiness_score", "$peer_avg_happiness"] },
          3
        ]
      },
      co2_gap_vs_peers: {
        $round: [
          { $subtract: ["$docs.co2_per_capita_t", "$peer_avg_co2"] },
          3
        ]
      }
    }
  },
  // Nahoře chci pozitivní odchylku v happiness a při stejné hodnotě nižší CO2 mezeru.
  { $sort: { happiness_gap_vs_peers: -1, co2_gap_vs_peers: 1 } },
  { $limit: 20 }
]).toArray()
```

**Komentář:** Dotaz vytvari GDP bucket skupiny a u kazdeho zaznamu pocita odchylku od prumeru vrstevniku. Vysledek je vhodny pro porovnani zemi s podobnou ekonomickou urovni.

## Dotaz 6
V ramci kazdeho roku porovnat poradi statu podle `happiness_score` a podle nizkych emisi `CO2 per capita` a najit nejvetsi rozdily poradi.

**Kolekce:** `country_year_master`

```javascript
db = db.getSiblingDB("worlddb");

db.country_year_master.aggregate([
  // Pracuju s roky, kde mám současně happiness i CO2.
  {
    $match: {
      year: { $gte: 2015, $lte: 2019 },
      happiness_score: { $ne: null },
      co2_per_capita_t: { $ne: null },
      $expr: {
        $and: [
          { $ne: [{ $toString: "$happiness_score" }, "NaN"] },
          { $ne: [{ $toString: "$co2_per_capita_t" }, "NaN"] }
        ]
      }
    }
  },
  // Nejprve udělám pořadí zemí podle happiness uvnitř každého roku.
  {
    $setWindowFields: {
      partitionBy: "$year",
      sortBy: { happiness_score: -1 },
      output: {
        happiness_rank: { $rank: {} }
      }
    }
  },
  // Ve druhém kroku udělám v tom samém roce pořadí podle nízkých emisí.
  {
    $setWindowFields: {
      partitionBy: "$year",
      sortBy: { co2_per_capita_t: 1 },
      output: {
        low_co2_rank: { $rank: {} }
      }
    }
  },
  // Rozdíl pořadí mi ukáže, kde si země vedou podobně nebo naopak úplně jinak.
  {
    $addFields: {
      rank_gap: { $subtract: ["$low_co2_rank", "$happiness_rank"] },
      abs_rank_gap: {
        $abs: { $subtract: ["$low_co2_rank", "$happiness_rank"] }
      }
    }
  },
  // Ve výstupu nechávám obě pořadí vedle sebe, aby byl rozpor okamžitě vidět.
  {
    $project: {
      _id: 0,
      year: 1,
      country: 1,
      iso3: 1,
      happiness_score: { $round: ["$happiness_score", 3] },
      co2_per_capita_t: { $round: ["$co2_per_capita_t", 3] },
      happiness_rank: 1,
      low_co2_rank: 1,
      rank_gap: 1,
      abs_rank_gap: 1
    }
  },
  // Nahoře jsou státy s největším rozporem mezi oběma žebříčky.
  { $sort: { abs_rank_gap: -1, year: 1 } },
  { $limit: 20 }
]).toArray()
```

**Komentář:** Dotaz porovnava dve poradi uvnitr kazdeho roku: podle happiness a podle nizkych emisi CO2. Vysledek ukazuje nejvetsi rozpory mezi socialnim a emisnim zebrickem.

---

# Kategorie 3: Kvalita Dat A Validace

Tato kategorie kontroluje, jestli jsou nahrana data pouzitelna pro analyticke dotazy. Dotazy jsou psane tak, aby vracely souhrn a ukazky, ne jen prazdne pole pri uspechu kontroly.

## Dotaz 1
Ziskat prehled uplnosti hlavni master kolekce vcetne procent chybejicich hodnot a poctu plne pouzitelnych radku.

**Kolekce:** `country_year_master`

```javascript
db = db.getSiblingDB("worlddb");

db.country_year_master.aggregate([
  // Nejdriv si u kazdeho radku oznacim, jestli ma vsechny hlavni hodnoty.
  {
    $addFields: {
      has_all_core_values: {
        $and: [
          { $ne: ["$happiness_score", null] },
          { $ne: ["$gdp_per_capita_usd", null] },
          { $ne: ["$co2_per_capita_t", null] },
          { $ne: ["$life_expectancy_years", null] }
        ]
      }
    }
  },
  {
    $group: {
      _id: null,
      total_rows: { $sum: 1 },
      first_year: { $min: "$year" },
      last_year: { $max: "$year" },
      countries: { $addToSet: "$iso3" },
      complete_core_rows: { $sum: { $cond: ["$has_all_core_values", 1, 0] } },
      missing_happiness: { $sum: { $cond: [{ $eq: ["$happiness_score", null] }, 1, 0] } },
      missing_gdp: { $sum: { $cond: [{ $eq: ["$gdp_per_capita_usd", null] }, 1, 0] } },
      missing_co2: { $sum: { $cond: [{ $eq: ["$co2_per_capita_t", null] }, 1, 0] } },
      missing_life_expectancy: { $sum: { $cond: [{ $eq: ["$life_expectancy_years", null] }, 1, 0] } }
    }
  },
  {
    $project: {
      _id: 0,
      total_rows: 1,
      country_count: { $size: "$countries" },
      first_year: 1,
      last_year: 1,
      complete_core_rows: 1,
      complete_core_rate_pct: {
        $round: [{ $multiply: [{ $divide: ["$complete_core_rows", "$total_rows"] }, 100] }, 2]
      },
      missing_happiness: 1,
      missing_gdp: 1,
      missing_gdp_pct: {
        $round: [{ $multiply: [{ $divide: ["$missing_gdp", "$total_rows"] }, 100] }, 2]
      },
      missing_co2: 1,
      missing_co2_pct: {
        $round: [{ $multiply: [{ $divide: ["$missing_co2", "$total_rows"] }, 100] }, 2]
      },
      missing_life_expectancy: 1,
      missing_life_expectancy_pct: {
        $round: [{ $multiply: [{ $divide: ["$missing_life_expectancy", "$total_rows"] }, 100] }, 2]
      }
    }
  }
]).toArray()
```

**Komentář:** Dotaz vrací jeden souhrnný dokument s počty i procenty. Na datech je hned vidět, že happiness je kompletní, ale některé WDI ukazatele nejsou dostupné pro všechny roky a země.

## Dotaz 2
Ukazat pokryti WDI indikatoru na urovni country-year: kolik indikatoru ma kazda zeme v danem roce, jak vypada rozdeleni podle poctu dostupnych indikatoru a ktere zaznamy jsou nejslabsi nebo nejsilnejsi.

**Kolekce:** `wdi_selected_long`

```javascript
db = db.getSiblingDB("worlddb");

db.wdi_selected_long.aggregate([
  // Nejdřív z dlouhého WDI formátu udělám jeden řádek pro každou kombinaci země a roku.
  {
    $group: {
      _id: { iso3: "$iso3", country: "$country", year: "$year" },
      available_indicators: { $addToSet: "$indicator" },
      non_missing_values: {
        $sum: {
          $cond: [
            {
              $and: [
                { $ne: ["$value", null] },
                { $ne: [{ $toString: "$value" }, "NaN"] }
              ]
            },
            1,
            0
          ]
        }
      }
    }
  },
  // Počet indikátorů říká, jak dobře je konkrétní country-year pokrytý ve WDI.
  {
    $addFields: {
      indicator_count: { $size: "$available_indicators" }
    }
  },
  // Facet vrací tři pohledy: distribuci, nejslabší záznamy a nejsilnější záznamy.
  {
    $facet: {
      coverage_distribution: [
        {
          $group: {
            _id: "$indicator_count",
            country_year_count: { $sum: 1 },
            first_year: { $min: "$_id.year" },
            last_year: { $max: "$_id.year" }
          }
        },
        {
          $project: {
            _id: 0,
            indicator_count: "$_id",
            country_year_count: 1,
            first_year: 1,
            last_year: 1
          }
        },
        { $sort: { indicator_count: 1 } }
      ],
      weakest_country_years: [
        {
          $project: {
            _id: 0,
            iso3: "$_id.iso3",
            country: "$_id.country",
            year: "$_id.year",
            indicator_count: 1,
            non_missing_values: 1,
            available_indicators: { $sortArray: { input: "$available_indicators", sortBy: 1 } }
          }
        },
        { $sort: { indicator_count: 1, non_missing_values: 1, year: 1, country: 1 } },
        { $limit: 12 }
      ],
      strongest_country_years: [
        {
          $project: {
            _id: 0,
            iso3: "$_id.iso3",
            country: "$_id.country",
            year: "$_id.year",
            indicator_count: 1,
            non_missing_values: 1,
            available_indicators: { $sortArray: { input: "$available_indicators", sortBy: 1 } }
          }
        },
        { $sort: { indicator_count: -1, non_missing_values: -1, year: -1, country: 1 } },
        { $limit: 12 }
      ]
    }
  }
]).toArray()
```

**Komentář:** Dotaz ukazuje kvalitu WDI dat na úrovni země a roku. Neřeší jen to, zda existují duplicity, ale přímo ukazuje, jak bohatě jsou country-year záznamy pokryté indikátory a kde je datové pokrytí nejslabší.

## Dotaz 3
Ukazat pokryti WDI indikatoru: pocet radku, pocet neprázdných hodnot, pocet zemi a casovy rozsah pro kazdy indikator.

**Kolekce:** `wdi_selected_long`

```javascript
db = db.getSiblingDB("worlddb");

db.wdi_selected_long.aggregate([
  // U kazde hodnoty si oznacim, jestli je realne pouzitelna.
  {
    $addFields: {
      has_value: {
        $and: [
          { $ne: ["$value", null] },
          { $ne: [{ $toString: "$value" }, "NaN"] }
        ]
      }
    }
  },
  {
    $group: {
      _id: "$indicator",
      total_rows: { $sum: 1 },
      non_missing_rows: { $sum: { $cond: ["$has_value", 1, 0] } },
      countries_with_value: { $addToSet: { $cond: ["$has_value", "$iso3", "$$REMOVE"] } },
      first_year: { $min: "$year" },
      last_year: { $max: "$year" },
      min_value: { $min: "$value" },
      max_value: { $max: "$value" }
    }
  },
  {
    $project: {
      _id: 0,
      indicator: "$_id",
      total_rows: 1,
      non_missing_rows: 1,
      missing_rows: { $subtract: ["$total_rows", "$non_missing_rows"] },
      non_missing_rate_pct: {
        $round: [{ $multiply: [{ $divide: ["$non_missing_rows", "$total_rows"] }, 100] }, 2]
      },
      countries_with_value: { $size: "$countries_with_value" },
      first_year: 1,
      last_year: 1,
      min_value: { $round: ["$min_value", 2] },
      max_value: { $round: ["$max_value", 2] }
    }
  },
  { $sort: { non_missing_rows: -1, indicator: 1 } }
]).toArray()
```

**Komentář:** Dotaz místo hledání jen chyb ukazuje reálné pokrytí každého WDI indikátoru. Výstup je užitečný pro obhajobu, protože vysvětluje, proč některé analýzy pracují s omezeným obdobím.

## Dotaz 4
Najit zeme, ktere v master kolekci nemaji plne pokryti pro roky 2015-2019.

**Kolekce:** `country_year_master`

```javascript
db = db.getSiblingDB("worlddb");

db.country_year_master.aggregate([
  // Kontroluju jen hlavni obdobi, se kterym pracuji dotazy nad happiness.
  {
    $match: {
      year: { $gte: 2015, $lte: 2019 }
    }
  },
  // U kazde zeme si ulozim roky, ktere jsou skutecne dostupne.
  {
    $group: {
      _id: { iso3: "$iso3", country: "$country" },
      years_present: { $addToSet: "$year" },
      row_count: { $sum: 1 }
    }
  },
  {
    $addFields: {
      expected_years: [2015, 2016, 2017, 2018, 2019],
      years_observed: { $size: "$years_present" }
    }
  },
  // setDifference ukaze konkretni roky, ktere zemi chybi.
  {
    $addFields: {
      missing_years: { $setDifference: ["$expected_years", "$years_present"] }
    }
  },
  {
    $match: {
      missing_years: { $ne: [] }
    }
  },
  {
    $project: {
      _id: 0,
      iso3: "$_id.iso3",
      country: "$_id.country",
      years_observed: 1,
      years_present: { $sortArray: { input: "$years_present", sortBy: 1 } },
      missing_years: 1
    }
  },
  { $sort: { years_observed: 1, country: 1 } },
  { $limit: 25 }
]).toArray()
```

**Komentář:** Dotaz ukazuje konkrétní země s neúplnou časovou řadou. To se hodí při vysvětlování, proč trendové dotazy vyžadují minimální počet pozorování.

## Dotaz 5
Overit rozumne rozsahy hlavních numerickych hodnot a vratit pocty problemu vcetne ukazek.

**Kolekce:** `country_year_master`

```javascript
db = db.getSiblingDB("worlddb");

db.country_year_master.aggregate([
  // Facet uklada ukazky problematickych hodnot pro kazde validacni pravidlo.
  {
    $facet: {
      invalid_happiness: [
        { $match: { $or: [{ happiness_score: { $lt: 0 } }, { happiness_score: { $gt: 10 } }] } },
        { $project: { _id: 0, country: 1, iso3: 1, year: 1, happiness_score: 1 } },
        { $limit: 5 }
      ],
      invalid_internet: [
        { $match: { $or: [{ internet_users_pct: { $lt: 0 } }, { internet_users_pct: { $gt: 100 } }] } },
        { $project: { _id: 0, country: 1, iso3: 1, year: 1, internet_users_pct: 1 } },
        { $limit: 5 }
      ],
      invalid_life_expectancy: [
        { $match: { $or: [{ life_expectancy_years: { $lt: 20 } }, { life_expectancy_years: { $gt: 100 } }] } },
        { $project: { _id: 0, country: 1, iso3: 1, year: 1, life_expectancy_years: 1 } },
        { $limit: 5 }
      ],
      invalid_co2: [
        { $match: { co2_per_capita_t: { $lt: 0 } } },
        { $project: { _id: 0, country: 1, iso3: 1, year: 1, co2_per_capita_t: 1 } },
        { $limit: 5 }
      ]
    }
  },
  // Vysledek shrnu do jednoho dokumentu, aby ani bez nalezenych chyb nebyl vystup prazdny.
  {
    $project: {
      _id: 0,
      validation_status: {
        $cond: [
          {
            $eq: [
              {
                $add: [
                  { $size: "$invalid_happiness" },
                  { $size: "$invalid_internet" },
                  { $size: "$invalid_life_expectancy" },
                  { $size: "$invalid_co2" }
                ]
              },
              0
            ]
          },
          "OK - no out-of-range examples found",
          "CHECK REQUIRED"
        ]
      },
      invalid_happiness_count: { $size: "$invalid_happiness" },
      invalid_happiness_examples: {
        $cond: [{ $eq: [{ $size: "$invalid_happiness" }, 0] }, "no invalid happiness examples", "$invalid_happiness"]
      },
      invalid_internet_count: { $size: "$invalid_internet" },
      invalid_internet_examples: {
        $cond: [{ $eq: [{ $size: "$invalid_internet" }, 0] }, "no invalid internet examples", "$invalid_internet"]
      },
      invalid_life_expectancy_count: { $size: "$invalid_life_expectancy" },
      invalid_life_expectancy_examples: {
        $cond: [{ $eq: [{ $size: "$invalid_life_expectancy" }, 0] }, "no invalid life expectancy examples", "$invalid_life_expectancy"]
      },
      invalid_co2_count: { $size: "$invalid_co2" },
      invalid_co2_examples: {
        $cond: [{ $eq: [{ $size: "$invalid_co2" }, 0] }, "no invalid CO2 examples", "$invalid_co2"]
      }
    }
  }
]).toArray()
```

**Komentář:** Dotaz validuje rozsahy hodnot, ale vrací souhrnný dokument i tehdy, když nenajde žádnou chybu. V reportu je pak jasné, že kontrola proběhla a dopadla v pořádku.

## Dotaz 6
Porovnat hodnoty `happiness_score` v master kolekci proti zdrojove kolekci a vratit souhrn konzistence.

**Kolekce:** `country_year_master`, `happiness_country_year`

```javascript
db = db.getSiblingDB("worlddb");

db.country_year_master.aggregate([
  // Ke kazdemu master radku dohledam puvodni happiness radek podle iso3, roku a nazvu zeme.
  {
    $lookup: {
      from: "happiness_country_year",
      let: { iso3: "$iso3", year: "$year", country: "$country" },
      pipeline: [
        {
          $match: {
            $expr: {
              $and: [
                { $eq: ["$iso3", "$$iso3"] },
                { $eq: ["$year", "$$year"] },
                { $eq: ["$country", "$$country"] }
              ]
            }
          }
        },
        { $project: { _id: 0, happiness_score: 1, country: 1 } }
      ],
      as: "source_happiness"
    }
  },
  { $unwind: "$source_happiness" },
  {
    $addFields: {
      score_difference: {
        $abs: { $subtract: ["$happiness_score", "$source_happiness.happiness_score"] }
      }
    }
  },
  {
    $facet: {
      summary: [
        {
          $group: {
            _id: null,
            compared_rows: { $sum: 1 },
            mismatch_rows: { $sum: { $cond: [{ $gt: ["$score_difference", 0.000001] }, 1, 0] } },
            max_difference: { $max: "$score_difference" }
          }
        },
        {
          $project: {
            _id: 0,
            compared_rows: 1,
            mismatch_rows: 1,
            max_difference: { $round: ["$max_difference", 8] },
            consistency_status: {
              $cond: [{ $eq: ["$mismatch_rows", 0] }, "OK - master matches source happiness", "MISMATCH FOUND"]
            }
          }
        }
      ],
      mismatch_examples: [
        { $match: { score_difference: { $gt: 0.000001 } } },
        {
          $project: {
            _id: 0,
            iso3: 1,
            country_master: "$country",
            country_source: "$source_happiness.country",
            year: 1,
            master_happiness: "$happiness_score",
            source_happiness: "$source_happiness.happiness_score",
            score_difference: 1
          }
        },
        { $sort: { score_difference: -1, iso3: 1, year: 1 } },
        { $limit: 10 }
      ]
    }
  },
  {
    $project: {
      summary: 1,
      mismatch_examples: {
        $cond: [
          { $eq: [{ $size: "$mismatch_examples" }, 0] },
          "no mismatch examples",
          "$mismatch_examples"
        ]
      }
    }
  }
]).toArray()
```

**Komentář:** Dotaz kontroluje, zda se při tvorbě master kolekce nezměnil happiness score. Výstup vrací počet porovnaných řádků a stav konzistence, takže není prázdný ani při úspěšné kontrole. Název země je v lookupu důležitý hlavně u případů typu Cyprus/North Cyprus.

---

# Kategorie 4: Profily Faktoru Happiness

Tato kategorie pracuje hlavne s vnitrni strukturou datasetu World Happiness. Dotazy se nezameruji jen na celkove skore, ale rozkladaji ho na faktory jako GDP, social support, health, freedom, generosity a corruption.

## Dotaz 1
Najit zeme s nejvyrovnanejsim profilem happiness faktoru v letech 2015-2019.

**Kolekce:** `happiness_country_year`

```javascript
db = db.getSiblingDB("worlddb");

db.happiness_country_year.aggregate([
  // Beru jen radky, kde jsou dostupne vsechny hlavni faktory happiness.
  {
    $match: {
      year: { $gte: 2015, $lte: 2019 },
      gdp_factor: { $ne: null },
      social_support_factor: { $ne: null },
      health_factor: { $ne: null },
      freedom_factor: { $ne: null },
      generosity_factor: { $ne: null },
      corruption_factor: { $ne: null }
    }
  },
  // Pro kazdy radek si spocitam prumer faktoru a rozsah mezi nejsilnejsim a nejslabsim faktorem.
  {
    $addFields: {
      factor_values: [
        "$gdp_factor",
        "$social_support_factor",
        "$health_factor",
        "$freedom_factor",
        "$generosity_factor",
        "$corruption_factor"
      ]
    }
  },
  {
    $addFields: {
      factor_balance_range: {
        $subtract: [{ $max: "$factor_values" }, { $min: "$factor_values" }]
      },
      factor_avg: { $avg: "$factor_values" }
    }
  },
  // Na urovni zeme agreguju prumernou vyrovnanost profilu.
  {
    $group: {
      _id: { iso3: "$iso3", country: "$country" },
      years_observed: { $sum: 1 },
      avg_happiness: { $avg: "$happiness_score" },
      avg_factor_balance_range: { $avg: "$factor_balance_range" },
      avg_factor_level: { $avg: "$factor_avg" }
    }
  },
  {
    $match: { years_observed: { $gte: 4 } }
  },
  {
    $project: {
      _id: 0,
      iso3: "$_id.iso3",
      country: "$_id.country",
      years_observed: 1,
      avg_happiness: { $round: ["$avg_happiness", 3] },
      avg_factor_level: { $round: ["$avg_factor_level", 3] },
      avg_factor_balance_range: { $round: ["$avg_factor_balance_range", 3] }
    }
  },
  // Nejmensi range znamena, ze zadny faktor vyrazne nevycniva ani nepropada.
  { $sort: { avg_factor_balance_range: 1, avg_happiness: -1 } },
  { $limit: 15 }
]).toArray()
```

**Komentář:** Dotaz nehledá jen nejšťastnější státy, ale státy s nejrovnoměrnějším profilem faktorů. Na datech pomáhá ukázat, kde je happiness postavené relativně vyváženě, ne pouze na jednom dominantním faktoru.

## Dotaz 2
Zjistit, ktery happiness faktor je u jednotlivych country-year zaznamu nejsilnejsi.

**Kolekce:** `happiness_country_year`

```javascript
db = db.getSiblingDB("worlddb");

db.happiness_country_year.aggregate([
  // Z kazdeho radku vytvorim pole dvojic faktor-hodnota.
  {
    $project: {
      _id: 0,
      country: 1,
      iso3: 1,
      year: 1,
      happiness_score: 1,
      factors: [
        { name: "gdp", value: "$gdp_factor" },
        { name: "social_support", value: "$social_support_factor" },
        { name: "health", value: "$health_factor" },
        { name: "freedom", value: "$freedom_factor" },
        { name: "generosity", value: "$generosity_factor" },
        { name: "corruption", value: "$corruption_factor" }
      ]
    }
  },
  { $unwind: "$factors" },
  // Seradim faktory uvnitr jednoho country-year zaznamu podle hodnoty.
  { $sort: { iso3: 1, year: 1, "factors.value": -1 } },
  {
    $group: {
      _id: { iso3: "$iso3", country: "$country", year: "$year" },
      happiness_score: { $first: "$happiness_score" },
      dominant_factor: { $first: "$factors.name" },
      dominant_factor_value: { $first: "$factors.value" }
    }
  },
  {
    $project: {
      _id: 0,
      iso3: "$_id.iso3",
      country: "$_id.country",
      year: "$_id.year",
      happiness_score: { $round: ["$happiness_score", 3] },
      dominant_factor: 1,
      dominant_factor_value: { $round: ["$dominant_factor_value", 3] }
    }
  },
  { $sort: { year: 1, dominant_factor: 1, happiness_score: -1 } },
  { $limit: 25 }
]).toArray()
```

**Komentář:** Dotaz převádí sloupce faktorů do pracovního pole a hledá nejsilnější faktor pro každý stát a rok. Výstup je dobrý pro vysvětlení, že happiness score není jedna izolovaná hodnota, ale skládá se z více dimenzí.

## Dotaz 3
Najit zeme s vysokym happiness score, i kdyz jejich `gdp_factor` patri mezi nizsi hodnoty.

**Kolekce:** `happiness_country_year`

```javascript
db = db.getSiblingDB("worlddb");

db.happiness_country_year.aggregate([
  // Omezim se na hlavni obdobi a validni hodnoty.
  {
    $match: {
      year: { $gte: 2015, $lte: 2019 },
      happiness_score: { $ne: null },
      gdp_factor: { $ne: null },
      social_support_factor: { $ne: null },
      health_factor: { $ne: null }
    }
  },
  // Zamerne beru vysoke happiness pri nizsim GDP faktoru.
  {
    $match: {
      happiness_score: { $gte: 6 },
      gdp_factor: { $lte: 1.0 }
    }
  },
  {
    $project: {
      _id: 0,
      country: 1,
      iso3: 1,
      year: 1,
      happiness_score: { $round: ["$happiness_score", 3] },
      gdp_factor: { $round: ["$gdp_factor", 3] },
      social_support_factor: { $round: ["$social_support_factor", 3] },
      health_factor: { $round: ["$health_factor", 3] },
      freedom_factor: { $round: ["$freedom_factor", 3] }
    }
  },
  // Nahore jsou zeme, kde vysoke happiness nevyplyva jen z GDP faktoru.
  { $sort: { happiness_score: -1, gdp_factor: 1 } },
  { $limit: 20 }
]).toArray()
```

**Komentář:** Dotaz pomáhá najít případy, kde samotný ekonomický faktor nevysvětluje vysoké happiness. Na konkrétních datech se pak dá ukázat, které jiné faktory mohou výsledek podpírat.

## Dotaz 4
Porovnat prumernou svobodu, socialni podporu a vnimani korupce podle urovne happiness.

**Kolekce:** `happiness_country_year`

```javascript
db = db.getSiblingDB("worlddb");

db.happiness_country_year.aggregate([
  // Pracuju jen s radky, kde mam vsechny faktory pro porovnani.
  {
    $match: {
      year: { $gte: 2015, $lte: 2019 },
      happiness_score: { $ne: null },
      social_support_factor: { $ne: null },
      freedom_factor: { $ne: null },
      corruption_factor: { $ne: null }
    }
  },
  // Rozdelim zaznamy do slovnich skupin podle vysky happiness.
  {
    $addFields: {
      happiness_group: {
        $switch: {
          branches: [
            { case: { $gte: ["$happiness_score", 7] }, then: "high_happiness" },
            { case: { $gte: ["$happiness_score", 5] }, then: "middle_happiness" }
          ],
          default: "low_happiness"
        }
      }
    }
  },
  {
    $group: {
      _id: "$happiness_group",
      row_count: { $sum: 1 },
      avg_happiness: { $avg: "$happiness_score" },
      avg_social_support: { $avg: "$social_support_factor" },
      avg_freedom: { $avg: "$freedom_factor" },
      avg_corruption_factor: { $avg: "$corruption_factor" }
    }
  },
  {
    $project: {
      _id: 0,
      happiness_group: "$_id",
      row_count: 1,
      avg_happiness: { $round: ["$avg_happiness", 3] },
      avg_social_support: { $round: ["$avg_social_support", 3] },
      avg_freedom: { $round: ["$avg_freedom", 3] },
      avg_corruption_factor: { $round: ["$avg_corruption_factor", 3] }
    }
  },
  { $sort: { avg_happiness: -1 } }
]).toArray()
```

**Komentář:** Dotaz tvoří přehled podle skupin happiness, ne podle jednotlivých zemí. Na výsledku je možné ukázat, jak se mezi skupinami mění sociální podpora, svoboda a faktor korupce.

## Dotaz 5
Najit zeme s nejvetsi volatilitou vybranych happiness faktoru v case.

**Kolekce:** `happiness_country_year`

```javascript
db = db.getSiblingDB("worlddb");

db.happiness_country_year.aggregate([
  // Volatilitu pocitam jen v hlavnim obdobi 2015-2019.
  {
    $match: {
      year: { $gte: 2015, $lte: 2019 },
      social_support_factor: { $ne: null },
      freedom_factor: { $ne: null },
      generosity_factor: { $ne: null }
    }
  },
  {
    $group: {
      _id: { iso3: "$iso3", country: "$country" },
      years_observed: { $sum: 1 },
      avg_happiness: { $avg: "$happiness_score" },
      std_social_support: { $stdDevSamp: "$social_support_factor" },
      std_freedom: { $stdDevSamp: "$freedom_factor" },
      std_generosity: { $stdDevSamp: "$generosity_factor" }
    }
  },
  {
    $match: {
      years_observed: { $gte: 4 },
      std_social_support: { $ne: null },
      std_freedom: { $ne: null },
      std_generosity: { $ne: null }
    }
  },
  // Celkova volatilita je soucet smerodatnych odchylek vybranych faktoru.
  {
    $addFields: {
      factor_volatility_score: {
        $add: ["$std_social_support", "$std_freedom", "$std_generosity"]
      }
    }
  },
  {
    $project: {
      _id: 0,
      iso3: "$_id.iso3",
      country: "$_id.country",
      years_observed: 1,
      avg_happiness: { $round: ["$avg_happiness", 3] },
      std_social_support: { $round: ["$std_social_support", 4] },
      std_freedom: { $round: ["$std_freedom", 4] },
      std_generosity: { $round: ["$std_generosity", 4] },
      factor_volatility_score: { $round: ["$factor_volatility_score", 4] }
    }
  },
  { $sort: { factor_volatility_score: -1 } },
  { $limit: 20 }
]).toArray()
```

**Komentář:** Dotaz ukazuje, kde se v čase nejvíc mění vnitřní složky happiness. Není to totéž jako volatilita celkového skóre, protože zde sleduju konkrétní faktory uvnitř datasetu.

## Dotaz 6
Zobrazit rocni prumer hlavniho happiness score a jeho faktoru pro cele dostupne obdobi.

**Kolekce:** `happiness_country_year`

```javascript
db = db.getSiblingDB("worlddb");

db.happiness_country_year.aggregate([
  // Roky agreguju pres vsechny dostupne zeme v happiness datasetu.
  {
    $match: {
      happiness_score: { $ne: null }
    }
  },
  {
    $group: {
      _id: "$year",
      countries_count: { $sum: 1 },
      avg_happiness: { $avg: "$happiness_score" },
      avg_gdp_factor: { $avg: "$gdp_factor" },
      avg_social_support_factor: { $avg: "$social_support_factor" },
      avg_health_factor: { $avg: "$health_factor" },
      avg_freedom_factor: { $avg: "$freedom_factor" },
      avg_generosity_factor: { $avg: "$generosity_factor" },
      avg_corruption_factor: { $avg: "$corruption_factor" }
    }
  },
  {
    $project: {
      _id: 0,
      year: "$_id",
      countries_count: 1,
      avg_happiness: { $round: ["$avg_happiness", 3] },
      avg_gdp_factor: { $round: ["$avg_gdp_factor", 3] },
      avg_social_support_factor: { $round: ["$avg_social_support_factor", 3] },
      avg_health_factor: { $round: ["$avg_health_factor", 3] },
      avg_freedom_factor: { $round: ["$avg_freedom_factor", 3] },
      avg_generosity_factor: { $round: ["$avg_generosity_factor", 3] },
      avg_corruption_factor: { $round: ["$avg_corruption_factor", 3] }
    }
  },
  { $sort: { year: 1 } }
]).toArray()
```

**Komentář:** Dotaz dává roční souhrn celé happiness kolekce. Hodí se pro rychlé vysvětlení, jak se v datech mění průměrné skóre a jeho hlavní složky mezi jednotlivými roky.

---

# Kategorie 5: Historicke Trendy CO2 A WDI

Tato kategorie pouziva delsi casove rady z kolekci `co2_country_year` a `wdi_selected_long`. Dotazy se lisi od predchozich kategorii tim, ze se nedrzi jen let 2015-2019 a nehledaji pouze happiness vysledky, ale ukazuji historicky vyvoj emisi a vybranych rozvojovych indikatoru.

## Dotaz 1
Najit zeme s nejvetsim rustem `CO2 per capita` mezi lety 1990 a 2019.

**Kolekce:** `co2_country_year`

```javascript
db = db.getSiblingDB("worlddb");

db.co2_country_year.aggregate([
  // Beru dva pevne body v case, aby bylo srovnani pro vsechny zeme stejne.
  {
    $match: {
      year: { $in: [1990, 2019] },
      co2_per_capita_t: { $ne: null },
      $expr: { $ne: [{ $toString: "$co2_per_capita_t" }, "NaN"] }
    }
  },
  {
    $group: {
      _id: { iso3: "$iso3", country: "$country" },
      co2_1990: {
        $max: { $cond: [{ $eq: ["$year", 1990] }, "$co2_per_capita_t", null] }
      },
      co2_2019: {
        $max: { $cond: [{ $eq: ["$year", 2019] }, "$co2_per_capita_t", null] }
      }
    }
  },
  // Pro procentni zmenu potrebuju obe hodnoty a kladny zacatek.
  {
    $match: {
      co2_1990: { $ne: null, $gt: 0 },
      co2_2019: { $ne: null }
    }
  },
  {
    $addFields: {
      co2_change_t: { $subtract: ["$co2_2019", "$co2_1990"] },
      co2_growth_pct: {
        $multiply: [
          { $divide: [{ $subtract: ["$co2_2019", "$co2_1990"] }, "$co2_1990"] },
          100
        ]
      }
    }
  },
  {
    $project: {
      _id: 0,
      iso3: "$_id.iso3",
      country: "$_id.country",
      co2_1990: { $round: ["$co2_1990", 3] },
      co2_2019: { $round: ["$co2_2019", 3] },
      co2_change_t: { $round: ["$co2_change_t", 3] },
      co2_growth_pct: { $round: ["$co2_growth_pct", 2] }
    }
  },
  { $sort: { co2_growth_pct: -1 } },
  { $limit: 20 }
]).toArray()
```

**Komentář:** Dotaz porovnává dlouhodobý vývoj emisí na osobu. Na rozdíl od happiness dotazů neřeší jen posledních několik let, ale ukazuje změnu mezi rokem 1990 a 2019.

## Dotaz 2
Rozlozit celkove emise v roce 2019 podle zdroju: uhli, ropa, plyn, cement a flaring.

**Kolekce:** `co2_country_year`

```javascript
db = db.getSiblingDB("worlddb");

db.co2_country_year.aggregate([
  // Beru jen zeme s vetsi celkovou hodnotou emisi, aby podily nebyly postavene na drobnych cislech.
  {
    $match: {
      year: 2019,
      co2_total_mt: { $gt: 50 }
    }
  },
  // Missing hodnoty u dilcich zdroju beru jako nulu.
  {
    $addFields: {
      coal: { $ifNull: ["$co2_coal_mt", 0] },
      oil: { $ifNull: ["$co2_oil_mt", 0] },
      gas: { $ifNull: ["$co2_gas_mt", 0] },
      cement: { $ifNull: ["$co2_cement_mt", 0] },
      flaring: { $ifNull: ["$co2_flaring_mt", 0] }
    }
  },
  // Prepocitam podily jednotlivych zdroju na celkovych emisich.
  {
    $project: {
      _id: 0,
      country: 1,
      iso3: 1,
      year: 1,
      co2_total_mt: { $round: ["$co2_total_mt", 2] },
      coal_share_pct: { $round: [{ $multiply: [{ $divide: ["$coal", "$co2_total_mt"] }, 100] }, 2] },
      oil_share_pct: { $round: [{ $multiply: [{ $divide: ["$oil", "$co2_total_mt"] }, 100] }, 2] },
      gas_share_pct: { $round: [{ $multiply: [{ $divide: ["$gas", "$co2_total_mt"] }, 100] }, 2] },
      cement_share_pct: { $round: [{ $multiply: [{ $divide: ["$cement", "$co2_total_mt"] }, 100] }, 2] },
      flaring_share_pct: { $round: [{ $multiply: [{ $divide: ["$flaring", "$co2_total_mt"] }, 100] }, 2] }
    }
  },
  { $sort: { co2_total_mt: -1 } },
  { $limit: 20 }
]).toArray()
```

**Komentář:** Dotaz nepracuje jen s jedním číslem CO2, ale rozkládá ho podle zdrojů. Na datech je dobře vidět, zda je emisní profil země tažen hlavně uhlím, ropou nebo plynem.

## Dotaz 3
Spocitat globalni soucet CO2 po dekadach a ukazat dlouhodoby vyvoj emisi.

**Kolekce:** `co2_country_year`

```javascript
db = db.getSiblingDB("worlddb");

db.co2_country_year.aggregate([
  // Vyloucim agregaty bez ISO3 a radky bez celkovych emisi.
  {
    $match: {
      iso3: { $ne: null },
      co2_total_mt: { $ne: null },
      year: { $gte: 1950 }
    }
  },
  // Rok prepoctu na dekadu, napr. 1997 -> 1990.
  {
    $addFields: {
      decade: {
        $multiply: [{ $floor: { $divide: ["$year", 10] } }, 10]
      }
    }
  },
  {
    $group: {
      _id: "$decade",
      country_year_rows: { $sum: 1 },
      avg_yearly_total_mt: { $avg: "$co2_total_mt" },
      max_country_year_emission_mt: { $max: "$co2_total_mt" }
    }
  },
  {
    $project: {
      _id: 0,
      decade: "$_id",
      country_year_rows: 1,
      avg_country_year_total_mt: { $round: ["$avg_yearly_total_mt", 2] },
      max_country_year_emission_mt: { $round: ["$max_country_year_emission_mt", 2] }
    }
  },
  { $sort: { decade: 1 } }
]).toArray()
```

**Komentář:** Dotaz agreguje CO2 data do dekád, takže neukazuje jednotlivé země, ale dlouhodobý vývoj datasetu. Je vhodný jako doplněk k detailním country-year dotazům.

## Dotaz 4
Najit zeme s nejvetsim rustem podilu uzivatelu internetu mezi roky 2000 a 2017.

**Kolekce:** `wdi_selected_long`

```javascript
db = db.getSiblingDB("worlddb");

db.wdi_selected_long.aggregate([
  // Internet users beru jako jeden konkretni WDI indikator.
  {
    $match: {
      indicator: "internet_users_pct",
      year: { $in: [2000, 2017] },
      value: { $ne: null },
      $expr: { $ne: [{ $toString: "$value" }, "NaN"] }
    }
  },
  {
    $group: {
      _id: { iso3: "$iso3", country: "$country" },
      internet_2000: {
        $max: { $cond: [{ $eq: ["$year", 2000] }, "$value", null] }
      },
      internet_2017: {
        $max: { $cond: [{ $eq: ["$year", 2017] }, "$value", null] }
      }
    }
  },
  {
    $match: {
      internet_2000: { $ne: null },
      internet_2017: { $ne: null }
    }
  },
  {
    $addFields: {
      internet_change_pct_points: { $subtract: ["$internet_2017", "$internet_2000"] }
    }
  },
  {
    $project: {
      _id: 0,
      iso3: "$_id.iso3",
      country: "$_id.country",
      internet_2000: { $round: ["$internet_2000", 2] },
      internet_2017: { $round: ["$internet_2017", 2] },
      internet_change_pct_points: { $round: ["$internet_change_pct_points", 2] }
    }
  },
  { $sort: { internet_change_pct_points: -1 } },
  { $limit: 20 }
]).toArray()
```

**Komentář:** Dotaz pracuje s WDI indikátorem mimo happiness i CO2 a ukazuje digitalizační změnu. Použití procentních bodů je zde čitelnější než relativní procentní růst.

## Dotaz 5
Najit zeme s nejvetsim rustem ocekavane delky zivota mezi roky 1960 a 2017.

**Kolekce:** `wdi_selected_long`

```javascript
db = db.getSiblingDB("worlddb");

db.wdi_selected_long.aggregate([
  // Life expectancy je dostupna jako dlouha casova rada, proto ji srovnavam od roku 1960.
  {
    $match: {
      indicator: "life_expectancy_years",
      year: { $in: [1960, 2017] },
      value: { $ne: null },
      $expr: { $ne: [{ $toString: "$value" }, "NaN"] }
    }
  },
  {
    $group: {
      _id: { iso3: "$iso3", country: "$country" },
      life_1960: {
        $max: { $cond: [{ $eq: ["$year", 1960] }, "$value", null] }
      },
      life_2017: {
        $max: { $cond: [{ $eq: ["$year", 2017] }, "$value", null] }
      }
    }
  },
  {
    $match: {
      life_1960: { $ne: null },
      life_2017: { $ne: null }
    }
  },
  {
    $addFields: {
      life_gain_years: { $subtract: ["$life_2017", "$life_1960"] }
    }
  },
  {
    $project: {
      _id: 0,
      iso3: "$_id.iso3",
      country: "$_id.country",
      life_1960: { $round: ["$life_1960", 2] },
      life_2017: { $round: ["$life_2017", 2] },
      life_gain_years: { $round: ["$life_gain_years", 2] }
    }
  },
  { $sort: { life_gain_years: -1 } },
  { $limit: 20 }
]).toArray()
```

**Komentář:** Dotaz ukazuje dlouhodobý rozvojový indikátor, který není vázaný jen na ekonomiku. Na datech lze jednoduše vysvětlit, kde se životní délka za sledované období zlepšila nejvíce.

## Dotaz 6
Najit country-year zaznamy s vysokym obchodem vuci GDP a soucasne nizkou nezamestnanosti.

**Kolekce:** `wdi_selected_long`

```javascript
db = db.getSiblingDB("worlddb");

db.wdi_selected_long.aggregate([
  // Z dlouheho WDI formatu beru jen dva indikatory, ktere chci porovnat vedle sebe.
  {
    $match: {
      year: { $gte: 2015, $lte: 2017 },
      indicator: { $in: ["trade_pct_gdp", "unemployment_pct"] },
      value: { $ne: null },
      $expr: { $ne: [{ $toString: "$value" }, "NaN"] }
    }
  },
  // Pivot z dlouheho formatu do jednoho radku za zemi a rok.
  {
    $group: {
      _id: { iso3: "$iso3", country: "$country", year: "$year" },
      trade_pct_gdp: {
        $max: {
          $cond: [{ $eq: ["$indicator", "trade_pct_gdp"] }, "$value", null]
        }
      },
      unemployment_pct: {
        $max: {
          $cond: [{ $eq: ["$indicator", "unemployment_pct"] }, "$value", null]
        }
      }
    }
  },
  {
    $match: {
      trade_pct_gdp: { $ne: null, $gte: 100 },
      unemployment_pct: { $ne: null, $lte: 5 }
    }
  },
  {
    $project: {
      _id: 0,
      iso3: "$_id.iso3",
      country: "$_id.country",
      year: "$_id.year",
      trade_pct_gdp: { $round: ["$trade_pct_gdp", 2] },
      unemployment_pct: { $round: ["$unemployment_pct", 2] }
    }
  },
  { $sort: { trade_pct_gdp: -1, unemployment_pct: 1 } },
  { $limit: 20 }
]).toArray()
```

**Komentář:** Dotaz ukazuje práci s dlouhým WDI formátem bez použití master kolekce. Nejdřív vybere dva indikátory, potom je převede do jednoho řádku a hledá ekonomiky s vysokou otevřeností a nízkou nezaměstnaností.
