#!/usr/bin/env bash
set -euo pipefail
# Read-only MERIS extraction commands used for this sample (2026-11-20).
# Requires mdbtools >= 1.0.0 (ACCDB support).
WORK="${WORK:-/tmp/meris}"
DB="${WORK}/extracted/MERIS_BdTbl.accdb"
OUT="${OUT:-$(cd "$(dirname "$0")" && pwd)}"

test -f "$DB" || { echo "missing $DB; download and unzip meris.zip first" >&2; exit 1; }
command -v mdb-tables >/dev/null || { echo "install mdbtools" >&2; exit 1; }

mdb-tables -1 "$DB" > "${OUT}/tables_all.txt"
for t in \
  tbl_Liste_ZonesRedev tbl_redevances_F1234 \
  tbl_Zones_RedevBenefRentSal_F1234 tbl_couts_zones \
  tbl_Liste_Traitements tbl_Equations_Recolte \
  tbl_Profil_Rentabilite_EqGraph tbl_Essences_b \
  tbl_essences_revenus_EssDhp tbl_770rq_Resultats_Rentabilite \
  tbl_770rq_Resultats_Rentabilite_m3_3 \
  tbl_770rq_Resultats_Rentabilite_Synthese_4 \
  tbl_775rq_Resultats_Rentabilite_Frais tbl_Rentabilite \
  tbl_parametres_rentabilite tbl_Profil_Rentabilite \
  tbl_Volume_Prescription tbl_unifiee_assigne_zones \
  tbl_unifiee_assigne_traitements tbl_Compile_Global
do
  mdb-count "$DB" "$t" | awk -v t="$t" '{print t "," $0}'
  mdb-export "$DB" "$t" > "${OUT}/${t}.csv"
done
