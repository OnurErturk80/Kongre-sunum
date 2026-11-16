#!/usr/bin/env python3
"""cikti/png/NN.png -> cikti/temas_K.png (2x2 temas sayfaları)."""
from PIL import Image
import glob, pathlib
ps = sorted(glob.glob('cikti/png/*.png')); 
for eski in glob.glob('cikti/temas_*.png'): pathlib.Path(eski).unlink()
for k in range(0, len(ps), 4):
    T = Image.new('RGB', (1920*2+60, 1080*2+60), '#888')
    for j, p in enumerate(ps[k:k+4]):
        T.paste(Image.open(p).convert('RGB'), (20+(j%2)*(1920+20), 20+(j//2)*(1080+20)))
    T = T.resize((1950, 1110), Image.LANCZOS); T.save(f'cikti/temas_{k//4+1}.png')
print(len(ps), 'slayt')
