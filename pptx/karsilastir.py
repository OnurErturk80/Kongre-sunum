from PIL import Image, ImageDraw
import pathlib, sys
H = pathlib.Path(__file__).parent.parent / 'sunum_v4/cikti/png'; P = pathlib.Path('on')
def sheet(nums, ad):
    W, Hh = 920, 518
    S = Image.new('RGB', (W*2+30, (Hh+30)*len(nums)), 'white'); d = ImageDraw.Draw(S)
    for i, n in enumerate(nums):
        a = Image.open(H/f'{n:02d}.png').resize((W, Hh)); b = Image.open(P/f's-{n:02d}.png').resize((W, Hh))
        S.paste(a, (0, i*(Hh+30)+24)); S.paste(b, (W+30, i*(Hh+30)+24))
        d.text((4, i*(Hh+30)+4), f'{n} HTML', fill='black'); d.text((W+34, i*(Hh+30)+4), f'{n} PPTX', fill='black')
    S.save(f'k_{ad}.png')
nums = list(map(int, sys.argv[1:]))
for j in range(0, len(nums), 3): sheet(nums[j:j+3], f'{nums[j]:02d}')
