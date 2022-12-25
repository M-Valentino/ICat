from PIL import Image, ImageOps, ImageFilter
from numpy import asarray
import sys
import pathlib

# For dark terminal backgrounds
def printImageD():
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

# For light terminal backgrounds
def printImageL():
    data = asarray(bw_img)
    for i in range(data.shape[0]):
        # One char represents one half-width pixel.
        for j in range(data.shape[1]):
            if data[i][j] >= 204:
                print(" ", end="")
            elif data[i][j] >= 153:
                print("░", end="")
            elif data[i][j] >= 102:
                print("▒",end="")
            elif data[i][j] >= 51:
                print("▓", end="")
            else:
                print("█", end="")
        print()

if (pathlib.Path(sys.argv[1]).suffix == ".svg"):
    print("SVG not yet supported.")
else:
    image = Image.open(sys.argv[1])
    settings = open("/usr/local/bin/icat_settings.cfg", "r")
    if ("half" in settings.readline()):
        width, height = image.size
        # Resizes image to be 50% as wide since image will be printed in half width "pixels".
        image = image.resize((width, round(height / 2)), Image.ANTIALIAS)
        scaleX = 2
    else:
        # Enables width pixel mode. 
        scaleX = 1

    options = sys.argv[2:]
    if ("0x1.5" in options):
        bw_img  = ImageOps.contain(image, (60 * scaleX,60)).convert("L")
    elif ("0x2" in options):
        bw_img  = ImageOps.contain(image, (80 * scaleX,80)).convert("L")
    else:
        # Default size printed if user gives no args.
        bw_img  = ImageOps.contain(image, (40 * scaleX,40)).convert("L")
    
    if ("0-s" in options):
        bw_img = bw_img.filter(ImageFilter.SHARPEN)
    if ("0-c" in options):
        bw_img = bw_img.filter(ImageFilter.CONTOUR)
    if ("0-i" in options):
        bw_img = ImageOps.invert(bw_img)

    if ("light" in settings.readline()):
        printImageL()
    else:
        printImageD()
    settings.close()
