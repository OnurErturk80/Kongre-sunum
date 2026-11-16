#!/bin/bash
# Taslağı baştan üretir: sunum.html -> denetim -> salon dosyası -> PDF/PPTX/PNG -> temas sayfaları
set -e
cd "$(dirname "$0")"; S=../skill/scripts; mkdir -p cikti
python3 kur_sunum_v4.py
python3 $S/sayi_denetle.py sunum.html analiz/tum_sayilar.json
python3 $S/sunum_derle.py sunum.html cikti/sunum_salon.html 2>&1 | grep -v FFTM
python3 $S/disa_aktar.py cikti/sunum_salon.html --cikti-dir cikti --ad sunum
python3 temas.py
