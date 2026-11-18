# National SCANFI v2 Area Weights

Generated: 2026-11-18T16:23:53Z  
Runtime: 180.318 s  
Product: SCANFI v2 2025 (20260119), 30 m, aggregated to 990 m blocks.

## Method

Forest area is the count of NFI land-cover classes 5 (treed broadleaf), 6 (treed conifer), and 7 (treed mixed) multiplied by 0.09 ha per 30 m pixel. Species area is allocated by normalising the ten SCANFI v2 species crown-closure layers within each 990 m block, then multiplying by block forest area. The raw crown-closure area is retained separately because SCANFI v2 species layers are absolute crown closure, not relative composition.

## National totals

- Forest area: **422,475,761 ha**
- Allocated species area: **422,475,762 ha**
- Maximum relative area residual: 6.169e-08
- Species-sum > 100% pixels: 0 (0.0 ha quarantined)
- Zero-species forest pixels: 0 (0.0 ha)
- Coastline/lake gap-filled forest area: 12,545,096.8 ha
- Unassigned forest area after nearest-unit fill: 0.0 ha

NFI Table 4.0 national forest-land benchmark: 369,019,352 ha; SCANFI treed area is 1.145x the benchmark.

## Forest area by province/territory

| Province | Forest area (ha) |
|---|---:|
| QC | 81,663,538 |
| ON | 68,517,060 |
| BC | 66,607,737 |
| NT | 43,460,564 |
| AB | 38,345,566 |
| MB | 33,753,910 |
| SK | 26,160,931 |
| YT | 25,905,743 |
| NL | 23,531,836 |
| NB | 6,692,498 |
| NS | 4,727,697 |
| NU | 2,834,208 |
| PE | 274,472 |

## Allocated area by RSYC target

| RSYC species | Area (ha) |
|---|---:|
| PICE.MAR | 153,682,121 |
| BROADLEAF | 82,649,860 |
| PINU.BAN | 39,126,191 |
| PICE.GLA | 39,033,903 |
| CONIFEROUS | 34,616,820 |
| LARI.LAR | 27,150,318 |
| PINU.CON | 21,195,759 |
| ABIE.BAL | 17,465,105 |
| PSEU.MEN | 5,293,793 |
| PINU.RES | 1,025,102 |
| PINU.STR | 1,025,102 |
| PINU.PON | 211,686 |

## Forest area by ecoprovince

| Ecoprovince | Ecozone | Forest area (ha) |
|---|---|---:|
| Mid-Boreal Shield | Boreal Shield East | 38,737,573 |
| Western Boreal Shield | Boreal Shield West | 36,663,767 |
| Central Boreal Plains | Boreal Plains | 35,127,120 |
| Southern Boreal Shield | Boreal Shield East | 31,245,367 |
| Eastern Boreal Shield | Boreal Shield East | 26,850,478 |
| Western Taiga Shield | Taiga Shield West | 23,080,875 |
| Great Bear Lowlands | Taiga Plains | 19,803,498 |
| Eastern Taiga | Taiga Shield East | 17,442,986 |
| Northern Boreal Cordillera | Boreal Cordillera | 17,133,238 |
| Hudson-James Lowlands | Hudson Plains | 16,344,831 |
| Hay-Slave Lowlands | Taiga Plains | 15,585,627 |
| Labrador Uplands | Taiga Shield East | 13,705,783 |
| Columbia Montane Cordillera | Montane Cordillera | 12,767,584 |
| Southern Coastal Mountains | Pacific Maritime | 11,285,864 |
| Northern Montane Cordillera | Montane Cordillera | 10,899,094 |
| Boreal Foothills | Boreal Plains | 10,859,591 |
| Appalachian-Acadian Highlands | Atlantic Maritime | 9,199,270 |
| Southern Boreal Cordillera | Boreal Cordillera | 8,720,269 |
| Central Montane Cordillera | Montane Cordillera | 8,420,236 |
| Newfoundland | Boreal Shield East | 7,012,730 |
| Eastern Boreal Plains | Boreal Plains | 6,520,075 |
| Fundy Uplands | Atlantic Maritime | 6,110,545 |
| Mackenzie Foothills | Taiga Plains | 5,503,361 |
| Lake of the Woods | Boreal Shield West | 5,375,714 |
| Whale River Lowland | Taiga Shield East | 4,948,332 |
| Mackenzie-Selwyn Mountains | Taiga Cordillera | 4,496,971 |
| Southern Montane Cordillera | Montane Cordillera | 4,466,627 |
| Ogilvie Mountains | Taiga Cordillera | 3,014,231 |
| Northumberland Lowlands | Atlantic Maritime | 2,877,962 |
| Western Boreal Cordillera | Boreal Cordillera | 2,803,976 |
| Hudson Bay Coastal Plains | Hudson Plains | 2,057,538 |
| Georgia Depression | Pacific Maritime | 1,524,063 |
| Northern Coastal Mountains | Pacific Maritime | 694,605 |
| Old Crow-Eagle Plains | Taiga Cordillera | 625,187 |
| Northern Yukon Mountains | Taiga Cordillera | 345,911 |
| Wrangel Mountains | Boreal Cordillera | 224,882 |

## Crosswalk

```
 scanfi_class_code    scanfi_class  is_forest rsyc_species  allocation_fraction                                         mapping_basis confidence                                                                   notes
                 1          bryoid      False                               0.0                                      non_forest_class       high                                          Excluded from the forest mask.
                 2           herbs      False                               0.0                                      non_forest_class       high                                          Excluded from the forest mask.
                 3            rock      False                               0.0                                      non_forest_class       high                                          Excluded from the forest mask.
                 4           shrub      False                               0.0                                      non_forest_class       high                                          Excluded from the forest mask.
                 8           water      False                               0.0                                      non_forest_class       high                                          Excluded from the forest mask.
              <NA>     blackSpruce       True     PICE.MAR                  1.0           scanfi_blackSpruce_crown_closure_normalised       high                                                    Exact species layer.
              <NA>       balsamFir       True     ABIE.BAL                  1.0             scanfi_balsamFir_crown_closure_normalised       high                                                    Exact species layer.
              <NA>        jackPine       True     PINU.BAN                  1.0              scanfi_jackPine_crown_closure_normalised       high                                                    Exact species layer.
              <NA>   lodgepolePine       True     PINU.CON                  1.0         scanfi_lodgepolePine_crown_closure_normalised       high                                                    Exact species layer.
              <NA>   ponderosaPine       True     PINU.PON                  1.0         scanfi_ponderosaPine_crown_closure_normalised       high                                                    Exact species layer.
              <NA>      douglasFir       True     PSEU.MEN                  1.0            scanfi_douglasFir_crown_closure_normalised       high                                                    Exact species layer.
              <NA>        tamarack       True     LARI.LAR                  1.0              scanfi_tamarack_crown_closure_normalised       high                                                    Exact species layer.
              <NA>    whiteRedPine       True     PINU.STR                  0.5 scanfi_whiteRedPine_composite_split_PINU.STR_PINU.RES        low Composite white+red pine split 50/50; PINU.RES receives the other half.
              <NA>    whiteRedPine       True     PINU.RES                  0.5 scanfi_whiteRedPine_composite_split_PINU.STR_PINU.RES        low Composite white+red pine split 50/50; PINU.STR receives the other half.
              <NA>       broadleaf       True    BROADLEAF                  1.0               scanfi_broadleaf_aggregate_to_BROADLEAF     medium                 Aggregate broadleaf class; no species-level resolution.
              <NA> otherConiferous       True     PICE.GLA                  1.0       scanfi_otherConiferous_boreal_proxy_to_PICE.GLA     medium                               Boreal ecozones only; white-spruce proxy.
              <NA> otherConiferous       True   CONIFEROUS                  1.0          scanfi_otherConiferous_generic_to_CONIFEROUS     medium                            Non-boreal ecozones; generic conifer target.
```

## Caveats

- SCANFI is a prediction surface, not a census or provincial inventory.
- Species area is composition-weighted forest area, not species-specific volume.
- White/red pine is split 50/50 between PINU.STR and PINU.RES.
- Broadleaf is an aggregate class; other conifer is a white-spruce proxy in boreal ecozones and generic CONIFEROUS elsewhere.
- Province attribution uses simplified geoBoundaries ADM1 polygons; treat as attribution, not legal boundaries.
- No MGM yield curves are joined in this product.
