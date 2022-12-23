from PIL import Image, ImageOps, ImageFilter, ImageEnhance
from numpy import asarray
import sys

def printImage():
    data = asarray(bw_img)
    for i in range(data.shape[0]):
        # Two chars are printed per pixel so that the image's aspect ratio is preserved.
        for j in range(data.shape[1]):
            if (data[i][j] >= 204):
                print("██", end="")
            elif (data[i][j] < 204 and data[i][j] >= 153):
                print("▓▓", end="")
            elif (data[i][j] < 153 and data[i][j] >= 102):
                print("▒▒",end="")
            elif (data[i][j] < 102 and data[i][j] >= 51):
                print("░░", end="")
            else:
                print("  ", end="")
        print()


image = Image.open(sys.argv[1])
# Resize image to maintian aspect ratio as well as convert it to black and white.
bw_img  = ImageOps.contain(image, (40,40)).convert("L")
    
if (sys.argv[2] == "0-s" or sys.argv[3] == "0-s" or sys.argv[4] == "0-s"):
    bw_img = bw_img.filter(ImageFilter.SHARPEN)

if (sys.argv[2] == "0-c" or sys.argv[3] == "0-c" or sys.argv[4] == "0-c"):
    bw_img = bw_img.filter(ImageFilter.CONTOUR)

if (sys.argv[2] == "0-i" or sys.argv[3] == "0-i" or sys.argv[4] == "0-i"):
    bw_img = ImageOps.invert(bw_img)

printImage()
