from PIL import Image, ImageOps, ImageFilter
from numpy import asarray
import sys
import pathlib

# For dark terminal backgrounds
def printImageD():
    data = asarray(image)
    for i in range(data.shape[0]):
        # One char represents one pixel.
        for j in range(data.shape[1]):
            if data[i][j] >= 204:
                print("█", end="")
            elif data[i][j] >= 153:
                print("▓", end="")
            elif data[i][j] >= 102:
                print("▒", end="")
            elif data[i][j] >= 51:
                print("░", end="")
            else:
                print(" ", end="")
        print()

# For light terminal backgrounds
def printImageL():
    data = asarray(image)
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            if data[i][j] >= 204:
                print(" ", end="")
            elif data[i][j] >= 153:
                print("░", end="")
            elif data[i][j] >= 102:
                print("▒", end="")
            elif data[i][j] >= 51:
                print("▓", end="")
            else:
                print("█", end="")
        print()

if pathlib.Path(sys.argv[1]).suffix == ".svg":
    print("SVG not yet supported.")
else:
    image = Image.open(sys.argv[1])
    settings = open("/usr/local/bin/icat_settings.cfg", "r")
    if "half" in settings.readline():
        width, height = image.size
        # Resizes image to be 50% as wide since image will be printed in half width "pixels".
        image = image.resize((width, round(height / 2)), Image.ANTIALIAS)
        # Is a multiplier used in doubling horizontal detail.
        scaleX = 2
    else:
        # Is a multiplier used in keeping horizontal detail the same. 
        scaleX = 1

    options = sys.argv[2:]
    if "0x1.5" in options:
        image = ImageOps.contain(image, (60 * scaleX, 60)).convert("L")
    elif "0x2" in options:
        image = ImageOps.contain(image, (80 * scaleX, 80)).convert("L")
    else:
        # Default size printed if user gives no args.
        image  = ImageOps.contain(image, (40 * scaleX, 40)).convert("L")
    
    if "0-s" in options:
        image = image.filter(ImageFilter.SHARPEN)
    if "0-c" in options:
        image = image.filter(ImageFilter.CONTOUR)
    if "0-i" in options:
        image = ImageOps.invert(image)

    if "light" in settings.readline():
        printImageL()
    else:
        printImageD()
    
    image.close()
    settings.close()