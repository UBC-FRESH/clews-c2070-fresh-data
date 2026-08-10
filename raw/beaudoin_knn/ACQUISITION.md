# Beaudoin et al. kNN National Forest Attribute Archives — Acquisition — 2026-08-10 (batch 2 sync)

## Identity

| Field | Value |
|-------|-------|
| Publisher | Natural Resources Canada — Canadian Forest Service — SAFORAH 2.0 |
| Title | Beaudoin et al. 2014/2017 kNN national forest attribute GeoTIFF archives |
| Catalogue / landing | http://tree.pfc.forestry.ca/ |
| Direct download host | `tree.pfc.forestry.ca` (Apache 2.4.12 / mod_auth_dacs) — server still serves the same content as the 2016-01-15 / 2016-01-18 release (Last-Modified headers unchanged) |
| Licence | Open Government Licence — Canada |
| Acquisition date | 2026-08-10 (batches 1 and 2 same calendar day) |
| Acquired by | UBC FRESH / CLEWs-C2070 forestry data maintainers |
| Coverage | National (250 m MODIS grid for Canada) |
| Vintage | 2001 base-year mosaic; Species + StructureBiomass releases dated 2014 (Species) and 2017 (StructureBiomass), with 2016-01-15 / 2016-01-18 publication timestamps |
| CRS | MODIS sinusoidal (EPSG:54008 / MODIS land projection) — GeoTIFF metadata |
| Format | Per-layer `.zip` archives (each containing a single GeoTIFF + metadata drop) inside POSIX tar (`.tar`) |

## Inventory (batch 1 + batch 2 — full picture as of 2026-08-10)

| Archive | URL | Bytes (Content-Length) | Batch | Status |
|---------|-----|----------------------:|------|--------|
| kNN-Species (109 species layers) | `http://tree.pfc.forestry.ca/kNN-Species.tar` | 2,497,034,240 | 1 | Archived |
| kNN-StructureBiomass (6 layers + metadata) | `http://tree.pfc.forestry.ca/kNN-StructureBiomass.tar` | 2,685,040,640 | 1 | Archived |
| kNN-StructureStandVolume (5 layers + metadata) | `http://tree.pfc.forestry.ca/kNN-StructureStandVolume.tar` | 1,808,496,640 | 2 | Archived |
| kNN-SpeciesGroups (18 layer union groups + metadata) | `http://tree.pfc.forestry.ca/kNN-SpeciesGroups.tar` | 2,068,951,040 | 2 | Archived |
| kNN-SpeciesDominant (all/broadleaf/needleleaf x id/prc x byte/float + metadata) | `http://tree.pfc.forestry.ca/kNN-SpeciesDominant.tar` | 1,357,199,360 | 2 | Archived |
| kNN-Genus (34 genus aggregations + metadata) | `http://tree.pfc.forestry.ca/kNN-Genus.tar` | 1,655,869,440 | 2 | Archived |
| kNN-LandCover (NonVeg / Veg / VegNonTreed / VegTreed) | `http://tree.pfc.forestry.ca/kNN-LandCover.tar` | 650,629,120 | 2 | Archived |
| kNN-Soils (FFCN / FFOC / FFTHIC / FFTN / MBD / MCLAY / MOC / MSAND / MSILT / MTN + Mansuy 2014 publication) | `http://tree.pfc.forestry.ca/kNN-Soils.tar` | 3,011,911,680 | 2 | Archived |
| kNN-Dominant (separator pointing to nfis.org) | `http://tree.pfc.forestry.ca/kNN-Dominant.tar` | (302 → `http://nfis.org/notfound_bi.html`, 614-byte HTML; not a tar) | 2 | **DEFERRED** — placeholder redirect, no source archive exists |

After batch 2 the deployment satisfies `species_composition` (kNN-Species, kNN-SpeciesGroups, kNN-Genus, kNN-SpeciesDominant) and `residue_yield_policy` (kNN-StructureBiomass, kNN-StructureStandVolume, kNN-LandCover, kNN-Soils) gates for the source-inventory row 46.

The remaining `kNN-Dominant.tar` URL is a 302 redirect to the nfis.org "not found" placeholder (Last-Modified 2015-07-22). The other 6 batch-2 URLs in the family were unaffected by the same host; the redirect is specific to the kNN-Dominant file pointer rather than a host outage. The deferral note is captured in `DOWNLOAD_DEFERRED_kNN-Dominant.txt` next to this ACQUISITION.md.

## Local files (batch 2 additions in **bold**)

| Path | Bytes | Local SHA-256 |
|------|------:|---------------|
| `data/raw/beaudoin_knn/kNN-Species.tar` | 2,497,034,240 | `65232a573ea417c292645cef1d57fcea78b0e75ee2e6b1b917ef2b95edc058fb` |
| `data/raw/beaudoin_knn/kNN-StructureBiomass.tar` | 2,685,040,640 | `aa08f8ca2e4503034aac4703615e8bf5db8e74c1b73e5ab4ee4bca7889619e17` |
| `data/raw/beaudoin_knn/kNN-StructureStandVolume.tar` | **1,808,496,640** | **`98f6ec11d5d55e0d745f6d4ba93d5f5027b25ad95236b2e5546d557f797ea74e`** |
| `data/raw/beaudoin_knn/kNN-SpeciesGroups.tar` | **2,068,951,040** | **`84ede1351b21646290f3e67c9bf6c60793fff5cf8efabda7e8961d2ecb582c13`** |
| `data/raw/beaudoin_knn/kNN-SpeciesDominant.tar` | **1,357,199,360** | **`2089e3d2c17eda782ef5ec0eec1b76712bf1e9d6df030dd469db45a8745f4859`** |
| `data/raw/beaudoin_knn/kNN-Genus.tar` | **1,655,869,440** | **`5364f57f962606d0b16bdcaae255b6b09f32a58540a70efd32e3a35317fa361c`** |
| `data/raw/beaudoin_knn/kNN-LandCover.tar` | **650,629,120** | **`167d7fb805f04c104fbcd6f5b5ef5ff7bb9c1fd9b4127d3d3625d1931d6894bd`** |
| `data/raw/beaudoin_knn/kNN-Soils.tar` | **3,011,911,680** | **`e350a7d2f0991d9ed5a20d8e986dd6b0aac3705834df29a43d4533bd449e0ab3`** |

Server `Last-Modified` timestamps: `Mon, 18 Jan 2016 17:26:57 GMT` (kNN-StructureStandVolume) / `Fri, 15 Jan 2016 23:20:05 GMT` (kNN-SpeciesGroups) / `Fri, 15 Jan 2016 23:12:45 GMT` (kNN-SpeciesDominant) / `Fri, 15 Jan 2016 23:14:16 GMT` (kNN-Genus) / `Fri, 15 Jan 2016 23:15:40 GMT` (kNN-LandCover) / `Fri, 15 Jan 2016 23:08:28 GMT` (kNN-Soils) / `Fri, 15 Jan 2016 17:18:30 GMT` (kNN-Species) / `Mon, 18 Jan 2016 16:46:55 GMT` (kNN-StructureBiomass). Server Apache: `Apache/2.4.12 (Unix) OpenSSL/1.0.2u mod_auth_dacs/1.4.33`.

Per-archive inner member contents (per size, not extracted to disk) are listed in `PROVENANCE.csv`.

## Annex status

All 8 .tar archives are in their annex-managed state at [here] + [arbutus-s3]. The full content can be regenerated through `datalad get <path>` (which fetches the corresponding `arbutus-s3` object).

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
> Mansuy, N., et al. (2014). *A spatial modelling framework for assessment
>   and prediction of soil carbon stocks in boreal forest ecosystems.* Geoderma.
Reproduced under the Open Government Licence — Canada.
