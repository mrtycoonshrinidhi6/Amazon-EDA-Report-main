"""
Assemble images from `visuals/` into a single PDF presentation `visuals/presentation.pdf`.
Usage:
    python scripts/make_presentation.py --input_dir visuals --output visuals/presentation.pdf

This script uses Pillow to open images and save them as a multi-page PDF.
"""
import argparse
from pathlib import Path
from PIL import Image


def images_to_pdf(input_dir: Path, output_file: Path):
    imgs = []
    for ext in ('*.png', '*.jpg', '*.jpeg'):
        imgs.extend(sorted(input_dir.glob(ext)))
    if not imgs:
        raise SystemExit(f'No images found in {input_dir!s}')
    pil_imgs = []
    for p in imgs:
        img = Image.open(p).convert('RGB')
        pil_imgs.append(img)
    first, rest = pil_imgs[0], pil_imgs[1:]
    first.save(output_file, save_all=True, append_images=rest)
    print(f'Wrote presentation PDF to {output_file!s}')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_dir', default='visuals', help='Directory containing image files')
    parser.add_argument('--output', default='visuals/presentation.pdf', help='Output PDF file')
    args = parser.parse_args()
    images_to_pdf(Path(args.input_dir), Path(args.output))

if __name__ == '__main__':
    main()
