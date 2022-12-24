from PIL import Image, ImageOps, ImageFilter
from numpy import asarray
import sys
import pathlib

def printImage():
    data = asarray(bw_img)
    for i in range(data.shape[0]):
        # One char represents one half-width pixel.
        for j in range(data.shape[1]):
            if data[i][j] >= 204:
                print("█", end="")
            elif data[i][j] >= 153:
                print("▓", end="")
            elif data[i][j] >= 102:
                print("▒",end="")
            elif data[i][j] >= 51:
                print("░", end="")
            else:
                print(" ", end="")
        print()

if (pathlib.Path(sys.argv[1]).suffix == ".svg"):
    print("SVG not yet supported.")
else:
    image = Image.open(sys.argv[1])
    width, height = image.size
    # Resizes image to be 50% as wide since image will be printed in half width "pixels".
    image = image.resize((width, round(height / 2)), Image.ANTIALIAS)
    # Resize image to maintian new aspect ratio (so it can fit on terminal) as well as convert it to black and white.
    bw_img  = ImageOps.contain(image, (80,40)).convert("L")
    
    options = sys.argv[2:]
    if "0-s" in options:
        bw_img = bw_img.filter(ImageFilter.SHARPEN)
    if "0-c" in options:
        bw_img = bw_img.filter(ImageFilter.CONTOUR)
    if "0-i" in options:
        bw_img = ImageOps.invert(bw_img)

    printImage()
