# ICat
Have you ever wanted to know what an image looks like without having to leave the terminal? Well you're in luck! Now you can "cat" images with this utility called ICat (short for image cat)! ICat works by reading images and converting them to ASCII text. Images printed to the terminal are displayed in greyscale with 5 colors.

ICat is primarily built with Python.
### Requirements
The following is needed on your Mac or Linux installation in order to run ICat:
- Python3
- numPy Python library
- Pillow Python library
- pathlib Python library
### Installation
Clone the git repo anywhere you like and then run **./install.sh**. If you get a `Permission denied` error, run the `chmod` command to change the file's permissions.
The directory ICat is installed to is `/usr/local/bin/`. If you delete your local clone of the ICat repo, the installation will not be affected.

When installing, you will be prompted to answer if your terminal is light or dark. This is to ensure that images display properly and don't appear inverted. You will also be asked if this character, '▓' appears as a square. This is to ensure that images don't appear stretched. If the character appears as a rectangle, images will be printed in "half pixels", and as a result, will have more horizontal detail.
## Running
To use ICat, run **icat 'imageFilename'**. You can add arguments after the file name argument.
- **-c** applies a contour filter to the image.
- **-i** inverts the image.
- **-s** sharpens the image.
- **x1.5** prints image 1.5x larger than the default size.
- **x2** prints image 2x larger than the default size.

## Example
icating this image:
<br>
<img src="https://user-images.githubusercontent.com/79779618/209410544-2d2c89ff-b77f-4165-a294-ebae8efd4de2.gif">
<br>
Produces this result:
<br>
<img src="https://user-images.githubusercontent.com/79779618/209453438-04fd71a5-0dce-483a-801c-4bcb9eca351d.png" width="400px">
