# National bucking architecture — tool references

Metadata-only register. No upstream code was cloned, copied, or vendored into
this repository. Each entry records the canonical repository, licence,
citation, input/output contract, and intended role in the national bucking
architecture. Verify licences and versions again before linking or
redistributing any component.

## Summary

| Component | Repository | Licence | Primary role |
|---|---|---|---|
| BuckR | https://github.com/CWFC-CCFB/BuckR | LGPL-2.1 | Dynamic-programming tree-bucking optimizer and price/grade feasibility reference |
| FSvolLib | https://github.com/USDAForestService/FSvolLib | CC0-1.0 | USFS taper/volume/biomass and Scribner board-foot reference implementation |
| biomasscan | https://github.com/tesera/biomasscan | MIT | Canadian national biomass allometry by component (Lambert/Ung equations) |
| CFSForestTools | https://github.com/CWFC-CCFB/CFSForestTools | LGPL-3.0 | Canadian stem taper (Schneider 2013), merchantable volume, MERIS/Petro log-grade matrices |
| FVS Canadian variants | https://github.com/USDAForestService/ForestVegetationSimulator | Public domain (U.S. Government) | Growth/yield projection plus BC Kozak and Ontario Zakrzewski/Honer/R9 Clark volume routines |

## 1. BuckR

- **Repository**: https://github.com/CWFC-CCFB/BuckR
- **Licence**: GNU Lesser General Public License v2.1 (LGPL-2.1). Copyright
  2025 His Majesty the King in Right of Canada.
- **Citation**: Bennemann, C.; Lussier, J.-M.; Labelle, E.R. 2025.
  An Open-Source Tree Bucking Optimizer Based on Dynamic Programming.
  *Forests* 16(5):780. https://doi.org/10.3390/f16050780
- **Artifact form**: R Markdown script (`BuckR-version-250321.Rmd`) plus a
  knitted Word document and sample tables. There is no installable package API.

### Input contract

- A working directory with `IN/` and `OUT/` subdirectories.
- A price list (CSV in the example) with one row per product:
  `SP` (species), `ProductID` (unique product ID), `L` (log length, cm),
  `SEDmin` and `SEDmax` (accepted small-end-diameter range, mm), and `VAM`
  (value per m3). Prices may be relative rather than market values.
- Stem-profile data (Excel sheet `tree` in the example) with `TreeID`, `SP`,
  `LG` (position from ground, cm), and `DG` (diameter at that position, mm),
  following the StanForD 2010 convention. The example uses 50 cm taper
  increments.
- Every species in the stem profiles must have price-list coverage; missing
  products are a hard error in the reference script.

### Output contract

- Optimal cut positions along each stem and the resulting log sequence.
- Assigned product/grade per log and the per-tree optimized value.
- Intermediate tables for merchantable length, log permutations, and product
  volumes. The optimizer maximizes total log value using dynamic programming
  (Dykstra 1984); a classification tree converts the price list into a
  product-selection model.

### Role in the architecture

Reference implementation for the **optimization core**: given a stem profile
and a price/grade matrix, choose cut positions that maximize value. Useful for
validating the national bucking DP formulation, price-matrix edge cases, and
small-tree worked examples. It is not a growth model, does not predict stem
profiles, and is not a production Canadian grade-matrix service.

## 2. FSvolLib

- **Repository**: https://github.com/USDAForestService/FSvolLib
- **Licence**: CC0-1.0. The repository `LICENCE.md` states the work is in the
  U.S. public domain and waives copyright worldwide under CC0 1.0. GitHub's
  licence detector reports `NOASSERTION`, so the file, not the API badge, is
  authoritative.
- **Citation**: USDA Forest Service, Forest Service Volume Estimation Library
  (FSvolLib), https://github.com/USDAForestService/FSvolLib. No journal article
  is required by the repository.
- **Artifact form**: C++ library with CMake presets, a C# interop layer, and
  WASM/Android build paths.

### Input contract

- Tree measurements: species, DBH, total height, and optionally crown/taper
  measurements, plus merchantability rules and volume-calculation options.
- The library exposes taper models and volume calculators, including Clark R8
  and R9 profile models, Flewelling, Czaplewski, DeMars, Wensel-Olson,
  Behre, and national-scale volume/biomass models.
- Board-foot output uses Scribner (including International 1/4-inch handling
  in the volume calculators).

### Output contract

- Gross and merchantable cubic volume, board-foot volume (Scribner), and
  biomass/component weights, depending on the selected calculator and
  merchantability rules.
- Per-tree output records plus calculation diagnostics/error information.

### Role in the architecture

USFS reference for **taper and volume calculation**, especially R9 Clark
profile volume and Scribner board-foot conversion. Use it to cross-check the
Ontario FVS R9 Clark path and to test merchantability-rule handling. It is
US-focused: it does not provide Canadian log-grade matrices or Canadian
species/grade prices, so it is a calculation reference rather than the
national product classifier.

## 3. biomasscan

- **Repository**: https://github.com/tesera/biomasscan
- **Licence**: MIT. Copyright (c) 2023 Tesera Systems Inc.
- **Citations**:
  - Lambert, M.-C., Ung, C.-H., Raulier, F. 2005. Canadian national tree
    aboveground biomass equations. *Canadian Journal of Forest Research*
    35: 1996–2018. https://doi.org/10.1139/x05-112
  - Ung, C.-H., Bernier, P., Guo, X.-J. 2008. Canadian national biomass
    equations: new parameter estimates that include British Columbia data.
    *Canadian Journal of Forest Research* 38: 1123–1132.
    https://doi.org/10.1139/x07-224
- **Artifact form**: R package with tree-level and plot-level functions.

### Input contract

- A tree list with species (common names accepted by the package matcher),
  diameter at breast height (cm), and height (m). The single-tree function
  takes `height`, `diameter`, and `species`; the table function takes column
  names for species, diameter, and height.
- Species names are matched to the package's equation table; unsupported
  species return `NA` rather than silently extrapolating.

### Output contract

- Biomass in kilograms for `Bark`, `Branches`, `Foliage`, `Wood`, and `Total`,
  either long or wide format.
- The equations reproduce Natural Resources Canada's online biomass calculator
  (Lambert/Ung national equations).

### Role in the architecture

Reference for **component biomass allometry** (crown fractions, bark, wood)
when converting tree lists or harvested stems to biomass. It does not perform
bucking, merchantable-volume segmentation, or log grading. Use it to validate
component fractions and total biomass, not to choose cut positions.

## 4. CFSForestTools

- **Repository**: https://github.com/CWFC-CCFB/CFSForestTools
- **Licence**: GNU Lesser General Public License v3.0 (LGPL-3.0). Copyright
  2009–2019 Gouvernement du Québec — Rouge Épicéa; 2019–2024 His Majesty the
  King in Right of Canada. Dependencies include `repicea-simulation` and
  `biosimclient` (both LGPL-3.0).
- **Citation for the taper model**: Fortin, M., Schneider, R., Saucier, J.-P.
  2013. Volume and Error Variance Estimation Using Integrated Stem Taper
  Models. *Forest Science* 59(3): 345–358.
  https://doi.org/10.5849/forsci.11-146
- **Artifact form**: Java library. The `schneider2013` stem-taper module and
  the Quebec MERIS/Petro tree loggers are implemented in source.

### Input contract

- Tree-level records with species, DBH (cm), height (m), and, where required by
  a module, age, crown ratio, or stem-quality variables.
- Stand/plot records for modules that use plot random effects.
- The Schneider 2013 taper module predicts under-bark diameter at requested
  heights; it supports species-specific parameter sets for the Quebec species
  groups (`bop`, `epb`, `epn`, `epr`, `peg`, `pet`, `pig`, `sab`, `tho`) and
  first/second-order variance approximations.
- The MERIS tree logger consumes a MERIS product matrix; the Petro grade
  predictor consumes species, DBH, height, and quality/vigor variables needed
  by the Quebec grade models.

### Output contract

- Taper profiles: under-bark diameter at specified heights and stem-section
  volumes.
- Merchantable volume (`Fortin2007`) and Honer 1983 volume where selected.
- Log-grade outputs: MERIS product categories and Petro under-bark volumes by
  log grade, plus the corresponding grade matrices/parameters.

### Role in the architecture

The closest Canadian reference for **taper + grade matrices**. It supplies:
- the Schneider 2013 taper formulation and parameter sets for Quebec species;
- MERIS and Petro log-grade product matrices;
- merchantable-volume and Honer volume calculators.

Use it as the primary cross-check for the national bucking module's taper and
grade-classification stages. LGPL-3.0 obligations apply if the library is
linked or redistributed; keep it as an external reference/service unless a
compliance decision is made.

## 5. FVS Canadian variants

- **Repository**: https://github.com/USDAForestService/ForestVegetationSimulator
- **Licence**: Public domain in the United States (U.S. Government work);
  `license.txt` releases the software without conditions and notes that
  embedded third-party components retain their own licences. The repository is
  not a uniform open-source licence grant outside the U.S.; confirm
  jurisdiction-specific reuse before redistribution.
- **Citation**: USDA Forest Service, Forest Vegetation Simulator (FVS),
  https://github.com/USDAForestService/ForestVegetationSimulator. See the FVS
  documentation and variant guides for model-specific citations.
- **Artifact form**: Fortran/C++ growth-and-yield engine with variant-specific
  source trees, including `canada/bc/` and `canada/on/`.

### Input contract

- An FVS keyword file controlling simulation length, output, treatments, and
  volume/taper method.
- A tree list with species, DBH, total height, crown ratio, damage codes, and
  stand/site variables required by the variant.
- Variant selection (BC or Ontario) determines the available species codes,
  taper/volume routines, and growth equations.

### Output contract

- Projected tree lists and stand attributes over time (growth, mortality,
  regeneration, ingrowth).
- Volume and taper outputs: total/merchantable cubic volume, board-foot volume,
  and variant-specific taper/log volumes.
- Fire/fuel, insect/pathogen, and treatment outputs where the relevant
  extensions are enabled.

### Canadian routines relevant to bucking

- **BC variant**: `CFVOL` computes total cubic-foot volume using several
  methods; `METHC = 4` selects Kozak taper-function volume. The source comment
  notes a planned update to the Kozak 2002 refit and BEC-zone log volumes. The
  BC source tree also contains `VOLS`, `CFVOL`, and taper-related routines.
- **Ontario variant**: `VOLONT` implements the Ontario **Zakrzewski**
  (`ZAKVOL`, `ZAKHT`) and **Honer** volume equations. `VARVOL` calls
  `R9CLARK` for the National Cruise System (`NATCRS`) path, providing the R9
  Clark profile volume used in Ontario.

### Role in the architecture

Reference for **growth projection and Canadian volume/taper routines**. The BC
Kozak and Ontario Zakrzewski/Honer/R9 Clark routines are directly relevant to
national bucking because they encode jurisdiction-specific merchantability and
taper conventions. Use FVS outputs as growth/yield and volume cross-checks,
and use the public-domain routines as equation references. Do not vendor the
Fortran source; integrate through an external runtime or a clean-room
reimplementation with tests against FVS outputs.

## Architecture crosswalk

| National bucking stage | Primary reference | Secondary reference |
|---|---|---|
| Stand/tree-list growth and yield | FVS Canadian variants | RSYC yield-curve benchmark (stand-level only) |
| Stem profile / taper | CFSForestTools `schneider2013` | FVS BC Kozak; FSvolLib Clark models |
| Merchantable volume | CFSForestTools Fortin 2007 / Honer 1983 | FVS BC `CFVOL`; FVS Ontario `VOLONT` |
| Log-grade / product matrix | CFSForestTools MERIS and Petro | BuckR price/grade list |
| Cut optimization | BuckR dynamic programming | — |
| Biomass components | biomasscan (Lambert/Ung) | FSvolLib biomass calculators |
| Board-foot conversion | FSvolLib Scribner | FVS variant board-foot outputs |

## Licence handling

- **LGPL-2.1 (BuckR)** and **LGPL-3.0 (CFSForestTools)**: dynamic linking or
  separate-process use is preferred; if distributed with modified library
  code, provide the corresponding source and notices. Do not copy source into
  the parent or data repository.
- **MIT (biomasscan)**: retain the copyright and permission notice if code is
  reused.
- **CC0-1.0 (FSvolLib)**: no attribution required, but retain provenance in
  methods documentation.
- **Public domain (FVS)**: U.S. Government work; retain the licence text and
  check third-party components before redistribution.

No upstream code or data payload is stored in `data/raw/national/bucking/`;
this file is the only artifact.
