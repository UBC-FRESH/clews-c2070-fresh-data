# QC Inventory Acquisition — 2023-08-09

## Identity

| Field | Value |
|-------|-------|
| Publisher | Ministère des Ressources naturelles et des Forêts (MRNF) — Direction des inventaires forestiers (DIF) |
| Title (French) | Carte écoforestière originale et résultats d'inventaire courants |
| Title (English) | Original ecoforestry map and current inventory results |
| Catalog | Données Québec `a232475f-ec3d-476a-8725-d0c12367b3f0`; mirrored at Open Canada |
| Licence | Attribution (CC-BY 4.0) |
| Acquisition date | 2026-08-09 |
| Acquired by | UBC FRESH / CLEWs-C2070 forestry data maintainers |
| Coverage | Public forest south of 52° parallel in QC |
| Vintage | 5th decennial ecoforestry inventory (5e inventaire écoforestier); updated annually since 2017 |
| CRS | Québec Lambert — EPSG:32198 |

## Bulk URL paths (openly-downloadable, recorded but not archived in this submodule)

The full provincial GeoPackage weighs **11.2 GB** (CARTE_ECO_ORI_PROV_GPKG.zip). Pulling that
volume is outside the scope of this increment; the per-feuillet index
(`URL_250K_ORI.csv`, 60 feuillets) is archived here as the navigational
authority.

| Artifact | URL | Bytes (server Content-Length) | ETag | Last-Modified | Status |
|----------|-----|-------------------------------|------|---------------|--------|
| Provincial GeoPackage | `https://diffusion.mffp.gouv.qc.ca/Diffusion/DonneeGratuite/Foret/DONNEES_FOR_ECO_SUD/Resultats_inventaire_et_carte_ecofor/02-Donnees/PROV/CARTE_ECO_ORI_PROV_GPKG.zip` | 11,244,667,626 | `d8b1406a83fadc1:0` | 2026-06-12 15:52:04 | URL recorded only; payload NOT archived in this submodule |
| Provincial GeoPackage (up-to-date) | `https://diffusion.mffp.gouv.qc.ca/Diffusion/DonneeGratuite/Foret/DONNEES_FOR_ECO_SUD/Carte_ecoforestiere_avec_perturbations/02-Donnees/PROV/CARTE_ECO_AJOUR_PROV_GPKG.zip` | 11,900,000,000+ | (not probed; CC-BY 4.0) | 2026-02-03 | Same posture as the ORI product; recorded for future migration |
| Per-feuillet index CSV | `https://diffusion.mffp.gouv.qc.ca/Diffusion/DonneeGratuite/Foret/DONNEES_FOR_ECO_SUD/Resultats_inventaire_et_carte_ecofor/03-Telechargement/URL_250K_ORI.csv` | 31,546 | (MD5 43e85c41…) | 2025-07-14 | Archived in `provenance/` |
| Per-agence index CSV | `https://diffusion.mffp.gouv.qc.ca/Diffusion/DonneeGratuite/Foret/DONNEES_FOR_ECO_SUD/Resultats_inventaire_et_carte_ecofor/03-Telechargement/URL_Agences_ORI.csv` | 8,131 | (MD5 711b21cd…) | 2025-07-14 | Archived in `provenance/` |
| LISEZ-MOI readme (FR, official) | `https://diffusion.mffp.gouv.qc.ca/Diffusion/DonneeGratuite/Foret/DONNEES_FOR_ECO_SUD/Resultats_inventaire_et_carte_ecofor/01-Documentation/LISEZ-MOI_carte-eco-ori-resultats_DQ.pdf` | 1,361,365 | (MD5 5f9c0abe…) | 2026-06-12 | Archived in `provenance/` |

## Feuille 21M (sample, archived)

The QC meridian 69° to 70° feuille 21M (~Saguenay–Lac-Saint-Jean, ~30 000 km²;
mixed boreal) was selected as a representative southern-boreal slice. It
weighs 854.6 MB and contains the same table set as the per-feuillet product:

- `PEUPLEMENT` — ecoforestry polygons (stand-level species, age, height,
  density, origin, productivity; CC-BY 4.0).
- `COMPILATION_FOR` — denometric compilation, polygon-linkable volume
  estimates by species and grant type.
- `STATION_FOR` — forest station characterisation (attribute lookup table).
- `DECHIC_DECOUPAGE` — the original ecoforestry stratification.
- `PER_HUMID_SUP` (and adjacent) — DEC / drainage / ecological classifications.

| Field | Value |
|-------|-------|
| Feuille | 21M (Saguenay–Lac-Saint-Jean area, southern boreal QC) |
| URL | `https://diffusion.mffp.gouv.qc.ca/Diffusion/DonneeGratuite/Foret/DONNEES_FOR_ECO_SUD/Resultats_inventaire_et_carte_ecofor/02-Donnees/Decoupage250K/21M/PRODUITS_IEQM_21M_GPKG.zip` |
| Bytes (server Content-Length) | 854,559,481 |
| Local SHA-256 | `ba38a58da5c71bdccfc8c62a831024978717af19e206bf49a9074931a9b005a1` |
| Status | Archived under `per_feuillet_sample/` (git-annex) |

## CSAS analysis posture

The 21M GPKG is used here as a real-schema anchor for the
`fresh_fibre.casfri_qc_reader` test suite. The reader's mapping is
synthetic-bounded for the LP fixture (per Phase 7 P7.1 CASFRI plan §3.2);
the real-feuille sample proves the reader's column-shape guess is
consistent with the actual file's geometry layer.

## Acknowledgements / citation

> MINISTÈRE DES RESSOURCES NATURELLES ET DES FORÊTS. *Carte écoforestière
> originale et résultats d'inventaire courants*, [Jeu de données], dans
> Données Québec, 2017, mis à jour le 03 février 2026.
> <https://www.donneesquebec.ca/recherche/dataset/resultats-d-inventaire-et-carte-ecoforestiere>
> (consulted 2026-08-09).

CC-BY 4.0 — reproduction with attribution and indication of changes
permitted.
