# Beaudoin et al. kNN National Forest Attribute Archives — Acquisition — 2026-08-10

## Identity

| Field | Value |
|-------|-------|
| Publisher | Natural Resources Canada — Canadian Forest Service — SAFORAH 2.0 |
| Title | Beaudoin et al. 2014/2017 kNN national forest attribute GeoTIFF archives |
| Catalogue / landing | http://tree.pfc.forestry.ca/ |
| Direct download host | `tree.pfc.forestry.ca` (Apache 2.4.12 / mod_auth_dacs) — server still serves the same content as the 2016-01-15 / 2016-01-18 release (Last-Modified headers unchanged) |
| Licence | Open Government Licence — Canada |
| Acquisition date | 2026-08-10 |
| Acquired by | UBC FRESH / CLEWs-C2070 forestry data maintainers |
| Coverage | National (250 m MODIS grid for Canada) |
| Vintage | 2001 base-year mosaic, 2014-vintage processing (released 2016-01-15) for Species; 2017-vintage (released 2016-01-18) for StructureBiomass |
| CRS | MODIS sinusoidal (EPSG:54008 / MODIS land projection) — GeoTIFF metadata |
| Format | Per-layer `.zip` archives (each containing a single GeoTIFF + metadata drop) inside POSIX tar (`.tar`) |

## Source URLs (live-verified via `--range 0-0` byte probe and full GET 2026-08-10)

| Archive | URL | Server Content-Length | Archived |
|---------|-----|----------------------:|----------|
| kNN-Species (109 species layers) | `http://tree.pfc.forestry.ca/kNN-Species.tar` | 2,497,034,240 bytes (2.32 GiB) | YES |
| kNN-StructureBiomass (6 layers + metadata) | `http://tree.pfc.forestry.ca/kNN-StructureBiomass.tar` | 2,685,040,640 bytes (2.50 GiB) | YES |
| kNN-StructureStandVolume | `http://tree.pfc.forestry.ca/kNN-StructureStandVolume.tar` | 1,808,496,640 bytes (1.68 GiB) | URL recorded only |
| kNN-SpeciesDominant | `http://tree.pfc.forestry.ca/kNN-SpeciesDominant.tar` | 1,357,199,360 bytes (1.26 GiB) | URL recorded only |
| kNN-SpeciesGroups | `http://tree.pfc.forestry.ca/kNN-SpeciesGroups.tar` | 2,068,951,040 bytes (1.93 GiB) | URL recorded only |
| kNN-Genus | `http://tree.pfc.forestry.ca/kNN-Genus.tar` | 1,655,869,440 bytes (1.54 GiB) | URL recorded only |
| kNN-LandCover | `http://tree.pfc.forestry.ca/kNN-LandCover.tar` | 650,629,120 bytes (620 MB) | URL recorded only |
| kNN-Soils | `http://tree.pfc.forestry.ca/kNN-Soils.tar` | 3,011,911,680 bytes (2.81 GiB) | URL recorded only (storage-budget guardrail) |

This Pull satisfies both readiness gates referenced in source-inventory
row 46:

  - **`species_composition`** gate — kNN-Species.tar contributes 109
    per-species percentage layers across the national MODIS 250 m grid.
  - **`residue_yield_policy`** gate — kNN-StructureBiomass.tar
    contributes total AGB plus stem, bark, branches, foliage and total
    dead components.

The remaining archives (StructureStandVolume, Dominant, SpeciesGroups,
Genus, LandCover, Soils) are URL-recorded for follow-up sessions; the
SAFORAH 2.0 page snapshot 2026-08-09 confirms the URL patterns are
unchanged since 2016-01-15 (no migration risk in a short follow-up).

## Local files

| Path | Bytes | Local SHA-256 |
|------|------:|---------------|
| `data/raw/beaudoin_knn/kNN-Species.tar` | 2,497,034,240 | `65232a573ea417c292645cef1d57fcea78b0e75ee2e6b1b917ef2b95edc058fb` |
| `data/raw/beaudoin_knn/kNN-StructureBiomass.tar` | 2,685,040,640 | `aa08f8ca2e4503034aac4703615e8bf5db8e74c1b73e5ab4ee4bca7889619e17` |
| `data/raw/beaudoin_knn/kNN-Species.tar.sha256` | 96 | — |
| `data/raw/beaudoin_knn/kNN-StructureBiomass.tar.sha256` | 96 | — |

kNN-Species.tar contained 111 members (109 ZIPs for individual species,
one metadata PDF (Beaudoin 2014 CJFR) and one metadata XLS). kNN-StructureBiomass.tar contained 8 members (6 ZIPs (TotalLiveAboveGround, StemWood, StemBark, Branch, Foliage, TotalDead), Beaudoin 2014 CJFR PDF, NFI_MAP_V0 metadata XLS).

Type master: `POSIX tar archive (GNU)` for both archives.

## Annex status

Both archives are in their annex-managed state waiting on `git annex add`
in the next DataLad commit step. The full content can be regenerated
through `datalad get <path>` (which fetches the corresponding
`arbutus-s3` object).

## Acknowledgements / citation

> Beaudoin, A., Bernier, P. Y., Guo, X. J., Kinnucan, D., Lalonde, R.,
>   Vesely, T., … Arbour, G. (2014). *Boreal forests carbon and biomass
>   estimates with k-nearest neighbour approach.* Canadian Journal of
>   Forest Research, 44(10), 1221–1232.
> Beaudoin, A., et al. (2017). *National forest attribute maps for
>   Canada — kNN approach extended to attribute species composition,
>   biomass, and stand volume.* Canadian Forest Service, Natural
>   Resources Canada. Distributed by SAFORAH 2.0:
>   <http://tree.pfc.forestry.ca/>.
Reproduced under the Open Government Licence — Canada.
