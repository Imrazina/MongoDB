# Vystupy Dotazu

Zdrojovy soubor dotazu: `/Users/shabossova/MongoDB/Dotazy/dotazy.md`

Spusteno dotazu: `30`

## [01] Kategorie 1: Propojovani Dat A Vazeb Mezi Datasety / Dotaz 1

**Stav:** OK

```text
[
  {
    country: 'Iceland',
    year: 2015,
    iso3: 'ISL',
    happiness_score: 7.561,
    gdp_per_capita_usd: 52428.6,
    co2_per_capita_t: 10.674,
    co2_total_mt: 3.534
  },
  {
    country: 'Norway',
    year: 2017,
    iso3: 'NOR',
    happiness_score: 7.537,
    gdp_per_capita_usd: 75704.25,
    co2_per_capita_t: 8.384,
    co2_total_mt: 44.242
  },
  {
    country: 'Denmark',
    year: 2015,
    iso3: 'DNK',
    happiness_score: 7.527,
    gdp_per_capita_usd: 53254.85,
    co2_per_capita_t: 6.205,
    co2_total_mt: 35.228
  },
  {
    country: 'Denmark',
    year: 2016,
    iso3: 'DNK',
    happiness_score: 7.526,
    gdp_per_capita_usd: 54467.1,
    co2_per_capita_t: 6.489,
    co2_total_mt: 37.033
  },
  {
    country: 'Norway',
    year: 2015,
    iso3: 'NOR',
    happiness_score: 7.522,
    gdp_per_capita_usd: 74521.57,
    co2_per_capita_t: 8.784,
    co2_total_mt: 45.59
  },
  {
    country: 'Denmark',
    year: 2017,
    iso3: 'DNK',
    happiness_score: 7.522,
    gdp_per_capita_usd: 57218.85,
    co2_per_capita_t: 6.062,
    co2_total_mt: 34.78
  },
  {
    country: 'Iceland',
    year: 2017,
    iso3: 'ISL',
    happiness_score: 7.504,
    gdp_per_capita_usd: 71311.79,
    co2_per_capita_t: 10.481,
    co2_total_mt: 3.602
  },
  {
    country: 'Iceland',
    year: 2016,
    iso3: 'ISL',
    happiness_score: 7.501,
    gdp_per_capita_usd: 61757.95,
    co2_per_capita_t: 10.383,
    co2_total_mt: 3.485
  },
  {
    country: 'Norway',
    year: 2016,
    iso3: 'NOR',
    happiness_score: 7.498,
    gdp_per_capita_usd: 70941.53,
    co2_per_capita_t: 8.549,
    co2_total_mt: 44.765
  },
  {
    country: 'Finland',
    year: 2017,
    iso3: 'FIN',
    happiness_score: 7.469,
    gdp_per_capita_usd: 45804.65,
    co2_per_capita_t: 8.093,
    co2_total_mt: 44.578
  }
]
```

---

## [02] Kategorie 1: Propojovani Dat A Vazeb Mezi Datasety / Dotaz 2

**Stav:** OK

```text
[
  {
    weakest_links: [
      {
        country: 'Taiwan',
        year: 2015,
        iso3: 'TWN',
        has_co2: true,
        missing_wdi_indicators: [
          'gdp_per_capita_usd',
          'life_expectancy_years',
          'internet_users_pct'
        ],
        wdi_indicator_count: 0,
        linkage_score: 1,
        happiness_score: 6.298
      },
      {
        country: 'Taiwan',
        year: 2016,
        iso3: 'TWN',
        has_co2: true,
        missing_wdi_indicators: [
          'gdp_per_capita_usd',
          'life_expectancy_years',
          'internet_users_pct'
        ],
        wdi_indicator_count: 0,
        linkage_score: 1,
        happiness_score: 6.379
      },
      {
        country: 'Taiwan Province of China',
        year: 2017,
        iso3: 'TWN',
        has_co2: true,
        missing_wdi_indicators: [
          'gdp_per_capita_usd',
          'life_expectancy_years',
          'internet_users_pct'
        ],
        wdi_indicator_count: 0,
        linkage_score: 1,
        happiness_score: 6.422
      },
      {
        country: 'Kosovo',
        year: 2015,
        iso3: 'XKX',
        has_co2: false,
        missing_wdi_indicators: [ 'internet_users_pct' ],
        wdi_indicator_count: 2,
        linkage_score: 2,
        happiness_score: 5.589
      },
      {
        country: 'Kosovo',
        year: 2016,
        iso3: 'XKX',
        has_co2: false,
        missing_wdi_indicators: [ 'internet_users_pct' ],
        wdi_indicator_count: 2,
        linkage_score: 2,
        happiness_score: 5.401
      },
      {
        country: 'Kosovo',
        year: 2017,
        iso3: 'XKX',
        has_co2: false,
        missing_wdi_indicators: [ 'internet_users_pct' ],
        wdi_indicator_count: 2,
        linkage_score: 2,
        happiness_score: 5.279
      },
      {
        country: 'Syria',
        year: 2015,
        iso3: 'SYR',
        has_co2: true,
        missing_wdi_indicators: [ 'gdp_per_capita_usd' ],
        wdi_indicator_count: 2,
        linkage_score: 3,
        happiness_score: 3.006
      },
      {
        country: 'Venezuela',
        year: 2015,
        iso3: 'VEN',
        has_co2: true,
        missing_wdi_indicators: [ 'gdp_per_capita_usd' ],
        wdi_indicator_count: 2,
        linkage_score: 3,
        happiness_score: 6.81
      },
      {
        country: 'Syria',
        year: 2016,
        iso3: 'SYR',
        has_co2: true,
        missing_wdi_indicators: [ 'gdp_per_capita_usd' ],
        wdi_indicator_count: 2,
        linkage_score: 3,
        happiness_score: 3.069
      },
      {
        country: 'Venezuela',
        year: 2016,
        iso3: 'VEN',
        has_co2: true,
        missing_wdi_indicators: [ 'gdp_per_capita_usd' ],
        wdi_indicator_count: 2,
        linkage_score: 3,
        happiness_score: 6.084
      },
      {
        country: 'South Sudan',
        year: 2017,
        iso3: 'SSD',
        has_co2: true,
        missing_wdi_indicators: [ 'gdp_per_capita_usd' ],
        wdi_indicator_count: 2,
        linkage_score: 3,
        happiness_score: 3.591
      },
      {
        country: 'Syria',
        year: 2017,
        iso3: 'SYR',
        has_co2: true,
        missing_wdi_indicators: [ 'gdp_per_capita_usd' ],
        wdi_indicator_count: 2,
        linkage_score: 3,
        happiness_score: 3.462
      },
      {
        country: 'Venezuela',
        year: 2017,
        iso3: 'VEN',
        has_co2: true,
        missing_wdi_indicators: [ 'gdp_per_capita_usd' ],
        wdi_indicator_count: 2,
        linkage_score: 3,
        happiness_score: 5.25
      }
    ],
    coverage_by_year: [
      {
        total_rows: 158,
        rows_with_co2: 157,
        rows_with_all_3_wdi: 154,
        fully_linked_rows: 154,
        year: 2015,
        full_link_rate_pct: 97.47
      },
      {
        total_rows: 157,
        rows_with_co2: 156,
        rows_with_all_3_wdi: 153,
        fully_linked_rows: 153,
        year: 2016,
        full_link_rate_pct: 97.45
      },
      {
        total_rows: 155,
        rows_with_co2: 154,
        rows_with_all_3_wdi: 150,
        fully_linked_rows: 150,
        year: 2017,
        full_link_rate_pct: 96.77
      }
    ],
    coverage_summary: [
      {
        total_rows: 470,
        rows_with_co2: 467,
        rows_with_all_3_wdi: 457,
        fully_linked_rows: 457,
        full_link_rate_pct: 97.23
      }
    ]
  }
]
```

---

## [03] Kategorie 1: Propojovani Dat A Vazeb Mezi Datasety / Dotaz 3

**Stav:** OK

```text
[
  {
    country: 'Afghanistan',
    year: 2016,
    iso3: 'AFG',
    happiness_score: 3.36,
    prev_happiness: 3.575,
    life_expectancy_years: 63.67,
    prev_life: 63.29
  },
  {
    country: 'Albania',
    year: 2016,
    iso3: 'ALB',
    happiness_score: 4.655,
    prev_happiness: 4.959,
    life_expectancy_years: 78.34,
    prev_life: 78.17
  },
  {
    country: 'Angola',
    year: 2016,
    iso3: 'AGO',
    happiness_score: 3.866,
    prev_happiness: 4.033,
    life_expectancy_years: 61.55,
    prev_life: 61.24
  },
  {
    country: 'Austria',
    year: 2016,
    iso3: 'AUT',
    happiness_score: 7.119,
    prev_happiness: 7.2,
    life_expectancy_years: 81.64,
    prev_life: 81.19
  },
  {
    country: 'Bangladesh',
    year: 2016,
    iso3: 'BGD',
    happiness_score: 4.643,
    prev_happiness: 4.694,
    life_expectancy_years: 72.49,
    prev_life: 72.16
  },
  {
    country: 'Belarus',
    year: 2016,
    iso3: 'BLR',
    happiness_score: 5.802,
    prev_happiness: 5.813,
    life_expectancy_years: 73.83,
    prev_life: 73.62
  },
  {
    country: 'Belgium',
    year: 2016,
    iso3: 'BEL',
    happiness_score: 6.929,
    prev_happiness: 6.937,
    life_expectancy_years: 81.44,
    prev_life: 80.99
  },
  {
    country: 'Bhutan',
    year: 2016,
    iso3: 'BTN',
    happiness_score: 5.196,
    prev_happiness: 5.253,
    life_expectancy_years: 70.2,
    prev_life: 69.82
  },
  {
    country: 'Bolivia',
    year: 2016,
    iso3: 'BOL',
    happiness_score: 5.822,
    prev_happiness: 5.89,
    life_expectancy_years: 69.12,
    prev_life: 68.76
  },
  {
    country: 'Botswana',
    year: 2016,
    iso3: 'BWA',
    happiness_score: 3.974,
    prev_happiness: 4.332,
    life_expectancy_years: 66.8,
    prev_life: 65.85
  },
  {
    country: 'Brazil',
    year: 2016,
    iso3: 'BRA',
    happiness_score: 6.952,
    prev_happiness: 6.983,
    life_expectancy_years: 75.51,
    prev_life: 75.28
  },
  {
    country: 'Bulgaria',
    year: 2016,
    iso3: 'BGR',
    happiness_score: 4.217,
    prev_happiness: 4.218,
    life_expectancy_years: 74.81,
    prev_life: 74.61
  },
  {
    country: 'Canada',
    year: 2016,
    iso3: 'CAN',
    happiness_score: 7.404,
    prev_happiness: 7.427,
    life_expectancy_years: 82.3,
    prev_life: 81.9
  },
  {
    country: 'Congo (Kinshasa)',
    year: 2016,
    iso3: 'COD',
    happiness_score: 4.272,
    prev_happiness: 4.517,
    life_expectancy_years: 59.62,
    prev_life: 59.2
  },
  {
    country: 'Costa Rica',
    year: 2016,
    iso3: 'CRI',
    happiness_score: 7.087,
    prev_happiness: 7.226,
    life_expectancy_years: 79.83,
    prev_life: 79.63
  },
  {
    country: 'Croatia',
    year: 2016,
    iso3: 'HRV',
    happiness_score: 5.488,
    prev_happiness: 5.759,
    life_expectancy_years: 78.02,
    prev_life: 77.28
  },
  {
    country: 'Cyprus',
    year: 2016,
    iso3: 'CYP',
    happiness_score: 5.546,
    prev_happiness: 5.695,
    life_expectancy_years: 80.51,
    prev_life: 80.34
  },
  {
    country: 'Denmark',
    year: 2016,
    iso3: 'DNK',
    happiness_score: 7.526,
    prev_happiness: 7.527,
    life_expectancy_years: 80.85,
    prev_life: 80.7
  },
  {
    country: 'El Salvador',
    year: 2016,
    iso3: 'SLV',
    happiness_score: 6.068,
    prev_happiness: 6.13,
    life_expectancy_years: 73.51,
    prev_life: 73.27
  },
  {
    country: 'Ethiopia',
    year: 2016,
    iso3: 'ETH',
    happiness_score: 4.508,
    prev_happiness: 4.512,
    life_expectancy_years: 65.47,
    prev_life: 65.04
  }
]
```

---

## [04] Kategorie 1: Propojovani Dat A Vazeb Mezi Datasety / Dotaz 4

**Stav:** OK

```text
[
  {
    country: 'Uruguay',
    year: 2017,
    iso3: 'URY',
    happiness_score: 6.454,
    gdp_per_capita_usd: 16245.6,
    co2_per_capita_t: 1.801,
    wellbeing_efficiency: 3.584
  },
  {
    country: 'Uruguay',
    year: 2016,
    iso3: 'URY',
    happiness_score: 6.545,
    gdp_per_capita_usd: 15298.35,
    co2_per_capita_t: 1.91,
    wellbeing_efficiency: 3.4262
  },
  {
    country: 'Uruguay',
    year: 2015,
    iso3: 'URY',
    happiness_score: 6.485,
    gdp_per_capita_usd: 15524.84,
    co2_per_capita_t: 1.981,
    wellbeing_efficiency: 3.2731
  },
  {
    country: 'Panama',
    year: 2017,
    iso3: 'PAN',
    happiness_score: 6.452,
    gdp_per_capita_usd: 15196.4,
    co2_per_capita_t: 2.74,
    wellbeing_efficiency: 2.3548
  },
  {
    country: 'Malta',
    year: 2016,
    iso3: 'MLT',
    happiness_score: 6.488,
    gdp_per_capita_usd: 24758.7,
    co2_per_capita_t: 2.9,
    wellbeing_efficiency: 2.2372
  },
  {
    country: 'Malta',
    year: 2017,
    iso3: 'MLT',
    happiness_score: 6.527,
    gdp_per_capita_usd: 26748.21,
    co2_per_capita_t: 3.193,
    wellbeing_efficiency: 2.0444
  },
  {
    country: 'Malta',
    year: 2015,
    iso3: 'MLT',
    happiness_score: 6.302,
    gdp_per_capita_usd: 23715.53,
    co2_per_capita_t: 3.647,
    wellbeing_efficiency: 1.7278
  },
  {
    country: 'Sweden',
    year: 2017,
    iso3: 'SWE',
    happiness_score: 7.284,
    gdp_per_capita_usd: 53253.48,
    co2_per_capita_t: 4.246,
    wellbeing_efficiency: 1.7156
  },
  {
    country: 'Sweden',
    year: 2016,
    iso3: 'SWE',
    happiness_score: 7.291,
    gdp_per_capita_usd: 51617.54,
    co2_per_capita_t: 4.362,
    wellbeing_efficiency: 1.6715
  },
  {
    country: 'Switzerland',
    year: 2017,
    iso3: 'CHE',
    happiness_score: 7.494,
    gdp_per_capita_usd: 80342.85,
    co2_per_capita_t: 4.517,
    wellbeing_efficiency: 1.659
  },
  {
    country: 'Sweden',
    year: 2015,
    iso3: 'SWE',
    happiness_score: 7.364,
    gdp_per_capita_usd: 50832.55,
    co2_per_capita_t: 4.441,
    wellbeing_efficiency: 1.6582
  },
  {
    country: 'Switzerland',
    year: 2015,
    iso3: 'CHE',
    happiness_score: 7.587,
    gdp_per_capita_usd: 82081.6,
    co2_per_capita_t: 4.677,
    wellbeing_efficiency: 1.6223
  },
  {
    country: 'Switzerland',
    year: 2016,
    iso3: 'CHE',
    happiness_score: 7.509,
    gdp_per_capita_usd: 80037.5,
    co2_per_capita_t: 4.68,
    wellbeing_efficiency: 1.6045
  },
  {
    country: 'Latvia',
    year: 2017,
    iso3: 'LVA',
    happiness_score: 5.85,
    gdp_per_capita_usd: 15684.56,
    co2_per_capita_t: 3.691,
    wellbeing_efficiency: 1.585
  },
  {
    country: 'Chile',
    year: 2017,
    iso3: 'CHL',
    happiness_score: 6.652,
    gdp_per_capita_usd: 15346.45,
    co2_per_capita_t: 4.577,
    wellbeing_efficiency: 1.4533
  }
]
```

---

## [05] Kategorie 1: Propojovani Dat A Vazeb Mezi Datasety / Dotaz 5

**Stav:** OK

```text
[
  {
    peer_count: 221,
    gdp_bucket: 0,
    country: 'Guatemala',
    iso3: 'GTM',
    year: 2017,
    gdp_per_capita_usd: 4470.99,
    happiness_score: 6.454,
    co2_per_capita_t: 1.045,
    peer_avg_happiness: 4.574,
    peer_avg_co2: 1.315,
    happiness_gap_vs_peers: 1.88,
    co2_gap_vs_peers: -0.271
  },
  {
    peer_count: 221,
    gdp_bucket: 0,
    country: 'Algeria',
    iso3: 'DZA',
    year: 2016,
    gdp_per_capita_usd: 3943.5,
    happiness_score: 6.355,
    co2_per_capita_t: 3.935,
    peer_avg_happiness: 4.574,
    peer_avg_co2: 1.315,
    happiness_gap_vs_peers: 1.781,
    co2_gap_vs_peers: 2.62
  },
  {
    peer_count: 221,
    gdp_bucket: 0,
    country: 'Guatemala',
    iso3: 'GTM',
    year: 2016,
    gdp_per_capita_usd: 4140.74,
    happiness_score: 6.324,
    co2_per_capita_t: 1.039,
    peer_avg_happiness: 4.574,
    peer_avg_co2: 1.315,
    happiness_gap_vs_peers: 1.75,
    co2_gap_vs_peers: -0.276
  },
  {
    peer_count: 77,
    gdp_bucket: 5000,
    country: 'Mexico',
    iso3: 'MEX',
    year: 2015,
    gdp_per_capita_usd: 9298.24,
    happiness_score: 7.187,
    co2_per_capita_t: 3.991,
    peer_avg_happiness: 5.465,
    peer_avg_co2: 5.087,
    happiness_gap_vs_peers: 1.722,
    co2_gap_vs_peers: -1.096
  },
  {
    peer_count: 221,
    gdp_bucket: 0,
    country: 'El Salvador',
    iso3: 'SLV',
    year: 2015,
    gdp_per_capita_usd: 3669.88,
    happiness_score: 6.13,
    co2_per_capita_t: 1.07,
    peer_avg_happiness: 4.574,
    peer_avg_co2: 1.315,
    happiness_gap_vs_peers: 1.556,
    co2_gap_vs_peers: -0.245
  },
  {
    peer_count: 221,
    gdp_bucket: 0,
    country: 'Guatemala',
    iso3: 'GTM',
    year: 2015,
    gdp_per_capita_usd: 3923.57,
    happiness_score: 6.123,
    co2_per_capita_t: 0.997,
    peer_avg_happiness: 4.574,
    peer_avg_co2: 1.315,
    happiness_gap_vs_peers: 1.549,
    co2_gap_vs_peers: -0.318
  },
  {
    peer_count: 77,
    gdp_bucket: 5000,
    country: 'Brazil',
    iso3: 'BRA',
    year: 2015,
    gdp_per_capita_usd: 8750.22,
    happiness_score: 6.983,
    co2_per_capita_t: 2.58,
    peer_avg_happiness: 5.465,
    peer_avg_co2: 5.087,
    happiness_gap_vs_peers: 1.518,
    co2_gap_vs_peers: -2.507
  },
  {
    peer_count: 221,
    gdp_bucket: 0,
    country: 'Nicaragua',
    iso3: 'NIC',
    year: 2017,
    gdp_per_capita_usd: 2221.81,
    happiness_score: 6.071,
    co2_per_capita_t: 0.843,
    peer_avg_happiness: 4.574,
    peer_avg_co2: 1.315,
    happiness_gap_vs_peers: 1.497,
    co2_gap_vs_peers: -0.473
  },
  {
    peer_count: 221,
    gdp_bucket: 0,
    country: 'El Salvador',
    iso3: 'SLV',
    year: 2016,
    gdp_per_capita_usd: 3768.84,
    happiness_score: 6.068,
    co2_per_capita_t: 1.055,
    peer_avg_happiness: 4.574,
    peer_avg_co2: 1.315,
    happiness_gap_vs_peers: 1.494,
    co2_gap_vs_peers: -0.26
  },
  {
    peer_count: 77,
    gdp_bucket: 5000,
    country: 'Brazil',
    iso3: 'BRA',
    year: 2016,
    gdp_per_capita_usd: 8650.38,
    happiness_score: 6.952,
    co2_per_capita_t: 2.382,
    peer_avg_happiness: 5.465,
    peer_avg_co2: 5.087,
    happiness_gap_vs_peers: 1.487,
    co2_gap_vs_peers: -2.705
  },
  {
    peer_count: 221,
    gdp_bucket: 0,
    country: 'El Salvador',
    iso3: 'SLV',
    year: 2017,
    gdp_per_capita_usd: 3889.31,
    happiness_score: 6.003,
    co2_per_capita_t: 0.953,
    peer_avg_happiness: 4.574,
    peer_avg_co2: 1.315,
    happiness_gap_vs_peers: 1.429,
    co2_gap_vs_peers: -0.363
  },
  {
    peer_count: 221,
    gdp_bucket: 0,
    country: 'Uzbekistan',
    iso3: 'UZB',
    year: 2015,
    gdp_per_capita_usd: 2137.58,
    happiness_score: 6.003,
    co2_per_capita_t: 3.35,
    peer_avg_happiness: 4.574,
    peer_avg_co2: 1.315,
    happiness_gap_vs_peers: 1.429,
    co2_gap_vs_peers: 2.035
  },
  {
    peer_count: 221,
    gdp_bucket: 0,
    country: 'Nicaragua',
    iso3: 'NIC',
    year: 2016,
    gdp_per_capita_usd: 2143.93,
    happiness_score: 5.992,
    co2_per_capita_t: 0.846,
    peer_avg_happiness: 4.574,
    peer_avg_co2: 1.315,
    happiness_gap_vs_peers: 1.418,
    co2_gap_vs_peers: -0.469
  },
  {
    peer_count: 221,
    gdp_bucket: 0,
    country: 'Uzbekistan',
    iso3: 'UZB',
    year: 2016,
    gdp_per_capita_usd: 2117.74,
    happiness_score: 5.987,
    co2_per_capita_t: 3.502,
    peer_avg_happiness: 4.574,
    peer_avg_co2: 1.315,
    happiness_gap_vs_peers: 1.413,
    co2_gap_vs_peers: 2.186
  },
  {
    peer_count: 221,
    gdp_bucket: 0,
    country: 'Uzbekistan',
    iso3: 'UZB',
    year: 2017,
    gdp_per_capita_usd: 1533.85,
    happiness_score: 5.971,
    co2_per_capita_t: 3.41,
    peer_avg_happiness: 4.574,
    peer_avg_co2: 1.315,
    happiness_gap_vs_peers: 1.397,
    co2_gap_vs_peers: 2.094
  },
  {
    peer_count: 221,
    gdp_bucket: 0,
    country: 'Belize',
    iso3: 'BLZ',
    year: 2017,
    gdp_per_capita_usd: 4971.2,
    happiness_score: 5.956,
    co2_per_capita_t: 1.643,
    peer_avg_happiness: 4.574,
    peer_avg_co2: 1.315,
    happiness_gap_vs_peers: 1.382,
    co2_gap_vs_peers: 0.327
  },
  {
    peer_count: 221,
    gdp_bucket: 0,
    country: 'Belize',
    iso3: 'BLZ',
    year: 2016,
    gdp_per_capita_usd: 4923.36,
    happiness_score: 5.956,
    co2_per_capita_t: 1.696,
    peer_avg_happiness: 4.574,
    peer_avg_co2: 1.315,
    happiness_gap_vs_peers: 1.382,
    co2_gap_vs_peers: 0.38
  },
  {
    peer_count: 221,
    gdp_bucket: 0,
    country: 'Moldova',
    iso3: 'MDA',
    year: 2016,
    gdp_per_capita_usd: 1913.24,
    happiness_score: 5.897,
    co2_per_capita_t: 1.52,
    peer_avg_happiness: 4.574,
    peer_avg_co2: 1.315,
    happiness_gap_vs_peers: 1.323,
    co2_gap_vs_peers: 0.205
  },
  {
    peer_count: 221,
    gdp_bucket: 0,
    country: 'Bolivia',
    iso3: 'BOL',
    year: 2015,
    gdp_per_capita_usd: 3077.03,
    happiness_score: 5.89,
    co2_per_capita_t: 1.915,
    peer_avg_happiness: 4.574,
    peer_avg_co2: 1.315,
    happiness_gap_vs_peers: 1.316,
    co2_gap_vs_peers: 0.6
  },
  {
    peer_count: 221,
    gdp_bucket: 0,
    country: 'Moldova',
    iso3: 'MDA',
    year: 2015,
    gdp_per_capita_usd: 1832.5,
    happiness_score: 5.889,
    co2_per_capita_t: 1.459,
    peer_avg_happiness: 4.574,
    peer_avg_co2: 1.315,
    happiness_gap_vs_peers: 1.315,
    co2_gap_vs_peers: 0.144
  }
]
```

---

## [06] Kategorie 1: Propojovani Dat A Vazeb Mezi Datasety / Dotaz 6

**Stav:** OK

```text
[
  {
    years_observed: 3,
    first_year: 2015,
    last_year: 2017,
    iso3: 'CMR',
    country: 'Cameroon',
    happiness_delta: 0.443,
    gdp_growth_pct: 7.23,
    co2_change_pct: -8.12
  },
  {
    years_observed: 3,
    first_year: 2015,
    last_year: 2017,
    iso3: 'HND',
    country: 'Honduras',
    happiness_delta: 0.393,
    gdp_growth_pct: 5.93,
    co2_change_pct: -4.54
  },
  {
    years_observed: 3,
    first_year: 2015,
    last_year: 2017,
    iso3: 'DOM',
    country: 'Dominican Republic',
    happiness_delta: 0.345,
    gdp_growth_pct: 7.92,
    co2_change_pct: -0.09
  },
  {
    years_observed: 3,
    first_year: 2015,
    last_year: 2017,
    iso3: 'TKM',
    country: 'Turkmenistan',
    happiness_delta: 0.274,
    gdp_growth_pct: 2.39,
    co2_change_pct: -3.82
  },
  {
    years_observed: 3,
    first_year: 2015,
    last_year: 2017,
    iso3: 'NIC',
    country: 'Nicaragua',
    happiness_delta: 0.243,
    gdp_growth_pct: 7.15,
    co2_change_pct: -2.26
  },
  {
    years_observed: 3,
    first_year: 2015,
    last_year: 2017,
    iso3: 'MLT',
    country: 'Malta',
    happiness_delta: 0.225,
    gdp_growth_pct: 12.79,
    co2_change_pct: -12.47
  },
  {
    years_observed: 3,
    first_year: 2015,
    last_year: 2017,
    iso3: 'DEU',
    country: 'Germany',
    happiness_delta: 0.201,
    gdp_growth_pct: 7.9,
    co2_change_pct: -1.91
  },
  {
    years_observed: 3,
    first_year: 2015,
    last_year: 2017,
    iso3: 'ZAF',
    country: 'South Africa',
    happiness_delta: 0.187,
    gdp_growth_pct: 7.11,
    co2_change_pct: -2.86
  },
  {
    years_observed: 3,
    first_year: 2015,
    last_year: 2017,
    iso3: 'NER',
    country: 'Niger',
    happiness_delta: 0.183,
    gdp_growth_pct: 4.22,
    co2_change_pct: -5.55
  },
  {
    years_observed: 3,
    first_year: 2015,
    last_year: 2017,
    iso3: 'JOR',
    country: 'Jordan',
    happiness_delta: 0.144,
    gdp_growth_pct: 0.82,
    co2_change_pct: -7.53
  },
  {
    years_observed: 3,
    first_year: 2015,
    last_year: 2017,
    iso3: 'KEN',
    country: 'Kenya',
    happiness_delta: 0.134,
    gdp_growth_pct: 17.7,
    co2_change_pct: -0.04
  },
  {
    years_observed: 3,
    first_year: 2015,
    last_year: 2017,
    iso3: 'BHR',
    country: 'Bahrain',
    happiness_delta: 0.127,
    gdp_growth_pct: 4.63,
    co2_change_pct: -5.42
  },
  {
    years_observed: 3,
    first_year: 2015,
    last_year: 2017,
    iso3: 'MNE',
    country: 'Montenegro',
    happiness_delta: 0.045,
    gdp_growth_pct: 19.49,
    co2_change_pct: -5.83
  },
  {
    years_observed: 3,
    first_year: 2015,
    last_year: 2017,
    iso3: 'IRL',
    country: 'Ireland',
    happiness_delta: 0.037,
    gdp_growth_pct: 11.27,
    co2_change_pct: -1.31
  },
  {
    years_observed: 3,
    first_year: 2015,
    last_year: 2017,
    iso3: 'ECU',
    country: 'Ecuador',
    happiness_delta: 0.033,
    gdp_growth_pct: 2.01,
    co2_change_pct: -5.82
  },
  {
    years_observed: 3,
    first_year: 2015,
    last_year: 2017,
    iso3: 'NZL',
    country: 'New Zealand',
    happiness_delta: 0.028,
    gdp_growth_pct: 10.18,
    co2_change_pct: -3.62
  },
  {
    years_observed: 3,
    first_year: 2015,
    last_year: 2017,
    iso3: 'ARG',
    country: 'Argentina',
    happiness_delta: 0.025,
    gdp_growth_pct: 5.11,
    co2_change_pct: -4.29
  },
  {
    years_observed: 3,
    first_year: 2015,
    last_year: 2017,
    iso3: 'ITA',
    country: 'Italy',
    happiness_delta: 0.016,
    gdp_growth_pct: 6.43,
    co2_change_pct: -1.96
  },
  {
    years_observed: 3,
    first_year: 2015,
    last_year: 2017,
    iso3: 'NOR',
    country: 'Norway',
    happiness_delta: 0.015,
    gdp_growth_pct: 1.59,
    co2_change_pct: -4.56
  }
]
```

---

## [07] Kategorie 2: Agregacni A Analyticke Dotazy / Dotaz 1

**Stav:** OK

```text
[
  {
    country: 'Algeria',
    year: 2016,
    iso3: 'DZA',
    happiness_score: 6.355,
    prev_happiness: 5.605,
    happiness_delta: 0.75,
    rolling_happiness_3y: 5.98,
    rolling_gdp_3y: 4053.17,
    momentum_score: 135.205
  },
  {
    country: 'Latvia',
    year: 2016,
    iso3: 'LVA',
    happiness_score: 5.56,
    prev_happiness: 5.098,
    happiness_delta: 0.462,
    rolling_happiness_3y: 5.329,
    rolling_gdp_3y: 13886.69,
    momentum_score: 100.879
  },
  {
    country: 'Germany',
    year: 2016,
    iso3: 'DEU',
    happiness_score: 6.994,
    prev_happiness: 6.75,
    happiness_delta: 0.244,
    rolling_happiness_3y: 6.872,
    rolling_gdp_3y: 41919.06,
    momentum_score: 97.312
  },
  {
    country: 'Romania',
    year: 2016,
    iso3: 'ROU',
    happiness_score: 5.528,
    prev_happiness: 5.124,
    happiness_delta: 0.404,
    rolling_happiness_3y: 5.326,
    rolling_gdp_3y: 9272.3,
    momentum_score: 94.587
  },
  {
    country: 'Bulgaria',
    year: 2017,
    iso3: 'BGR',
    happiness_score: 4.714,
    prev_happiness: 4.217,
    happiness_delta: 0.497,
    rolling_happiness_3y: 4.383,
    rolling_gdp_3y: 7563.75,
    momentum_score: 94.286
  },
  {
    country: 'Somalia',
    year: 2016,
    iso3: 'SOM',
    happiness_score: 5.44,
    prev_happiness: 5.057,
    happiness_delta: 0.383,
    rolling_happiness_3y: 5.185,
    rolling_gdp_3y: 474.44,
    momentum_score: 90.194
  },
  {
    country: 'Bahrain',
    year: 2016,
    iso3: 'BHR',
    happiness_score: 6.218,
    prev_happiness: 5.96,
    happiness_delta: 0.258,
    rolling_happiness_3y: 6.089,
    rolling_gdp_3y: 22658.92,
    momentum_score: 88.956
  },
  {
    country: 'Norway',
    year: 2017,
    iso3: 'NOR',
    happiness_score: 7.537,
    prev_happiness: 7.498,
    happiness_delta: 0.039,
    rolling_happiness_3y: 7.519,
    rolling_gdp_3y: 73722.45,
    momentum_score: 86.462
  },
  {
    country: 'North Cyprus',
    year: 2017,
    iso3: 'CYP',
    happiness_score: 5.81,
    prev_happiness: 5.546,
    happiness_delta: 0.264,
    rolling_happiness_3y: 5.709,
    rolling_gdp_3y: 24565.69,
    momentum_score: 85.947
  },
  {
    country: 'Romania',
    year: 2017,
    iso3: 'ROU',
    happiness_score: 5.825,
    prev_happiness: 5.528,
    happiness_delta: 0.297,
    rolling_happiness_3y: 5.492,
    rolling_gdp_3y: 9787.95,
    momentum_score: 85.602
  },
  {
    country: 'Hungary',
    year: 2016,
    iso3: 'HUN',
    happiness_score: 5.145,
    prev_happiness: 4.8,
    happiness_delta: 0.345,
    rolling_happiness_3y: 4.973,
    rolling_gdp_3y: 12671.63,
    momentum_score: 85.492
  },
  {
    country: 'Latvia',
    year: 2017,
    iso3: 'LVA',
    happiness_score: 5.85,
    prev_happiness: 5.56,
    happiness_delta: 0.29,
    rolling_happiness_3y: 5.503,
    rolling_gdp_3y: 14485.98,
    momentum_score: 85.475
  },
  {
    country: 'Malta',
    year: 2016,
    iso3: 'MLT',
    happiness_score: 6.488,
    prev_happiness: 6.302,
    happiness_delta: 0.186,
    rolling_happiness_3y: 6.395,
    rolling_gdp_3y: 24237.11,
    momentum_score: 84.974
  },
  {
    country: 'Finland',
    year: 2017,
    iso3: 'FIN',
    happiness_score: 7.469,
    prev_happiness: 7.413,
    happiness_delta: 0.056,
    rolling_happiness_3y: 7.429,
    rolling_gdp_3y: 43930.91,
    momentum_score: 84.286
  },
  {
    country: 'South Africa',
    year: 2017,
    iso3: 'ZAF',
    happiness_score: 4.829,
    prev_happiness: 4.459,
    happiness_delta: 0.37,
    rolling_happiness_3y: 4.643,
    rolling_gdp_3y: 5724.6,
    momentum_score: 84.006
  }
]
```

---

## [08] Kategorie 2: Agregacni A Analyticke Dotazy / Dotaz 2

**Stav:** OK

```text
[
  {
    years_observed: 5,
    iso3: 'NZL',
    country: 'New Zealand',
    avg_happiness: 7.313,
    std_happiness: 0.018,
    happiness_range: 0.048,
    coeff_variation: 0.0025,
    avg_co2: 7.5,
    stability_index: 401.353
  },
  {
    years_observed: 5,
    iso3: 'BEL',
    country: 'Belgium',
    avg_happiness: 6.921,
    std_happiness: 0.018,
    happiness_range: 0.046,
    coeff_variation: 0.0026,
    avg_co2: 8.771,
    stability_index: 390.099
  },
  {
    years_observed: 5,
    iso3: 'SAU',
    country: 'Saudi Arabia',
    avg_happiness: 6.376,
    std_happiness: 0.024,
    happiness_range: 0.067,
    coeff_variation: 0.0037,
    avg_co2: 18.999,
    stability_index: 266.827
  },
  {
    years_observed: 5,
    iso3: 'ISL',
    country: 'Iceland',
    avg_happiness: 7.511,
    std_happiness: 0.028,
    happiness_range: 0.067,
    coeff_variation: 0.0038,
    avg_co2: 10.347,
    stability_index: 265.803
  },
  {
    years_observed: 4,
    iso3: 'HKG',
    country: 'Hong Kong',
    avg_happiness: 5.448,
    std_happiness: 0.022,
    happiness_range: 0.044,
    coeff_variation: 0.004,
    avg_co2: 5.711,
    stability_index: 250.059
  },
  {
    years_observed: 5,
    iso3: 'ECU',
    country: 'Ecuador',
    avg_happiness: 5.992,
    std_happiness: 0.025,
    happiness_range: 0.055,
    coeff_variation: 0.0041,
    avg_co2: 2.392,
    stability_index: 241.719
  },
  {
    years_observed: 5,
    iso3: 'AUS',
    country: 'Australia',
    avg_happiness: 7.276,
    std_happiness: 0.031,
    happiness_range: 0.085,
    coeff_variation: 0.0042,
    avg_co2: 16.76,
    stability_index: 235.551
  },
  {
    years_observed: 5,
    iso3: 'DNK',
    country: 'Denmark',
    avg_happiness: 7.546,
    std_happiness: 0.033,
    happiness_range: 0.078,
    coeff_variation: 0.0044,
    avg_co2: 6.024,
    stability_index: 229.246
  },
  {
    years_observed: 5,
    iso3: 'SWE',
    country: 'Sweden',
    avg_happiness: 7.319,
    std_happiness: 0.034,
    happiness_range: 0.08,
    coeff_variation: 0.0047,
    avg_co2: 4.236,
    stability_index: 215.019
  },
  {
    years_observed: 5,
    iso3: 'NOR',
    country: 'Norway',
    avg_happiness: 7.541,
    std_happiness: 0.036,
    happiness_range: 0.096,
    coeff_variation: 0.0048,
    avg_co2: 8.415,
    stability_index: 209.069
  },
  {
    years_observed: 5,
    iso3: 'ESP',
    country: 'Spain',
    avg_happiness: 6.351,
    std_happiness: 0.035,
    happiness_range: 0.093,
    coeff_variation: 0.0056,
    avg_co2: 5.7,
    stability_index: 180.056
  },
  {
    years_observed: 5,
    iso3: 'CHE',
    country: 'Switzerland',
    avg_happiness: 7.511,
    std_happiness: 0.044,
    happiness_range: 0.107,
    coeff_variation: 0.0058,
    avg_co2: 4.498,
    stability_index: 172.264
  },
  {
    years_observed: 5,
    iso3: 'IRL',
    country: 'Ireland',
    avg_happiness: 6.964,
    std_happiness: 0.043,
    happiness_range: 0.114,
    coeff_variation: 0.0062,
    avg_co2: 8.148,
    stability_index: 161.797
  },
  {
    years_observed: 5,
    iso3: 'JPN',
    country: 'Japan',
    avg_happiness: 5.926,
    std_happiness: 0.037,
    happiness_range: 0.101,
    coeff_variation: 0.0063,
    avg_co2: 9.265,
    stability_index: 159.766
  },
  {
    years_observed: 5,
    iso3: 'PSE',
    country: 'Palestinian Territories',
    avg_happiness: 4.737,
    std_happiness: 0.031,
    happiness_range: 0.079,
    coeff_variation: 0.0066,
    avg_co2: 0.67,
    stability_index: 151.051
  }
]
```

---

## [09] Kategorie 2: Agregacni A Analyticke Dotazy / Dotaz 3

**Stav:** OK

```text
[
  {
    iso3: 'CAF',
    country: 'Central African Republic',
    y2015_happiness: 3.678,
    y2017_happiness: 2.693,
    happiness_delta: -0.985,
    y2015_gdp: 348.38,
    y2017_gdp: 418.41,
    gdp_growth_pct: 20.1,
    divergence_score: 118.6
  },
  {
    iso3: 'LSO',
    country: 'Lesotho',
    y2015_happiness: 4.898,
    y2017_happiness: 3.808,
    happiness_delta: -1.09,
    y2015_gdp: 1154.36,
    y2017_gdp: 1154.44,
    gdp_growth_pct: 0.01,
    divergence_score: 109.01
  },
  {
    iso3: 'LBR',
    country: 'Liberia',
    y2015_happiness: 4.571,
    y2017_happiness: 3.533,
    happiness_delta: -1.038,
    y2015_gdp: 706.06,
    y2017_gdp: 694.32,
    gdp_growth_pct: -1.66,
    divergence_score: 102.14
  },
  {
    iso3: 'HTI',
    country: 'Haiti',
    y2015_happiness: 4.518,
    y2017_happiness: 3.603,
    happiness_delta: -0.915,
    y2015_gdp: 814.55,
    y2017_gdp: 765.68,
    gdp_growth_pct: -6,
    divergence_score: 85.5
  },
  {
    iso3: 'UKR',
    country: 'Ukraine',
    y2015_happiness: 4.681,
    y2017_happiness: 4.096,
    happiness_delta: -0.585,
    y2015_gdp: 2124.66,
    y2017_gdp: 2639.82,
    gdp_growth_pct: 24.25,
    divergence_score: 82.75
  },
  {
    iso3: 'ZWE',
    country: 'Zimbabwe',
    y2015_happiness: 4.61,
    y2017_happiness: 3.875,
    happiness_delta: -0.735,
    y2015_gdp: 1265.29,
    y2017_gdp: 1333.4,
    gdp_growth_pct: 5.38,
    divergence_score: 78.88
  },
  {
    iso3: 'ZMB',
    country: 'Zambia',
    y2015_happiness: 5.129,
    y2017_happiness: 4.514,
    happiness_delta: -0.615,
    y2015_gdp: 1313.89,
    y2017_gdp: 1513.28,
    gdp_growth_pct: 15.18,
    divergence_score: 76.68
  },
  {
    iso3: 'BWA',
    country: 'Botswana',
    y2015_happiness: 4.332,
    y2017_happiness: 3.766,
    happiness_delta: -0.566,
    y2015_gdp: 6521.15,
    y2017_gdp: 7595.61,
    gdp_growth_pct: 16.48,
    divergence_score: 73.08
  },
  {
    iso3: 'GHA',
    country: 'Ghana',
    y2015_happiness: 4.633,
    y2017_happiness: 4.12,
    happiness_delta: -0.513,
    y2015_gdp: 1783.06,
    y2017_gdp: 2046.11,
    gdp_growth_pct: 14.75,
    divergence_score: 66.05
  },
  {
    iso3: 'HRV',
    country: 'Croatia',
    y2015_happiness: 5.759,
    y2017_happiness: 5.293,
    happiness_delta: -0.466,
    y2015_gdp: 11773.26,
    y2017_gdp: 13386.51,
    gdp_growth_pct: 13.7,
    divergence_score: 60.3
  },
  {
    iso3: 'LBY',
    country: 'Libya',
    y2015_happiness: 5.754,
    y2017_happiness: 5.525,
    happiness_delta: -0.229,
    y2015_gdp: 4465.49,
    y2017_gdp: 5978.04,
    gdp_growth_pct: 33.87,
    divergence_score: 56.77
  },
  {
    iso3: 'MEX',
    country: 'Mexico',
    y2015_happiness: 7.187,
    y2017_happiness: 6.578,
    happiness_delta: -0.609,
    y2015_gdp: 9298.24,
    y2017_gdp: 8910.33,
    gdp_growth_pct: -4.17,
    divergence_score: 56.73
  },
  {
    iso3: 'SDN',
    country: 'Sudan',
    y2015_happiness: 4.55,
    y2017_happiness: 4.139,
    happiness_delta: -0.411,
    y2015_gdp: 2513.88,
    y2017_gdp: 2898.55,
    gdp_growth_pct: 15.3,
    divergence_score: 56.4
  },
  {
    iso3: 'TZA',
    country: 'Tanzania',
    y2015_happiness: 3.781,
    y2017_happiness: 3.349,
    happiness_delta: -0.432,
    y2015_gdp: 905.76,
    y2017_gdp: 958.45,
    gdp_growth_pct: 5.82,
    divergence_score: 49.02
  },
  {
    iso3: 'IND',
    country: 'India',
    y2015_happiness: 4.565,
    y2017_happiness: 4.315,
    happiness_delta: -0.25,
    y2015_gdp: 1606.95,
    y2017_gdp: 1979.36,
    gdp_growth_pct: 23.18,
    divergence_score: 48.18
  }
]
```

---

## [10] Kategorie 2: Agregacni A Analyticke Dotazy / Dotaz 4

**Stav:** OK

```text
[
  {
    years_observed: 3,
    first_year: 2015,
    last_year: 2017,
    iso3: 'MLT',
    country: 'Malta',
    gdp_growth_pct: 12.79,
    happiness_delta: 0.225,
    co2_change_pct: -12.47,
    green_growth_score: 29.75
  },
  {
    years_observed: 3,
    first_year: 2015,
    last_year: 2017,
    iso3: 'MNE',
    country: 'Montenegro',
    gdp_growth_pct: 19.49,
    happiness_delta: 0.045,
    co2_change_pct: -5.83,
    green_growth_score: 26.22
  },
  {
    years_observed: 3,
    first_year: 2015,
    last_year: 2017,
    iso3: 'CMR',
    country: 'Cameroon',
    gdp_growth_pct: 7.23,
    happiness_delta: 0.443,
    co2_change_pct: -8.12,
    green_growth_score: 24.22
  },
  {
    years_observed: 3,
    first_year: 2015,
    last_year: 2017,
    iso3: 'KEN',
    country: 'Kenya',
    gdp_growth_pct: 17.7,
    happiness_delta: 0.134,
    co2_change_pct: -0.04,
    green_growth_score: 20.41
  },
  {
    years_observed: 3,
    first_year: 2015,
    last_year: 2017,
    iso3: 'HND',
    country: 'Honduras',
    gdp_growth_pct: 5.93,
    happiness_delta: 0.393,
    co2_change_pct: -4.54,
    green_growth_score: 18.33
  },
  {
    years_observed: 3,
    first_year: 2015,
    last_year: 2017,
    iso3: 'DOM',
    country: 'Dominican Republic',
    gdp_growth_pct: 7.92,
    happiness_delta: 0.345,
    co2_change_pct: -0.09,
    green_growth_score: 14.91
  },
  {
    years_observed: 3,
    first_year: 2015,
    last_year: 2017,
    iso3: 'NZL',
    country: 'New Zealand',
    gdp_growth_pct: 10.18,
    happiness_delta: 0.028,
    co2_change_pct: -3.62,
    green_growth_score: 14.36
  },
  {
    years_observed: 3,
    first_year: 2015,
    last_year: 2017,
    iso3: 'NIC',
    country: 'Nicaragua',
    gdp_growth_pct: 7.15,
    happiness_delta: 0.243,
    co2_change_pct: -2.26,
    green_growth_score: 14.28
  },
  {
    years_observed: 3,
    first_year: 2015,
    last_year: 2017,
    iso3: 'DEU',
    country: 'Germany',
    gdp_growth_pct: 7.9,
    happiness_delta: 0.201,
    co2_change_pct: -1.91,
    green_growth_score: 13.83
  },
  {
    years_observed: 3,
    first_year: 2015,
    last_year: 2017,
    iso3: 'ZAF',
    country: 'South Africa',
    gdp_growth_pct: 7.11,
    happiness_delta: 0.187,
    co2_change_pct: -2.86,
    green_growth_score: 13.71
  },
  {
    years_observed: 3,
    first_year: 2015,
    last_year: 2017,
    iso3: 'NER',
    country: 'Niger',
    gdp_growth_pct: 4.22,
    happiness_delta: 0.183,
    co2_change_pct: -5.55,
    green_growth_score: 13.43
  },
  {
    years_observed: 3,
    first_year: 2015,
    last_year: 2017,
    iso3: 'IRL',
    country: 'Ireland',
    gdp_growth_pct: 11.27,
    happiness_delta: 0.037,
    co2_change_pct: -1.31,
    green_growth_score: 13.32
  },
  {
    years_observed: 3,
    first_year: 2015,
    last_year: 2017,
    iso3: 'BHR',
    country: 'Bahrain',
    gdp_growth_pct: 4.63,
    happiness_delta: 0.127,
    co2_change_pct: -5.42,
    green_growth_score: 12.59
  },
  {
    years_observed: 3,
    first_year: 2015,
    last_year: 2017,
    iso3: 'TKM',
    country: 'Turkmenistan',
    gdp_growth_pct: 2.39,
    happiness_delta: 0.274,
    co2_change_pct: -3.82,
    green_growth_score: 11.7
  },
  {
    years_observed: 3,
    first_year: 2015,
    last_year: 2017,
    iso3: 'JOR',
    country: 'Jordan',
    gdp_growth_pct: 0.82,
    happiness_delta: 0.144,
    co2_change_pct: -7.53,
    green_growth_score: 11.23
  }
]
```

---

## [11] Kategorie 2: Agregacni A Analyticke Dotazy / Dotaz 5

**Stav:** OK

```text
[
  {
    peer_count: 221,
    gdp_bucket: 0,
    country: 'Guatemala',
    iso3: 'GTM',
    year: 2017,
    gdp_per_capita_usd: 4470.99,
    happiness_score: 6.454,
    co2_per_capita_t: 1.045,
    peer_avg_happiness: 4.574,
    peer_avg_co2: 1.315,
    happiness_gap_vs_peers: 1.88,
    co2_gap_vs_peers: -0.271
  },
  {
    peer_count: 221,
    gdp_bucket: 0,
    country: 'Algeria',
    iso3: 'DZA',
    year: 2016,
    gdp_per_capita_usd: 3943.5,
    happiness_score: 6.355,
    co2_per_capita_t: 3.935,
    peer_avg_happiness: 4.574,
    peer_avg_co2: 1.315,
    happiness_gap_vs_peers: 1.781,
    co2_gap_vs_peers: 2.62
  },
  {
    peer_count: 221,
    gdp_bucket: 0,
    country: 'Guatemala',
    iso3: 'GTM',
    year: 2016,
    gdp_per_capita_usd: 4140.74,
    happiness_score: 6.324,
    co2_per_capita_t: 1.039,
    peer_avg_happiness: 4.574,
    peer_avg_co2: 1.315,
    happiness_gap_vs_peers: 1.75,
    co2_gap_vs_peers: -0.276
  },
  {
    peer_count: 77,
    gdp_bucket: 5000,
    country: 'Mexico',
    iso3: 'MEX',
    year: 2015,
    gdp_per_capita_usd: 9298.24,
    happiness_score: 7.187,
    co2_per_capita_t: 3.991,
    peer_avg_happiness: 5.465,
    peer_avg_co2: 5.087,
    happiness_gap_vs_peers: 1.722,
    co2_gap_vs_peers: -1.096
  },
  {
    peer_count: 221,
    gdp_bucket: 0,
    country: 'El Salvador',
    iso3: 'SLV',
    year: 2015,
    gdp_per_capita_usd: 3669.88,
    happiness_score: 6.13,
    co2_per_capita_t: 1.07,
    peer_avg_happiness: 4.574,
    peer_avg_co2: 1.315,
    happiness_gap_vs_peers: 1.556,
    co2_gap_vs_peers: -0.245
  },
  {
    peer_count: 221,
    gdp_bucket: 0,
    country: 'Guatemala',
    iso3: 'GTM',
    year: 2015,
    gdp_per_capita_usd: 3923.57,
    happiness_score: 6.123,
    co2_per_capita_t: 0.997,
    peer_avg_happiness: 4.574,
    peer_avg_co2: 1.315,
    happiness_gap_vs_peers: 1.549,
    co2_gap_vs_peers: -0.318
  },
  {
    peer_count: 77,
    gdp_bucket: 5000,
    country: 'Brazil',
    iso3: 'BRA',
    year: 2015,
    gdp_per_capita_usd: 8750.22,
    happiness_score: 6.983,
    co2_per_capita_t: 2.58,
    peer_avg_happiness: 5.465,
    peer_avg_co2: 5.087,
    happiness_gap_vs_peers: 1.518,
    co2_gap_vs_peers: -2.507
  },
  {
    peer_count: 221,
    gdp_bucket: 0,
    country: 'Nicaragua',
    iso3: 'NIC',
    year: 2017,
    gdp_per_capita_usd: 2221.81,
    happiness_score: 6.071,
    co2_per_capita_t: 0.843,
    peer_avg_happiness: 4.574,
    peer_avg_co2: 1.315,
    happiness_gap_vs_peers: 1.497,
    co2_gap_vs_peers: -0.473
  },
  {
    peer_count: 221,
    gdp_bucket: 0,
    country: 'El Salvador',
    iso3: 'SLV',
    year: 2016,
    gdp_per_capita_usd: 3768.84,
    happiness_score: 6.068,
    co2_per_capita_t: 1.055,
    peer_avg_happiness: 4.574,
    peer_avg_co2: 1.315,
    happiness_gap_vs_peers: 1.494,
    co2_gap_vs_peers: -0.26
  },
  {
    peer_count: 77,
    gdp_bucket: 5000,
    country: 'Brazil',
    iso3: 'BRA',
    year: 2016,
    gdp_per_capita_usd: 8650.38,
    happiness_score: 6.952,
    co2_per_capita_t: 2.382,
    peer_avg_happiness: 5.465,
    peer_avg_co2: 5.087,
    happiness_gap_vs_peers: 1.487,
    co2_gap_vs_peers: -2.705
  },
  {
    peer_count: 221,
    gdp_bucket: 0,
    country: 'El Salvador',
    iso3: 'SLV',
    year: 2017,
    gdp_per_capita_usd: 3889.31,
    happiness_score: 6.003,
    co2_per_capita_t: 0.953,
    peer_avg_happiness: 4.574,
    peer_avg_co2: 1.315,
    happiness_gap_vs_peers: 1.429,
    co2_gap_vs_peers: -0.363
  },
  {
    peer_count: 221,
    gdp_bucket: 0,
    country: 'Uzbekistan',
    iso3: 'UZB',
    year: 2015,
    gdp_per_capita_usd: 2137.58,
    happiness_score: 6.003,
    co2_per_capita_t: 3.35,
    peer_avg_happiness: 4.574,
    peer_avg_co2: 1.315,
    happiness_gap_vs_peers: 1.429,
    co2_gap_vs_peers: 2.035
  },
  {
    peer_count: 221,
    gdp_bucket: 0,
    country: 'Nicaragua',
    iso3: 'NIC',
    year: 2016,
    gdp_per_capita_usd: 2143.93,
    happiness_score: 5.992,
    co2_per_capita_t: 0.846,
    peer_avg_happiness: 4.574,
    peer_avg_co2: 1.315,
    happiness_gap_vs_peers: 1.418,
    co2_gap_vs_peers: -0.469
  },
  {
    peer_count: 221,
    gdp_bucket: 0,
    country: 'Uzbekistan',
    iso3: 'UZB',
    year: 2016,
    gdp_per_capita_usd: 2117.74,
    happiness_score: 5.987,
    co2_per_capita_t: 3.502,
    peer_avg_happiness: 4.574,
    peer_avg_co2: 1.315,
    happiness_gap_vs_peers: 1.413,
    co2_gap_vs_peers: 2.186
  },
  {
    peer_count: 221,
    gdp_bucket: 0,
    country: 'Uzbekistan',
    iso3: 'UZB',
    year: 2017,
    gdp_per_capita_usd: 1533.85,
    happiness_score: 5.971,
    co2_per_capita_t: 3.41,
    peer_avg_happiness: 4.574,
    peer_avg_co2: 1.315,
    happiness_gap_vs_peers: 1.397,
    co2_gap_vs_peers: 2.094
  },
  {
    peer_count: 221,
    gdp_bucket: 0,
    country: 'Belize',
    iso3: 'BLZ',
    year: 2017,
    gdp_per_capita_usd: 4971.2,
    happiness_score: 5.956,
    co2_per_capita_t: 1.643,
    peer_avg_happiness: 4.574,
    peer_avg_co2: 1.315,
    happiness_gap_vs_peers: 1.382,
    co2_gap_vs_peers: 0.327
  },
  {
    peer_count: 221,
    gdp_bucket: 0,
    country: 'Belize',
    iso3: 'BLZ',
    year: 2016,
    gdp_per_capita_usd: 4923.36,
    happiness_score: 5.956,
    co2_per_capita_t: 1.696,
    peer_avg_happiness: 4.574,
    peer_avg_co2: 1.315,
    happiness_gap_vs_peers: 1.382,
    co2_gap_vs_peers: 0.38
  },
  {
    peer_count: 221,
    gdp_bucket: 0,
    country: 'Moldova',
    iso3: 'MDA',
    year: 2016,
    gdp_per_capita_usd: 1913.24,
    happiness_score: 5.897,
    co2_per_capita_t: 1.52,
    peer_avg_happiness: 4.574,
    peer_avg_co2: 1.315,
    happiness_gap_vs_peers: 1.323,
    co2_gap_vs_peers: 0.205
  },
  {
    peer_count: 221,
    gdp_bucket: 0,
    country: 'Bolivia',
    iso3: 'BOL',
    year: 2015,
    gdp_per_capita_usd: 3077.03,
    happiness_score: 5.89,
    co2_per_capita_t: 1.915,
    peer_avg_happiness: 4.574,
    peer_avg_co2: 1.315,
    happiness_gap_vs_peers: 1.316,
    co2_gap_vs_peers: 0.6
  },
  {
    peer_count: 221,
    gdp_bucket: 0,
    country: 'Moldova',
    iso3: 'MDA',
    year: 2015,
    gdp_per_capita_usd: 1832.5,
    happiness_score: 5.889,
    co2_per_capita_t: 1.459,
    peer_avg_happiness: 4.574,
    peer_avg_co2: 1.315,
    happiness_gap_vs_peers: 1.315,
    co2_gap_vs_peers: 0.144
  }
]
```

---

## [12] Kategorie 2: Agregacni A Analyticke Dotazy / Dotaz 6

**Stav:** OK

```text
[
  {
    country: 'Burundi',
    year: 2015,
    iso3: 'BDI',
    happiness_rank: 156,
    low_co2_rank: 2,
    rank_gap: -154,
    abs_rank_gap: 154,
    happiness_score: 2.905,
    co2_per_capita_t: 0.037
  },
  {
    country: 'Burundi',
    year: 2016,
    iso3: 'BDI',
    happiness_rank: 156,
    low_co2_rank: 3,
    rank_gap: -153,
    abs_rank_gap: 153,
    happiness_score: 2.905,
    co2_per_capita_t: 0.043
  },
  {
    country: 'Central African Republic',
    year: 2017,
    iso3: 'CAF',
    happiness_rank: 154,
    low_co2_rank: 3,
    rank_gap: -151,
    abs_rank_gap: 151,
    happiness_score: 2.693,
    co2_per_capita_t: 0.043
  },
  {
    country: 'Burundi',
    year: 2018,
    iso3: 'BDI',
    happiness_rank: 155,
    low_co2_rank: 4,
    rank_gap: -151,
    abs_rank_gap: 151,
    happiness_score: 2.905,
    co2_per_capita_t: 0.059
  },
  {
    country: 'Central African Republic',
    year: 2018,
    iso3: 'CAF',
    happiness_rank: 154,
    low_co2_rank: 3,
    rank_gap: -151,
    abs_rank_gap: 151,
    happiness_score: 3.083,
    co2_per_capita_t: 0.043
  },
  {
    country: 'Central African Republic',
    year: 2019,
    iso3: 'CAF',
    happiness_rank: 154,
    low_co2_rank: 3,
    rank_gap: -151,
    abs_rank_gap: 151,
    happiness_score: 3.083,
    co2_per_capita_t: 0.044
  },
  {
    country: 'Burundi',
    year: 2017,
    iso3: 'BDI',
    happiness_rank: 153,
    low_co2_rank: 4,
    rank_gap: -149,
    abs_rank_gap: 149,
    happiness_score: 2.905,
    co2_per_capita_t: 0.048
  },
  {
    country: 'Rwanda',
    year: 2015,
    iso3: 'RWA',
    happiness_rank: 153,
    low_co2_rank: 6,
    rank_gap: -147,
    abs_rank_gap: 147,
    happiness_score: 3.465,
    co2_per_capita_t: 0.083
  },
  {
    country: 'Central African Republic',
    year: 2015,
    iso3: 'CAF',
    happiness_rank: 147,
    low_co2_rank: 3,
    rank_gap: -144,
    abs_rank_gap: 144,
    happiness_score: 3.678,
    co2_per_capita_t: 0.037
  },
  {
    country: 'Rwanda',
    year: 2016,
    iso3: 'RWA',
    happiness_rank: 151,
    low_co2_rank: 7,
    rank_gap: -144,
    abs_rank_gap: 144,
    happiness_score: 3.515,
    co2_per_capita_t: 0.09
  },
  {
    country: 'Rwanda',
    year: 2017,
    iso3: 'RWA',
    happiness_rank: 150,
    low_co2_rank: 6,
    rank_gap: -144,
    abs_rank_gap: 144,
    happiness_score: 3.471,
    co2_per_capita_t: 0.095
  },
  {
    country: 'Malawi',
    year: 2019,
    iso3: 'MWI',
    happiness_rank: 149,
    low_co2_rank: 5,
    rank_gap: -144,
    abs_rank_gap: 144,
    happiness_score: 3.41,
    co2_per_capita_t: 0.084
  },
  {
    country: 'Rwanda',
    year: 2018,
    iso3: 'RWA',
    happiness_rank: 150,
    low_co2_rank: 7,
    rank_gap: -143,
    abs_rank_gap: 143,
    happiness_score: 3.408,
    co2_per_capita_t: 0.102
  },
  {
    country: 'South Sudan',
    year: 2019,
    iso3: 'SSD',
    happiness_rank: 155,
    low_co2_rank: 12,
    rank_gap: -143,
    abs_rank_gap: 143,
    happiness_score: 2.853,
    co2_per_capita_t: 0.158
  },
  {
    country: 'Rwanda',
    year: 2019,
    iso3: 'RWA',
    happiness_rank: 151,
    low_co2_rank: 9,
    rank_gap: -142,
    abs_rank_gap: 142,
    happiness_score: 3.334,
    co2_per_capita_t: 0.141
  },
  {
    country: 'Canada',
    year: 2015,
    iso3: 'CAN',
    happiness_rank: 5,
    low_co2_rank: 146,
    rank_gap: 141,
    abs_rank_gap: 141,
    happiness_score: 7.427,
    co2_per_capita_t: 16.072
  },
  {
    country: 'Australia',
    year: 2016,
    iso3: 'AUS',
    happiness_rank: 9,
    low_co2_rank: 150,
    rank_gap: 141,
    abs_rank_gap: 141,
    happiness_score: 7.313,
    co2_per_capita_t: 16.997
  },
  {
    country: 'Chad',
    year: 2015,
    iso3: 'TCD',
    happiness_rank: 148,
    low_co2_rank: 8,
    rank_gap: -140,
    abs_rank_gap: 140,
    happiness_score: 3.667,
    co2_per_capita_t: 0.119
  },
  {
    country: 'Australia',
    year: 2015,
    iso3: 'AUS',
    happiness_rank: 10,
    low_co2_rank: 150,
    rank_gap: 140,
    abs_rank_gap: 140,
    happiness_score: 7.284,
    co2_per_capita_t: 16.868
  },
  {
    country: 'Canada',
    year: 2016,
    iso3: 'CAN',
    happiness_rank: 6,
    low_co2_rank: 146,
    rank_gap: 140,
    abs_rank_gap: 140,
    happiness_score: 7.404,
    co2_per_capita_t: 15.521
  }
]
```

---

## [13] Kategorie 3: Kvalita Dat A Validace / Dotaz 1

**Stav:** OK

```text
[
  {
    total_rows: 782,
    first_year: 2015,
    last_year: 2019,
    complete_core_rows: 457,
    missing_happiness: 0,
    missing_gdp: 322,
    missing_co2: 5,
    missing_life_expectancy: 315,
    country_count: 162,
    complete_core_rate_pct: 58.44,
    missing_gdp_pct: 41.18,
    missing_co2_pct: 0.64,
    missing_life_expectancy_pct: 40.28
  }
]
```

---

## [14] Kategorie 3: Kvalita Dat A Validace / Dotaz 2

**Stav:** OK

```text
[
  {
    coverage_distribution: [
      {
        country_year_count: 314,
        first_year: 1960,
        last_year: 2018,
        indicator_count: 1
      },
      {
        country_year_count: 668,
        first_year: 1960,
        last_year: 2017,
        indicator_count: 2
      },
      {
        country_year_count: 2162,
        first_year: 1960,
        last_year: 2017,
        indicator_count: 3
      },
      {
        country_year_count: 511,
        first_year: 1960,
        last_year: 2017,
        indicator_count: 4
      },
      {
        country_year_count: 1043,
        first_year: 1960,
        last_year: 2017,
        indicator_count: 5
      },
      {
        country_year_count: 4368,
        first_year: 1960,
        last_year: 2017,
        indicator_count: 6
      },
      {
        country_year_count: 1276,
        first_year: 1960,
        last_year: 2017,
        indicator_count: 7
      },
      {
        country_year_count: 5085,
        first_year: 1991,
        last_year: 2017,
        indicator_count: 8
      }
    ],
    weakest_country_years: [
      {
        non_missing_values: 1,
        indicator_count: 1,
        iso3: 'XKX',
        country: 'Kosovo',
        year: 1960,
        available_indicators: [ 'population_total' ]
      },
      {
        non_missing_values: 1,
        indicator_count: 1,
        iso3: 'SXM',
        country: 'Sint Maarten (Dutch part)',
        year: 1960,
        available_indicators: [ 'urban_population_pct' ]
      },
      {
        non_missing_values: 1,
        indicator_count: 1,
        iso3: 'MAF',
        country: 'St. Martin (French part)',
        year: 1960,
        available_indicators: [ 'population_total' ]
      },
      {
        non_missing_values: 1,
        indicator_count: 1,
        iso3: 'XKX',
        country: 'Kosovo',
        year: 1961,
        available_indicators: [ 'population_total' ]
      },
      {
        non_missing_values: 1,
        indicator_count: 1,
        iso3: 'SXM',
        country: 'Sint Maarten (Dutch part)',
        year: 1961,
        available_indicators: [ 'urban_population_pct' ]
      },
      {
        non_missing_values: 1,
        indicator_count: 1,
        iso3: 'MAF',
        country: 'St. Martin (French part)',
        year: 1961,
        available_indicators: [ 'population_total' ]
      },
      {
        non_missing_values: 1,
        indicator_count: 1,
        iso3: 'XKX',
        country: 'Kosovo',
        year: 1962,
        available_indicators: [ 'population_total' ]
      },
      {
        non_missing_values: 1,
        indicator_count: 1,
        iso3: 'SXM',
        country: 'Sint Maarten (Dutch part)',
        year: 1962,
        available_indicators: [ 'urban_population_pct' ]
      },
      {
        non_missing_values: 1,
        indicator_count: 1,
        iso3: 'MAF',
        country: 'St. Martin (French part)',
        year: 1962,
        available_indicators: [ 'population_total' ]
      },
      {
        non_missing_values: 1,
        indicator_count: 1,
        iso3: 'XKX',
        country: 'Kosovo',
        year: 1963,
        available_indicators: [ 'population_total' ]
      },
      {
        non_missing_values: 1,
        indicator_count: 1,
        iso3: 'SXM',
        country: 'Sint Maarten (Dutch part)',
        year: 1963,
        available_indicators: [ 'urban_population_pct' ]
      },
      {
        non_missing_values: 1,
        indicator_count: 1,
        iso3: 'MAF',
        country: 'St. Martin (French part)',
        year: 1963,
        available_indicators: [ 'population_total' ]
      }
    ],
    strongest_country_years: [
      {
        non_missing_values: 8,
        indicator_count: 8,
        iso3: 'AFG',
        country: 'Afghanistan',
        year: 2017,
        available_indicators: [
          'gdp_current_usd',
          'gdp_per_capita_usd',
          'internet_users_pct',
          'life_expectancy_years',
          'population_total',
          'trade_pct_gdp',
          'unemployment_pct',
          'urban_population_pct'
        ]
      },
      {
        non_missing_values: 8,
        indicator_count: 8,
        iso3: 'ALB',
        country: 'Albania',
        year: 2017,
        available_indicators: [
          'gdp_current_usd',
          'gdp_per_capita_usd',
          'internet_users_pct',
          'life_expectancy_years',
          'population_total',
          'trade_pct_gdp',
          'unemployment_pct',
          'urban_population_pct'
        ]
      },
      {
        non_missing_values: 8,
        indicator_count: 8,
        iso3: 'DZA',
        country: 'Algeria',
        year: 2017,
        available_indicators: [
          'gdp_current_usd',
          'gdp_per_capita_usd',
          'internet_users_pct',
          'life_expectancy_years',
          'population_total',
          'trade_pct_gdp',
          'unemployment_pct',
          'urban_population_pct'
        ]
      },
      {
        non_missing_values: 8,
        indicator_count: 8,
        iso3: 'AGO',
        country: 'Angola',
        year: 2017,
        available_indicators: [
          'gdp_current_usd',
          'gdp_per_capita_usd',
          'internet_users_pct',
          'life_expectancy_years',
          'population_total',
          'trade_pct_gdp',
          'unemployment_pct',
          'urban_population_pct'
        ]
      },
      {
        non_missing_values: 8,
        indicator_count: 8,
        iso3: 'ARB',
        country: 'Arab World',
        year: 2017,
        available_indicators: [
          'gdp_current_usd',
          'gdp_per_capita_usd',
          'internet_users_pct',
          'life_expectancy_years',
          'population_total',
          'trade_pct_gdp',
          'unemployment_pct',
          'urban_population_pct'
        ]
      },
      {
        non_missing_values: 8,
        indicator_count: 8,
        iso3: 'ARG',
        country: 'Argentina',
        year: 2017,
        available_indicators: [
          'gdp_current_usd',
          'gdp_per_capita_usd',
          'internet_users_pct',
          'life_expectancy_years',
          'population_total',
          'trade_pct_gdp',
          'unemployment_pct',
          'urban_population_pct'
        ]
      },
      {
        non_missing_values: 8,
        indicator_count: 8,
        iso3: 'ARM',
        country: 'Armenia',
        year: 2017,
        available_indicators: [
          'gdp_current_usd',
          'gdp_per_capita_usd',
          'internet_users_pct',
          'life_expectancy_years',
          'population_total',
          'trade_pct_gdp',
          'unemployment_pct',
          'urban_population_pct'
        ]
      },
      {
        non_missing_values: 8,
        indicator_count: 8,
        iso3: 'AUS',
        country: 'Australia',
        year: 2017,
        available_indicators: [
          'gdp_current_usd',
          'gdp_per_capita_usd',
          'internet_users_pct',
          'life_expectancy_years',
          'population_total',
          'trade_pct_gdp',
          'unemployment_pct',
          'urban_population_pct'
        ]
      },
      {
        non_missing_values: 8,
        indicator_count: 8,
        iso3: 'AUT',
        country: 'Austria',
        year: 2017,
        available_indicators: [
          'gdp_current_usd',
          'gdp_per_capita_usd',
          'internet_users_pct',
          'life_expectancy_years',
          'population_total',
          'trade_pct_gdp',
          'unemployment_pct',
          'urban_population_pct'
        ]
      },
      {
        non_missing_values: 8,
        indicator_count: 8,
        iso3: 'AZE',
        country: 'Azerbaijan',
        year: 2017,
        available_indicators: [
          'gdp_current_usd',
          'gdp_per_capita_usd',
          'internet_users_pct',
          'life_expectancy_years',
          'population_total',
          'trade_pct_gdp',
          'unemployment_pct',
          'urban_population_pct'
        ]
      },
      {
        non_missing_values: 8,
        indicator_count: 8,
        iso3: 'BHS',
        country: 'Bahamas, The',
        year: 2017,
        available_indicators: [
          'gdp_current_usd',
          'gdp_per_capita_usd',
          'internet_users_pct',
          'life_expectancy_years',
          'population_total',
          'trade_pct_gdp',
          'unemployment_pct',
          'urban_population_pct'
        ]
      },
      {
        non_missing_values: 8,
        indicator_count: 8,
        iso3: 'BHR',
        country: 'Bahrain',
        year: 2017,
        available_indicators: [
          'gdp_current_usd',
          'gdp_per_capita_usd',
          'internet_users_pct',
          'life_expectancy_years',
          'population_total',
          'trade_pct_gdp',
          'unemployment_pct',
          'urban_population_pct'
        ]
      }
    ]
  }
]
```

---

## [15] Kategorie 3: Kvalita Dat A Validace / Dotaz 3

**Stav:** OK

```text
[
  {
    total_rows: 15147,
    non_missing_rows: 15147,
    first_year: 1960,
    last_year: 2017,
    indicator: 'population_total',
    missing_rows: 0,
    non_missing_rate_pct: 100,
    countries_with_value: 263,
    min_value: 4279,
    max_value: 7529719387
  },
  {
    total_rows: 15072,
    non_missing_rows: 15072,
    first_year: 1960,
    last_year: 2017,
    indicator: 'urban_population_pct',
    missing_rows: 0,
    non_missing_rate_pct: 100,
    countries_with_value: 261,
    min_value: 2.08,
    max_value: 100
  },
  {
    total_rows: 13997,
    non_missing_rows: 13997,
    first_year: 1960,
    last_year: 2017,
    indicator: 'life_expectancy_years',
    missing_rows: 0,
    non_missing_rate_pct: 100,
    countries_with_value: 254,
    min_value: 18.91,
    max_value: 85.42
  },
  {
    total_rows: 11831,
    non_missing_rows: 11831,
    first_year: 1960,
    last_year: 2017,
    indicator: 'gdp_current_usd',
    missing_rows: 0,
    non_missing_rate_pct: 100,
    countries_with_value: 256,
    min_value: 8824447.74,
    max_value: 80934771028340.3
  },
  {
    total_rows: 11828,
    non_missing_rows: 11828,
    first_year: 1960,
    last_year: 2017,
    indicator: 'gdp_per_capita_usd',
    missing_rows: 0,
    non_missing_rate_pct: 100,
    countries_with_value: 256,
    min_value: 34.74,
    max_value: 185152.53
  },
  {
    total_rows: 10597,
    non_missing_rows: 10597,
    first_year: 1960,
    last_year: 2017,
    indicator: 'trade_pct_gdp',
    missing_rows: 0,
    non_missing_rate_pct: 100,
    countries_with_value: 246,
    min_value: 0,
    max_value: 860.8
  },
  {
    total_rows: 6524,
    non_missing_rows: 6524,
    first_year: 1991,
    last_year: 2018,
    indicator: 'unemployment_pct',
    missing_rows: 0,
    non_missing_rate_pct: 100,
    countries_with_value: 233,
    min_value: 0.14,
    max_value: 37.94
  },
  {
    total_rows: 6219,
    non_missing_rows: 6219,
    first_year: 1960,
    last_year: 2017,
    indicator: 'internet_users_pct',
    missing_rows: 0,
    non_missing_rate_pct: 100,
    countries_with_value: 258,
    min_value: 0,
    max_value: 98.87
  }
]
```

---

## [16] Kategorie 3: Kvalita Dat A Validace / Dotaz 4

**Stav:** OK

```text
[
  {
    years_observed: 1,
    missing_years: [ 2016, 2017, 2018, 2019 ],
    iso3: 'DJI',
    country: 'Djibouti',
    years_present: [ 2015 ]
  },
  {
    years_observed: 1,
    missing_years: [ 2015, 2016, 2017, 2018 ],
    iso3: 'GMB',
    country: 'Gambia',
    years_present: [ 2019 ]
  },
  {
    years_observed: 1,
    missing_years: [ 2015, 2016, 2018, 2019 ],
    iso3: 'HKG',
    country: 'Hong Kong S.A.R., China',
    years_present: [ 2017 ]
  },
  {
    years_observed: 1,
    missing_years: [ 2015, 2016, 2017, 2018 ],
    iso3: 'MKD',
    country: 'North Macedonia',
    years_present: [ 2019 ]
  },
  {
    years_observed: 1,
    missing_years: [ 2016, 2017, 2018, 2019 ],
    iso3: 'OMN',
    country: 'Oman',
    years_present: [ 2015 ]
  },
  {
    years_observed: 1,
    missing_years: [ 2015, 2017, 2018, 2019 ],
    iso3: 'PRI',
    country: 'Puerto Rico',
    years_present: [ 2016 ]
  },
  {
    years_observed: 1,
    missing_years: [ 2015, 2017, 2018, 2019 ],
    iso3: 'SOM',
    country: 'Somaliland Region',
    years_present: [ 2016 ]
  },
  {
    years_observed: 1,
    missing_years: [ 2016, 2017, 2018, 2019 ],
    iso3: 'SOM',
    country: 'Somaliland region',
    years_present: [ 2015 ]
  },
  {
    years_observed: 1,
    missing_years: [ 2015, 2016, 2018, 2019 ],
    iso3: 'TWN',
    country: 'Taiwan Province of China',
    years_present: [ 2017 ]
  },
  {
    years_observed: 2,
    missing_years: [ 2015, 2016, 2017 ],
    iso3: 'CYP',
    country: 'Northern Cyprus',
    years_present: [ 2018, 2019 ]
  },
  {
    years_observed: 2,
    missing_years: [ 2017, 2018, 2019 ],
    iso3: 'SUR',
    country: 'Suriname',
    years_present: [ 2015, 2016 ]
  },
  {
    years_observed: 2,
    missing_years: [ 2016, 2017, 2018 ],
    iso3: 'SWZ',
    country: 'Swaziland',
    years_present: [ 2015, 2019 ]
  },
  {
    years_observed: 2,
    missing_years: [ 2015, 2016, 2017 ],
    iso3: 'TTO',
    country: 'Trinidad & Tobago',
    years_present: [ 2018, 2019 ]
  },
  {
    years_observed: 3,
    missing_years: [ 2015, 2019 ],
    iso3: 'BLZ',
    country: 'Belize',
    years_present: [ 2016, 2017, 2018 ]
  },
  {
    years_observed: 3,
    missing_years: [ 2017, 2018 ],
    iso3: 'COM',
    country: 'Comoros',
    years_present: [ 2015, 2016, 2019 ]
  },
  {
    years_observed: 3,
    missing_years: [ 2018, 2019 ],
    iso3: 'CYP',
    country: 'North Cyprus',
    years_present: [ 2015, 2016, 2017 ]
  },
  {
    years_observed: 3,
    missing_years: [ 2018, 2019 ],
    iso3: 'TTO',
    country: 'Trinidad and Tobago',
    years_present: [ 2015, 2016, 2017 ]
  },
  {
    years_observed: 4,
    missing_years: [ 2019 ],
    iso3: 'AGO',
    country: 'Angola',
    years_present: [ 2015, 2016, 2017, 2018 ]
  },
  {
    years_observed: 4,
    missing_years: [ 2016 ],
    iso3: 'CAF',
    country: 'Central African Republic',
    years_present: [ 2015, 2017, 2018, 2019 ]
  },
  {
    years_observed: 4,
    missing_years: [ 2017 ],
    iso3: 'HKG',
    country: 'Hong Kong',
    years_present: [ 2015, 2016, 2018, 2019 ]
  },
  {
    years_observed: 4,
    missing_years: [ 2017 ],
    iso3: 'LAO',
    country: 'Laos',
    years_present: [ 2015, 2016, 2018, 2019 ]
  },
  {
    years_observed: 4,
    missing_years: [ 2016 ],
    iso3: 'LSO',
    country: 'Lesotho',
    years_present: [ 2015, 2017, 2018, 2019 ]
  },
  {
    years_observed: 4,
    missing_years: [ 2019 ],
    iso3: 'MKD',
    country: 'Macedonia',
    years_present: [ 2015, 2016, 2017, 2018 ]
  },
  {
    years_observed: 4,
    missing_years: [ 2016 ],
    iso3: 'MOZ',
    country: 'Mozambique',
    years_present: [ 2015, 2017, 2018, 2019 ]
  },
  {
    years_observed: 4,
    missing_years: [ 2015 ],
    iso3: 'NAM',
    country: 'Namibia',
    years_present: [ 2016, 2017, 2018, 2019 ]
  }
]
```

---

## [17] Kategorie 3: Kvalita Dat A Validace / Dotaz 5

**Stav:** OK

```text
[
  {
    validation_status: 'OK - no out-of-range examples found',
    invalid_happiness_count: 0,
    invalid_happiness_examples: 'no invalid happiness examples',
    invalid_internet_count: 0,
    invalid_internet_examples: 'no invalid internet examples',
    invalid_life_expectancy_count: 0,
    invalid_life_expectancy_examples: 'no invalid life expectancy examples',
    invalid_co2_count: 0,
    invalid_co2_examples: 'no invalid CO2 examples'
  }
]
```

---

## [18] Kategorie 3: Kvalita Dat A Validace / Dotaz 6

**Stav:** OK

```text
[
  {
    summary: [
      {
        compared_rows: 782,
        mismatch_rows: 0,
        max_difference: 0,
        consistency_status: 'OK - master matches source happiness'
      }
    ],
    mismatch_examples: 'no mismatch examples'
  }
]
```

---

## [19] Kategorie 4: Profily Faktoru Happiness / Dotaz 1

**Stav:** OK

```text
[
  {
    years_observed: 4,
    iso3: 'CAF',
    country: 'Central African Republic',
    avg_happiness: 3.134,
    avg_factor_level: 0.117,
    avg_factor_balance_range: 0.327
  },
  {
    years_observed: 5,
    iso3: 'TGO',
    country: 'Togo',
    avg_happiness: 3.544,
    avg_factor_level: 0.253,
    avg_factor_balance_range: 0.36
  },
  {
    years_observed: 5,
    iso3: 'BEN',
    country: 'Benin',
    avg_happiness: 3.901,
    avg_factor_level: 0.278,
    avg_factor_balance_range: 0.367
  },
  {
    years_observed: 5,
    iso3: 'AFG',
    country: 'Afghanistan',
    avg_happiness: 3.513,
    avg_factor_level: 0.244,
    avg_factor_balance_range: 0.423
  },
  {
    years_observed: 5,
    iso3: 'MWI',
    country: 'Malawi',
    avg_happiness: 3.883,
    avg_factor_level: 0.285,
    avg_factor_balance_range: 0.425
  },
  {
    years_observed: 5,
    iso3: 'BDI',
    country: 'Burundi',
    avg_happiness: 3.079,
    avg_factor_level: 0.19,
    avg_factor_balance_range: 0.425
  },
  {
    years_observed: 4,
    iso3: 'SSD',
    country: 'South Sudan',
    avg_happiness: 3.383,
    avg_factor_level: 0.253,
    avg_factor_balance_range: 0.454
  },
  {
    years_observed: 5,
    iso3: 'GIN',
    country: 'Guinea',
    avg_happiness: 3.854,
    avg_factor_level: 0.31,
    avg_factor_balance_range: 0.531
  },
  {
    years_observed: 5,
    iso3: 'RWA',
    country: 'Rwanda',
    avg_happiness: 3.439,
    avg_factor_level: 0.468,
    avg_factor_balance_range: 0.563
  },
  {
    years_observed: 5,
    iso3: 'HTI',
    country: 'Haiti',
    avg_happiness: 3.866,
    avg_factor_level: 0.323,
    avg_factor_balance_range: 0.578
  },
  {
    years_observed: 5,
    iso3: 'BGD',
    country: 'Bangladesh',
    avg_happiness: 4.58,
    avg_factor_level: 0.424,
    avg_factor_balance_range: 0.599
  },
  {
    years_observed: 5,
    iso3: 'ETH',
    country: 'Ethiopia',
    avg_happiness: 4.423,
    avg_factor_level: 0.379,
    avg_factor_balance_range: 0.619
  },
  {
    years_observed: 5,
    iso3: 'PAK',
    country: 'Pakistan',
    avg_happiness: 5.344,
    avg_factor_level: 0.393,
    avg_factor_balance_range: 0.626
  },
  {
    years_observed: 5,
    iso3: 'SYR',
    country: 'Syria',
    avg_happiness: 3.292,
    avg_factor_level: 0.382,
    avg_factor_balance_range: 0.629
  },
  {
    years_observed: 5,
    iso3: 'IND',
    country: 'India',
    avg_happiness: 4.298,
    avg_factor_level: 0.432,
    avg_factor_balance_range: 0.649
  }
]
```

---

## [20] Kategorie 4: Profily Faktoru Happiness / Dotaz 2

**Stav:** OK

```text
[
  {
    dominant_factor: 'freedom',
    iso3: 'MWI',
    country: 'Malawi',
    year: 2015,
    happiness_score: 4.292,
    dominant_factor_value: 0.431
  },
  {
    dominant_factor: 'freedom',
    iso3: 'KHM',
    country: 'Cambodia',
    year: 2015,
    happiness_score: 3.819,
    dominant_factor_value: 0.662
  },
  {
    dominant_factor: 'freedom',
    iso3: 'CAF',
    country: 'Central African Republic',
    year: 2015,
    happiness_score: 3.678,
    dominant_factor_value: 0.489
  },
  {
    dominant_factor: 'freedom',
    iso3: 'BEN',
    country: 'Benin',
    year: 2015,
    happiness_score: 3.34,
    dominant_factor_value: 0.484
  },
  {
    dominant_factor: 'freedom',
    iso3: 'TGO',
    country: 'Togo',
    year: 2015,
    happiness_score: 2.839,
    dominant_factor_value: 0.365
  },
  {
    dominant_factor: 'gdp',
    iso3: 'CHE',
    country: 'Switzerland',
    year: 2015,
    happiness_score: 7.587,
    dominant_factor_value: 1.397
  },
  {
    dominant_factor: 'gdp',
    iso3: 'NOR',
    country: 'Norway',
    year: 2015,
    happiness_score: 7.522,
    dominant_factor_value: 1.459
  },
  {
    dominant_factor: 'gdp',
    iso3: 'CAN',
    country: 'Canada',
    year: 2015,
    happiness_score: 7.427,
    dominant_factor_value: 1.326
  },
  {
    dominant_factor: 'gdp',
    iso3: 'NLD',
    country: 'Netherlands',
    year: 2015,
    happiness_score: 7.378,
    dominant_factor_value: 1.329
  },
  {
    dominant_factor: 'gdp',
    iso3: 'SWE',
    country: 'Sweden',
    year: 2015,
    happiness_score: 7.364,
    dominant_factor_value: 1.332
  },
  {
    dominant_factor: 'gdp',
    iso3: 'AUS',
    country: 'Australia',
    year: 2015,
    happiness_score: 7.284,
    dominant_factor_value: 1.334
  },
  {
    dominant_factor: 'gdp',
    iso3: 'ISR',
    country: 'Israel',
    year: 2015,
    happiness_score: 7.278,
    dominant_factor_value: 1.229
  },
  {
    dominant_factor: 'gdp',
    iso3: 'AUT',
    country: 'Austria',
    year: 2015,
    happiness_score: 7.2,
    dominant_factor_value: 1.337
  },
  {
    dominant_factor: 'gdp',
    iso3: 'MEX',
    country: 'Mexico',
    year: 2015,
    happiness_score: 7.187,
    dominant_factor_value: 1.021
  },
  {
    dominant_factor: 'gdp',
    iso3: 'USA',
    country: 'United States',
    year: 2015,
    happiness_score: 7.119,
    dominant_factor_value: 1.395
  },
  {
    dominant_factor: 'gdp',
    iso3: 'LUX',
    country: 'Luxembourg',
    year: 2015,
    happiness_score: 6.946,
    dominant_factor_value: 1.564
  },
  {
    dominant_factor: 'gdp',
    iso3: 'BEL',
    country: 'Belgium',
    year: 2015,
    happiness_score: 6.937,
    dominant_factor_value: 1.308
  },
  {
    dominant_factor: 'gdp',
    iso3: 'ARE',
    country: 'United Arab Emirates',
    year: 2015,
    happiness_score: 6.901,
    dominant_factor_value: 1.427
  },
  {
    dominant_factor: 'gdp',
    iso3: 'OMN',
    country: 'Oman',
    year: 2015,
    happiness_score: 6.853,
    dominant_factor_value: 1.36
  },
  {
    dominant_factor: 'gdp',
    iso3: 'SGP',
    country: 'Singapore',
    year: 2015,
    happiness_score: 6.798,
    dominant_factor_value: 1.522
  },
  {
    dominant_factor: 'gdp',
    iso3: 'DEU',
    country: 'Germany',
    year: 2015,
    happiness_score: 6.75,
    dominant_factor_value: 1.328
  },
  {
    dominant_factor: 'gdp',
    iso3: 'QAT',
    country: 'Qatar',
    year: 2015,
    happiness_score: 6.611,
    dominant_factor_value: 1.69
  },
  {
    dominant_factor: 'gdp',
    iso3: 'FRA',
    country: 'France',
    year: 2015,
    happiness_score: 6.575,
    dominant_factor_value: 1.278
  },
  {
    dominant_factor: 'gdp',
    iso3: 'SAU',
    country: 'Saudi Arabia',
    year: 2015,
    happiness_score: 6.411,
    dominant_factor_value: 1.395
  },
  {
    dominant_factor: 'gdp',
    iso3: 'TWN',
    country: 'Taiwan',
    year: 2015,
    happiness_score: 6.298,
    dominant_factor_value: 1.291
  }
]
```

---

## [21] Kategorie 4: Profily Faktoru Happiness / Dotaz 3

**Stav:** OK

```text
[
  {
    country: 'Costa Rica',
    year: 2015,
    iso3: 'CRI',
    happiness_score: 7.226,
    gdp_factor: 0.956,
    social_support_factor: 1.238,
    health_factor: 0.86,
    freedom_factor: 0.634
  },
  {
    country: 'Brazil',
    year: 2015,
    iso3: 'BRA',
    happiness_score: 6.983,
    gdp_factor: 0.981,
    social_support_factor: 1.233,
    health_factor: 0.697,
    freedom_factor: 0.49
  },
  {
    country: 'Colombia',
    year: 2015,
    iso3: 'COL',
    happiness_score: 6.477,
    gdp_factor: 0.919,
    social_support_factor: 1.24,
    health_factor: 0.691,
    freedom_factor: 0.535
  },
  {
    country: 'Thailand',
    year: 2015,
    iso3: 'THA',
    happiness_score: 6.455,
    gdp_factor: 0.967,
    social_support_factor: 1.265,
    health_factor: 0.739,
    freedom_factor: 0.557
  },
  {
    country: 'Guatemala',
    year: 2017,
    iso3: 'GTM',
    happiness_score: 6.454,
    gdp_factor: 0.872,
    social_support_factor: 1.256,
    health_factor: 0.54,
    freedom_factor: 0.531
  },
  {
    country: 'Guatemala',
    year: 2019,
    iso3: 'GTM',
    happiness_score: 6.436,
    gdp_factor: 0.8,
    social_support_factor: 1.269,
    health_factor: 0.746,
    freedom_factor: 0.535
  },
  {
    country: 'Brazil',
    year: 2018,
    iso3: 'BRA',
    happiness_score: 6.419,
    gdp_factor: 0.986,
    social_support_factor: 1.474,
    health_factor: 0.675,
    freedom_factor: 0.493
  },
  {
    country: 'Guatemala',
    year: 2018,
    iso3: 'GTM',
    happiness_score: 6.382,
    gdp_factor: 0.781,
    social_support_factor: 1.268,
    health_factor: 0.608,
    freedom_factor: 0.604
  },
  {
    country: 'Guatemala',
    year: 2016,
    iso3: 'GTM',
    happiness_score: 6.324,
    gdp_factor: 0.835,
    social_support_factor: 0.871,
    health_factor: 0.54,
    freedom_factor: 0.504
  },
  {
    country: 'Suriname',
    year: 2015,
    iso3: 'SUR',
    happiness_score: 6.269,
    gdp_factor: 0.995,
    social_support_factor: 0.972,
    health_factor: 0.608,
    freedom_factor: 0.597
  },
  {
    country: 'Colombia',
    year: 2018,
    iso3: 'COL',
    happiness_score: 6.26,
    gdp_factor: 0.96,
    social_support_factor: 1.439,
    health_factor: 0.635,
    freedom_factor: 0.531
  },
  {
    country: 'El Salvador',
    year: 2019,
    iso3: 'SLV',
    happiness_score: 6.253,
    gdp_factor: 0.794,
    social_support_factor: 1.242,
    health_factor: 0.789,
    freedom_factor: 0.43
  },
  {
    country: 'Uzbekistan',
    year: 2019,
    iso3: 'UZB',
    happiness_score: 6.174,
    gdp_factor: 0.745,
    social_support_factor: 1.529,
    health_factor: 0.756,
    freedom_factor: 0.631
  },
  {
    country: 'El Salvador',
    year: 2018,
    iso3: 'SLV',
    happiness_score: 6.167,
    gdp_factor: 0.806,
    social_support_factor: 1.231,
    health_factor: 0.639,
    freedom_factor: 0.461
  },
  {
    country: 'Nicaragua',
    year: 2018,
    iso3: 'NIC',
    happiness_score: 6.141,
    gdp_factor: 0.668,
    social_support_factor: 1.319,
    health_factor: 0.7,
    freedom_factor: 0.527
  },
  {
    country: 'El Salvador',
    year: 2015,
    iso3: 'SLV',
    happiness_score: 6.13,
    gdp_factor: 0.765,
    social_support_factor: 1.025,
    health_factor: 0.677,
    freedom_factor: 0.404
  },
  {
    country: 'Colombia',
    year: 2019,
    iso3: 'COL',
    happiness_score: 6.125,
    gdp_factor: 0.985,
    social_support_factor: 1.41,
    health_factor: 0.841,
    freedom_factor: 0.47
  },
  {
    country: 'Guatemala',
    year: 2015,
    iso3: 'GTM',
    happiness_score: 6.123,
    gdp_factor: 0.746,
    social_support_factor: 1.044,
    health_factor: 0.644,
    freedom_factor: 0.577
  },
  {
    country: 'Nicaragua',
    year: 2019,
    iso3: 'NIC',
    happiness_score: 6.105,
    gdp_factor: 0.694,
    social_support_factor: 1.325,
    health_factor: 0.835,
    freedom_factor: 0.435
  },
  {
    country: 'Kosovo',
    year: 2019,
    iso3: 'XKX',
    happiness_score: 6.1,
    gdp_factor: 0.882,
    social_support_factor: 1.232,
    health_factor: 0.758,
    freedom_factor: 0.489
  }
]
```

---

## [22] Kategorie 4: Profily Faktoru Happiness / Dotaz 4

**Stav:** OK

```text
[
  {
    row_count: 72,
    happiness_group: 'high_happiness',
    avg_happiness: 7.342,
    avg_social_support: 1.384,
    avg_freedom: 0.585,
    avg_corruption_factor: 0.286
  },
  {
    row_count: 411,
    happiness_group: 'middle_happiness',
    avg_happiness: 5.878,
    avg_social_support: 1.197,
    avg_freedom: 0.436,
    avg_corruption_factor: 0.116
  },
  {
    row_count: 298,
    happiness_group: 'low_happiness',
    avg_happiness: 4.212,
    avg_social_support: 0.842,
    avg_freedom: 0.335,
    avg_corruption_factor: 0.1
  }
]
```

---

## [23] Kategorie 4: Profily Faktoru Happiness / Dotaz 5

**Stav:** OK

```text
[
  {
    years_observed: 5,
    iso3: 'ARE',
    country: 'United Arab Emirates',
    avg_happiness: 6.744,
    std_social_support: 0.2373,
    std_freedom: 0.1452,
    std_generosity: 0.0621,
    factor_volatility_score: 0.4446
  },
  {
    years_observed: 5,
    iso3: 'MMR',
    country: 'Myanmar',
    avg_happiness: 4.383,
    std_social_support: 0.2502,
    std_freedom: 0.0635,
    std_generosity: 0.1306,
    factor_volatility_score: 0.4443
  },
  {
    years_observed: 5,
    iso3: 'XKX',
    country: 'Kosovo',
    avg_happiness: 5.606,
    std_social_support: 0.2623,
    std_freedom: 0.1455,
    std_generosity: 0.0218,
    factor_volatility_score: 0.4296
  },
  {
    years_observed: 5,
    iso3: 'PAK',
    country: 'Pakistan',
    avg_happiness: 5.344,
    std_social_support: 0.2646,
    std_freedom: 0.0957,
    std_generosity: 0.0574,
    factor_volatility_score: 0.4177
  },
  {
    years_observed: 5,
    iso3: 'LBN',
    country: 'Lebanon',
    avg_happiness: 5.15,
    std_social_support: 0.2584,
    std_freedom: 0.1107,
    std_generosity: 0.0361,
    factor_volatility_score: 0.4052
  },
  {
    years_observed: 5,
    iso3: 'MUS',
    country: 'Mauritius',
    avg_happiness: 5.707,
    std_social_support: 0.2761,
    std_freedom: 0.0512,
    std_generosity: 0.0772,
    factor_volatility_score: 0.4045
  },
  {
    years_observed: 5,
    iso3: 'KHM',
    country: 'Cambodia',
    avg_happiness: 4.205,
    std_social_support: 0.2733,
    std_freedom: 0.0426,
    std_generosity: 0.0849,
    factor_volatility_score: 0.4008
  },
  {
    years_observed: 5,
    iso3: 'HRV',
    country: 'Croatia',
    avg_happiness: 5.459,
    std_social_support: 0.2668,
    std_freedom: 0.0565,
    std_generosity: 0.0736,
    factor_volatility_score: 0.3969
  },
  {
    years_observed: 5,
    iso3: 'BGD',
    country: 'Bangladesh',
    avg_happiness: 4.58,
    std_social_support: 0.2889,
    std_freedom: 0.0776,
    std_generosity: 0.0232,
    factor_volatility_score: 0.3897
  },
  {
    years_observed: 4,
    iso3: 'LAO',
    country: 'Laos',
    avg_happiness: 4.793,
    std_social_support: 0.2369,
    std_freedom: 0.0471,
    std_generosity: 0.1041,
    factor_volatility_score: 0.3881
  },
  {
    years_observed: 5,
    iso3: 'AFG',
    country: 'Afghanistan',
    avg_happiness: 3.513,
    std_social_support: 0.1989,
    std_freedom: 0.0877,
    std_generosity: 0.0886,
    factor_volatility_score: 0.3752
  },
  {
    years_observed: 5,
    iso3: 'YEM',
    country: 'Yemen',
    avg_happiness: 3.626,
    std_social_support: 0.2842,
    std_freedom: 0.0757,
    std_generosity: 0.01,
    factor_volatility_score: 0.3699
  },
  {
    years_observed: 5,
    iso3: 'ETH',
    country: 'Ethiopia',
    avg_happiness: 4.423,
    std_social_support: 0.2695,
    std_freedom: 0.0452,
    std_generosity: 0.0459,
    factor_volatility_score: 0.3607
  },
  {
    years_observed: 5,
    iso3: 'SGP',
    country: 'Singapore',
    avg_happiness: 6.543,
    std_social_support: 0.2711,
    std_freedom: 0.0512,
    std_generosity: 0.0363,
    factor_volatility_score: 0.3586
  },
  {
    years_observed: 5,
    iso3: 'GBR',
    country: 'United Kingdom',
    avg_happiness: 6.91,
    std_social_support: 0.1841,
    std_freedom: 0.0571,
    std_generosity: 0.1138,
    factor_volatility_score: 0.355
  },
  {
    years_observed: 5,
    iso3: 'NPL',
    country: 'Nepal',
    avg_happiness: 4.812,
    std_social_support: 0.2438,
    std_freedom: 0.0616,
    std_generosity: 0.0484,
    factor_volatility_score: 0.3539
  },
  {
    years_observed: 5,
    iso3: 'LKA',
    country: 'Sri Lanka',
    avg_happiness: 4.393,
    std_social_support: 0.2002,
    std_freedom: 0.045,
    std_generosity: 0.1059,
    factor_volatility_score: 0.3511
  },
  {
    years_observed: 4,
    iso3: 'HKG',
    country: 'Hong Kong',
    avg_happiness: 5.448,
    std_social_support: 0.1998,
    std_freedom: 0.0667,
    std_generosity: 0.0844,
    factor_volatility_score: 0.3509
  },
  {
    years_observed: 4,
    iso3: 'TWN',
    country: 'Taiwan',
    avg_happiness: 6.391,
    std_social_support: 0.2567,
    std_freedom: 0.0429,
    std_generosity: 0.05,
    factor_volatility_score: 0.3496
  },
  {
    years_observed: 5,
    iso3: 'BGR',
    country: 'Bulgaria',
    avg_happiness: 4.619,
    std_social_support: 0.2681,
    std_freedom: 0.0533,
    std_generosity: 0.0273,
    factor_volatility_score: 0.3487
  }
]
```

---

## [24] Kategorie 4: Profily Faktoru Happiness / Dotaz 6

**Stav:** OK

```text
[
  {
    countries_count: 158,
    year: 2015,
    avg_happiness: 5.376,
    avg_gdp_factor: 0.846,
    avg_social_support_factor: 0.991,
    avg_health_factor: 0.63,
    avg_freedom_factor: 0.429,
    avg_generosity_factor: 0.237,
    avg_corruption_factor: 0.143
  },
  {
    countries_count: 157,
    year: 2016,
    avg_happiness: 5.382,
    avg_gdp_factor: 0.954,
    avg_social_support_factor: 0.794,
    avg_health_factor: 0.558,
    avg_freedom_factor: 0.371,
    avg_generosity_factor: 0.243,
    avg_corruption_factor: 0.138
  },
  {
    countries_count: 155,
    year: 2017,
    avg_happiness: 5.354,
    avg_gdp_factor: 0.985,
    avg_social_support_factor: 1.189,
    avg_health_factor: 0.551,
    avg_freedom_factor: 0.409,
    avg_generosity_factor: 0.247,
    avg_corruption_factor: 0.123
  },
  {
    countries_count: 156,
    year: 2018,
    avg_happiness: 5.376,
    avg_gdp_factor: 0.891,
    avg_social_support_factor: 1.213,
    avg_health_factor: 0.597,
    avg_freedom_factor: 0.455,
    avg_generosity_factor: 0.181,
    avg_corruption_factor: 0.112
  },
  {
    countries_count: 156,
    year: 2019,
    avg_happiness: 5.407,
    avg_gdp_factor: 0.905,
    avg_social_support_factor: 1.209,
    avg_health_factor: 0.725,
    avg_freedom_factor: 0.393,
    avg_generosity_factor: 0.185,
    avg_corruption_factor: 0.111
  }
]
```

---

## [25] Kategorie 5: Historicke Trendy CO2 A WDI / Dotaz 1

**Stav:** OK

```text
[
  {
    iso3: 'LAO',
    country: 'Laos',
    co2_1990: 0.119,
    co2_2019: 2.717,
    co2_change_t: 2.598,
    co2_growth_pct: 2185.35
  },
  {
    iso3: 'GNQ',
    country: 'Equatorial Guinea',
    co2_1990: 0.134,
    co2_2019: 2.986,
    co2_change_t: 2.853,
    co2_growth_pct: 2132.07
  },
  {
    iso3: 'NPL',
    country: 'Nepal',
    co2_1990: 0.037,
    co2_2019: 0.466,
    co2_change_t: 0.429,
    co2_growth_pct: 1166.38
  },
  {
    iso3: 'VNM',
    country: 'Viet Nam',
    co2_1990: 0.318,
    co2_2019: 3.56,
    co2_change_t: 3.242,
    co2_growth_pct: 1018.55
  },
  {
    iso3: 'BTN',
    country: 'Bhutan',
    co2_1990: 0.23,
    co2_2019: 1.886,
    co2_change_t: 1.656,
    co2_growth_pct: 721.08
  },
  {
    iso3: 'KHM',
    country: 'Cambodia',
    co2_1990: 0.141,
    co2_2019: 1.112,
    co2_change_t: 0.971,
    co2_growth_pct: 686.23
  },
  {
    iso3: 'MMR',
    country: 'Myanmar',
    co2_1990: 0.106,
    co2_2019: 0.653,
    co2_change_t: 0.547,
    co2_growth_pct: 517.73
  },
  {
    iso3: 'BEN',
    country: 'Benin',
    co2_1990: 0.113,
    co2_2019: 0.581,
    co2_change_t: 0.468,
    co2_growth_pct: 415.04
  },
  {
    iso3: 'MDV',
    country: 'Maldives',
    co2_1990: 0.766,
    co2_2019: 3.871,
    co2_change_t: 3.105,
    co2_growth_pct: 405.66
  },
  {
    iso3: 'LKA',
    country: 'Sri Lanka',
    co2_1990: 0.223,
    co2_2019: 1.026,
    co2_change_t: 0.804,
    co2_growth_pct: 360.93
  },
  {
    iso3: 'BGD',
    country: 'Bangladesh',
    co2_1990: 0.131,
    co2_2019: 0.554,
    co2_change_t: 0.422,
    co2_growth_pct: 321.37
  },
  {
    iso3: 'MLI',
    country: 'Mali',
    co2_1990: 0.047,
    co2_2019: 0.187,
    co2_change_t: 0.14,
    co2_growth_pct: 296.93
  },
  {
    iso3: 'BFA',
    country: 'Burkina Faso',
    co2_1990: 0.064,
    co2_2019: 0.253,
    co2_change_t: 0.189,
    co2_growth_pct: 296.23
  },
  {
    iso3: 'CHN',
    country: 'China',
    co2_1990: 2.154,
    co2_2019: 7.554,
    co2_change_t: 5.4,
    co2_growth_pct: 250.74
  },
  {
    iso3: 'UGA',
    country: 'Uganda',
    co2_1990: 0.043,
    co2_2019: 0.14,
    co2_change_t: 0.097,
    co2_growth_pct: 223.54
  },
  {
    iso3: 'MNG',
    country: 'Mongolia',
    co2_1990: 4.53,
    co2_2019: 14.619,
    co2_change_t: 10.089,
    co2_growth_pct: 222.72
  },
  {
    iso3: 'MOZ',
    country: 'Mozambique',
    co2_1990: 0.074,
    co2_2019: 0.236,
    co2_change_t: 0.162,
    co2_growth_pct: 217.51
  },
  {
    iso3: 'COG',
    country: 'Congo',
    co2_1990: 0.423,
    co2_2019: 1.318,
    co2_change_t: 0.895,
    co2_growth_pct: 211.9
  },
  {
    iso3: 'IDN',
    country: 'Indonesia',
    co2_1990: 0.795,
    co2_2019: 2.446,
    co2_change_t: 1.651,
    co2_growth_pct: 207.73
  },
  {
    iso3: 'VCT',
    country: 'Saint Vincent and the Grenadines',
    co2_1990: 0.717,
    co2_2019: 2.165,
    co2_change_t: 1.448,
    co2_growth_pct: 202.13
  }
]
```

---

## [26] Kategorie 5: Historicke Trendy CO2 A WDI / Dotaz 2

**Stav:** OK

```text
[
  {
    country: 'Global',
    iso3: 'WLD',
    year: 2019,
    co2_total_mt: 37082.56,
    coal_share_pct: 39.71,
    oil_share_pct: 33.29,
    gas_share_pct: 20.62,
    cement_share_pct: 4.36,
    flaring_share_pct: 1.18
  },
  {
    country: 'China',
    iso3: 'CHN',
    year: 2019,
    co2_total_mt: 10741,
    coal_share_pct: 70.23,
    oil_share_pct: 14.52,
    gas_share_pct: 5.87,
    cement_share_pct: 7.7,
    flaring_share_pct: 0.04
  },
  {
    country: 'USA',
    iso3: 'USA',
    year: 2019,
    co2_total_mt: 5259.14,
    coal_share_pct: 20.36,
    oil_share_pct: 44.85,
    gas_share_pct: 31.83,
    cement_share_pct: 0.78,
    flaring_share_pct: 1.68
  },
  {
    country: 'India',
    iso3: 'IND',
    year: 2019,
    co2_total_mt: 2626.46,
    coal_share_pct: 63.88,
    oil_share_pct: 25.66,
    gas_share_pct: 4.9,
    cement_share_pct: 5.47,
    flaring_share_pct: 0.09
  },
  {
    country: 'Russia',
    iso3: 'RUS',
    year: 2019,
    co2_total_mt: 1692.36,
    coal_share_pct: 23.07,
    oil_share_pct: 23.54,
    gas_share_pct: 47.5,
    cement_share_pct: 1.2,
    flaring_share_pct: 3.7
  },
  {
    country: 'International Transport',
    iso3: 'XIT',
    year: 2019,
    co2_total_mt: 1249.56,
    coal_share_pct: 0,
    oil_share_pct: 100,
    gas_share_pct: 0,
    cement_share_pct: 0,
    flaring_share_pct: 0
  },
  {
    country: 'Japan',
    iso3: 'JPN',
    year: 2019,
    co2_total_mt: 1106.02,
    coal_share_pct: 39.08,
    oil_share_pct: 37.6,
    gas_share_pct: 20.27,
    cement_share_pct: 2.29,
    flaring_share_pct: 0.03
  },
  {
    country: 'Germany',
    iso3: 'DEU',
    year: 2019,
    co2_total_mt: 707.15,
    coal_share_pct: 33.95,
    oil_share_pct: 38.31,
    gas_share_pct: 24.39,
    cement_share_pct: 1.88,
    flaring_share_pct: 0.29
  },
  {
    country: 'Iran',
    iso3: 'IRN',
    year: 2019,
    co2_total_mt: 702.96,
    coal_share_pct: 0.53,
    oil_share_pct: 32.63,
    gas_share_pct: 60.17,
    cement_share_pct: 2.97,
    flaring_share_pct: 3.69
  },
  {
    country: 'Indonesia',
    iso3: 'IDN',
    year: 2019,
    co2_total_mt: 659.44,
    coal_share_pct: 47.83,
    oil_share_pct: 33.69,
    gas_share_pct: 13.33,
    cement_share_pct: 4.57,
    flaring_share_pct: 0.57
  },
  {
    country: 'Saudi Arabia',
    iso3: 'SAU',
    year: 2019,
    co2_total_mt: 656.48,
    coal_share_pct: 0,
    oil_share_pct: 56.66,
    gas_share_pct: 38.99,
    cement_share_pct: 3.75,
    flaring_share_pct: 0.6
  },
  {
    country: 'South Korea',
    iso3: 'KOR',
    year: 2019,
    co2_total_mt: 646.1,
    coal_share_pct: 49.78,
    oil_share_pct: 27.21,
    gas_share_pct: 17.58,
    cement_share_pct: 3.86,
    flaring_share_pct: 0
  },
  {
    country: 'Canada',
    iso3: 'CAN',
    year: 2019,
    co2_total_mt: 584.71,
    coal_share_pct: 9.98,
    oil_share_pct: 46.06,
    gas_share_pct: 39.67,
    cement_share_pct: 1.22,
    flaring_share_pct: 2.71
  },
  {
    country: 'Brazil',
    iso3: 'BRA',
    year: 2019,
    co2_total_mt: 475.1,
    coal_share_pct: 13.03,
    oil_share_pct: 63.64,
    gas_share_pct: 14.13,
    cement_share_pct: 4.18,
    flaring_share_pct: 3.68
  },
  {
    country: 'Mexico',
    iso3: 'MEX',
    year: 2019,
    co2_total_mt: 472.19,
    coal_share_pct: 9.59,
    oil_share_pct: 51.23,
    gas_share_pct: 33.27,
    cement_share_pct: 4.13,
    flaring_share_pct: 1.79
  },
  {
    country: 'South Africa',
    iso3: 'ZAF',
    year: 2019,
    co2_total_mt: 466.92,
    coal_share_pct: 84.46,
    oil_share_pct: 12.42,
    gas_share_pct: 1.95,
    cement_share_pct: 1.17,
    flaring_share_pct: 0.01
  },
  {
    country: 'Australia',
    iso3: 'AUS',
    year: 2019,
    co2_total_mt: 416.36,
    coal_share_pct: 39.5,
    oil_share_pct: 34.37,
    gas_share_pct: 19.62,
    cement_share_pct: 0.73,
    flaring_share_pct: 4.85
  },
  {
    country: 'Turkey',
    iso3: 'TUR',
    year: 2019,
    co2_total_mt: 401.72,
    coal_share_pct: 41.07,
    oil_share_pct: 28.59,
    gas_share_pct: 20.7,
    cement_share_pct: 8.05,
    flaring_share_pct: 0.05
  },
  {
    country: 'United Kingdom',
    iso3: 'GBR',
    year: 2019,
    co2_total_mt: 364.75,
    coal_share_pct: 6.72,
    oil_share_pct: 46.33,
    gas_share_pct: 43.68,
    cement_share_pct: 1.22,
    flaring_share_pct: 1.17
  },
  {
    country: 'Viet Nam',
    iso3: 'VNM',
    year: 2019,
    co2_total_mt: 341,
    coal_share_pct: 56.14,
    oil_share_pct: 22.38,
    gas_share_pct: 5.54,
    cement_share_pct: 15.5,
    flaring_share_pct: 0.43
  }
]
```

---

## [27] Kategorie 5: Historicke Trendy CO2 A WDI / Dotaz 3

**Stav:** OK

```text
[
  {
    country_year_rows: 2260,
    decade: 1950,
    avg_country_year_total_mt: 64.7,
    max_country_year_emission_mt: 8856.22
  },
  {
    country_year_rows: 2260,
    decade: 1960,
    avg_country_year_total_mt: 98.9,
    max_country_year_emission_mt: 13767.4
  },
  {
    country_year_rows: 2260,
    decade: 1970,
    avg_country_year_total_mt: 153.07,
    max_country_year_emission_mt: 19618.46
  },
  {
    country_year_rows: 2260,
    decade: 1980,
    avg_country_year_total_mt: 179.5,
    max_country_year_emission_mt: 22410.4
  },
  {
    country_year_rows: 2260,
    decade: 1990,
    avg_country_year_total_mt: 207.96,
    max_country_year_emission_mt: 24732.39
  },
  {
    country_year_rows: 2260,
    decade: 2000,
    avg_country_year_total_mt: 255.8,
    max_country_year_emission_mt: 32085.84
  },
  {
    country_year_rows: 2260,
    decade: 2010,
    avg_country_year_total_mt: 314.02,
    max_country_year_emission_mt: 37082.56
  },
  {
    country_year_rows: 452,
    decade: 2020,
    avg_country_year_total_mt: 320.3,
    max_country_year_emission_mt: 37123.85
  }
]
```

---

## [28] Kategorie 5: Historicke Trendy CO2 A WDI / Dotaz 4

**Stav:** OK

```text
[
  {
    iso3: 'KWT',
    country: 'Kuwait',
    internet_2000: 6.73,
    internet_2017: 98,
    internet_change_pct_points: 91.27
  },
  {
    iso3: 'QAT',
    country: 'Qatar',
    internet_2000: 4.86,
    internet_2017: 95.94,
    internet_change_pct_points: 91.08
  },
  {
    iso3: 'BHR',
    country: 'Bahrain',
    internet_2000: 6.15,
    internet_2017: 95.88,
    internet_change_pct_points: 89.72
  },
  {
    iso3: 'AND',
    country: 'Andorra',
    internet_2000: 10.54,
    internet_2017: 98.87,
    internet_change_pct_points: 88.33
  },
  {
    iso3: 'BRN',
    country: 'Brunei Darussalam',
    internet_2000: 9,
    internet_2017: 94.87,
    internet_change_pct_points: 85.87
  },
  {
    iso3: 'ABW',
    country: 'Aruba',
    internet_2000: 15.44,
    internet_2017: 97.17,
    internet_change_pct_points: 81.73
  },
  {
    iso3: 'SAU',
    country: 'Saudi Arabia',
    internet_2000: 2.21,
    internet_2017: 82.12,
    internet_change_pct_points: 79.91
  },
  {
    iso3: 'AZE',
    country: 'Azerbaijan',
    internet_2000: 0.15,
    internet_2017: 79,
    internet_change_pct_points: 78.85
  },
  {
    iso3: 'BRB',
    country: 'Barbados',
    internet_2000: 3.97,
    internet_2017: 81.76,
    internet_change_pct_points: 77.79
  },
  {
    iso3: 'BHS',
    country: 'Bahamas, The',
    internet_2000: 8,
    internet_2017: 85,
    internet_change_pct_points: 77
  },
  {
    iso3: 'OMN',
    country: 'Oman',
    internet_2000: 3.52,
    internet_2017: 80.19,
    internet_change_pct_points: 76.67
  },
  {
    iso3: 'KAZ',
    country: 'Kazakhstan',
    internet_2000: 0.67,
    internet_2017: 76.43,
    internet_change_pct_points: 75.76
  },
  {
    iso3: 'LVA',
    country: 'Latvia',
    internet_2000: 6.32,
    internet_2017: 81.32,
    internet_change_pct_points: 75
  },
  {
    iso3: 'LUX',
    country: 'Luxembourg',
    internet_2000: 22.89,
    internet_2017: 97.83,
    internet_change_pct_points: 74.94
  },
  {
    iso3: 'KNA',
    country: 'St. Kitts and Nevis',
    internet_2000: 5.86,
    internet_2017: 80.71,
    internet_change_pct_points: 74.85
  },
  {
    iso3: 'MDA',
    country: 'Moldova',
    internet_2000: 1.28,
    internet_2017: 76.12,
    internet_change_pct_points: 74.84
  },
  {
    iso3: 'RUS',
    country: 'Russian Federation',
    internet_2000: 1.98,
    internet_2017: 76.01,
    internet_change_pct_points: 74.03
  },
  {
    iso3: 'MKD',
    country: 'North Macedonia',
    internet_2000: 2.49,
    internet_2017: 76.31,
    internet_change_pct_points: 73.83
  },
  {
    iso3: 'BLR',
    country: 'Belarus',
    internet_2000: 1.86,
    internet_2017: 74.44,
    internet_change_pct_points: 72.58
  },
  {
    iso3: 'SVK',
    country: 'Slovak Republic',
    internet_2000: 9.43,
    internet_2017: 81.63,
    internet_change_pct_points: 72.2
  }
]
```

---

## [29] Kategorie 5: Historicke Trendy CO2 A WDI / Dotaz 5

**Stav:** OK

```text
[
  {
    iso3: 'MDV',
    country: 'Maldives',
    life_1960: 37.4,
    life_2017: 77.65,
    life_gain_years: 40.25
  },
  {
    iso3: 'BTN',
    country: 'Bhutan',
    life_1960: 34.53,
    life_2017: 70.56,
    life_gain_years: 36.04
  },
  {
    iso3: 'TLS',
    country: 'Timor-Leste',
    life_1960: 33.73,
    life_2017: 69.2,
    life_gain_years: 35.47
  },
  {
    iso3: 'NPL',
    country: 'Nepal',
    life_1960: 35.2,
    life_2017: 70.6,
    life_gain_years: 35.41
  },
  {
    iso3: 'OMN',
    country: 'Oman',
    life_1960: 42.67,
    life_2017: 77.26,
    life_gain_years: 34.59
  },
  {
    iso3: 'TUN',
    country: 'Tunisia',
    life_1960: 42.02,
    life_2017: 75.94,
    life_gain_years: 33.92
  },
  {
    iso3: 'CHN',
    country: 'China',
    life_1960: 43.73,
    life_2017: 76.41,
    life_gain_years: 32.68
  },
  {
    iso3: 'AFG',
    country: 'Afghanistan',
    life_1960: 32.29,
    life_2017: 64.05,
    life_gain_years: 31.75
  },
  {
    iso3: 'IRN',
    country: 'Iran, Islamic Rep.',
    life_1960: 44.95,
    life_2017: 76.15,
    life_gain_years: 31.21
  },
  {
    iso3: 'YEM',
    country: 'Yemen, Rep.',
    life_1960: 34.36,
    life_2017: 65.16,
    life_gain_years: 30.8
  },
  {
    iso3: 'TUR',
    country: 'Turkey',
    life_1960: 45.37,
    life_2017: 76.01,
    life_gain_years: 30.64
  },
  {
    iso3: 'MLI',
    country: 'Mali',
    life_1960: 28.2,
    life_2017: 58.46,
    life_gain_years: 30.26
  },
  {
    iso3: 'DZA',
    country: 'Algeria',
    life_1960: 46.14,
    life_2017: 76.29,
    life_gain_years: 30.16
  },
  {
    iso3: 'KOR',
    country: 'Korea, Rep.',
    life_1960: 53,
    life_2017: 82.63,
    life_gain_years: 29.63
  },
  {
    iso3: 'LBY',
    country: 'Libya',
    life_1960: 42.61,
    life_2017: 72.11,
    life_gain_years: 29.5
  },
  {
    iso3: 'GMB',
    country: 'Gambia, The',
    life_1960: 32.03,
    life_2017: 61.42,
    life_gain_years: 29.39
  },
  {
    iso3: 'SEN',
    country: 'Senegal',
    life_1960: 38.22,
    life_2017: 67.48,
    life_gain_years: 29.25
  },
  {
    iso3: 'SAU',
    country: 'Saudi Arabia',
    life_1960: 45.64,
    life_2017: 74.72,
    life_gain_years: 29.08
  },
  {
    iso3: 'TEA',
    country: 'East Asia & Pacific (IDA & IBRD countries)',
    life_1960: 45.65,
    life_2017: 74.68,
    life_gain_years: 29.03
  },
  {
    iso3: 'EAP',
    country: 'East Asia & Pacific (excluding high income)',
    life_1960: 45.72,
    life_2017: 74.65,
    life_gain_years: 28.92
  }
]
```

---

## [30] Kategorie 5: Historicke Trendy CO2 A WDI / Dotaz 6

**Stav:** OK

```text
[
  {
    iso3: 'HKG',
    country: 'Hong Kong SAR, China',
    year: 2015,
    trade_pct_gdp: 389.41,
    unemployment_pct: 3.32
  },
  {
    iso3: 'HKG',
    country: 'Hong Kong SAR, China',
    year: 2017,
    trade_pct_gdp: 375.09,
    unemployment_pct: 3.09
  },
  {
    iso3: 'HKG',
    country: 'Hong Kong SAR, China',
    year: 2016,
    trade_pct_gdp: 371.71,
    unemployment_pct: 3.39
  },
  {
    iso3: 'SGP',
    country: 'Singapore',
    year: 2015,
    trade_pct_gdp: 329.05,
    unemployment_pct: 3.79
  },
  {
    iso3: 'SGP',
    country: 'Singapore',
    year: 2017,
    trade_pct_gdp: 322.43,
    unemployment_pct: 3.91
  },
  {
    iso3: 'SGP',
    country: 'Singapore',
    year: 2016,
    trade_pct_gdp: 310.26,
    unemployment_pct: 4.08
  },
  {
    iso3: 'MLT',
    country: 'Malta',
    year: 2016,
    trade_pct_gdp: 264.62,
    unemployment_pct: 4.7
  },
  {
    iso3: 'MLT',
    country: 'Malta',
    year: 2017,
    trade_pct_gdp: 249.2,
    unemployment_pct: 4.57
  },
  {
    iso3: 'VNM',
    country: 'Vietnam',
    year: 2017,
    trade_pct_gdp: 200.38,
    unemployment_pct: 1.89
  },
  {
    iso3: 'VNM',
    country: 'Vietnam',
    year: 2016,
    trade_pct_gdp: 184.69,
    unemployment_pct: 1.85
  },
  {
    iso3: 'VNM',
    country: 'Vietnam',
    year: 2015,
    trade_pct_gdp: 178.77,
    unemployment_pct: 1.86
  },
  {
    iso3: 'ARE',
    country: 'United Arab Emirates',
    year: 2016,
    trade_pct_gdp: 176.75,
    unemployment_pct: 1.64
  },
  {
    iso3: 'ARE',
    country: 'United Arab Emirates',
    year: 2015,
    trade_pct_gdp: 175.22,
    unemployment_pct: 1.84
  },
  {
    iso3: 'ARE',
    country: 'United Arab Emirates',
    year: 2017,
    trade_pct_gdp: 172.81,
    unemployment_pct: 2.46
  },
  {
    iso3: 'HUN',
    country: 'Hungary',
    year: 2017,
    trade_pct_gdp: 168.93,
    unemployment_pct: 4.16
  },
  {
    iso3: 'NLD',
    country: 'Netherlands',
    year: 2017,
    trade_pct_gdp: 155.17,
    unemployment_pct: 4.84
  },
  {
    iso3: 'BHR',
    country: 'Bahrain',
    year: 2015,
    trade_pct_gdp: 154.07,
    unemployment_pct: 1.08
  },
  {
    iso3: 'CZE',
    country: 'Czech Republic',
    year: 2017,
    trade_pct_gdp: 151.93,
    unemployment_pct: 2.89
  },
  {
    iso3: 'CZE',
    country: 'Czech Republic',
    year: 2016,
    trade_pct_gdp: 151.39,
    unemployment_pct: 3.95
  },
  {
    iso3: 'GIN',
    country: 'Guinea',
    year: 2017,
    trade_pct_gdp: 146.77,
    unemployment_pct: 3.57
  }
]
```
