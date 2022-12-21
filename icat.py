from PIL import Image, ImageOps
from numpy import asarray
import cv2 as cv2
import sys

def printImage():
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


if (len(sys.argv) == 1):
    print("USAGE: enter file path to an image.")
elif (sys.argv[2] == "0-i"):
    image = Image.open(sys.argv[1])
    # Resize image to maintian aspect ratio as well as convert it to black and white.
    bw_img  = ImageOps.contain(image, (40,40)).convert("L")
    bw_img = ImageOps.invert(bw_img)
    data = asarray(bw_img)
    printImage()
else:
    image = Image.open(sys.argv[1])
    # Resize image to maintian aspect ratio as well as convert it to black and white.
    bw_img  = ImageOps.contain(image, (40,40)).convert("L")
    data = asarray(bw_img)
    printImage()
