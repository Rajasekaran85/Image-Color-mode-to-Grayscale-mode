# Application Title

Image Grayscale mode converter

## Description

* Convert the Color Images (RGB mode) to Grayscale mode type
* Using Wand Library (ImagicMagick)
* Source Image (Input Image) resolution will retain in the converted output image.
* Images types: TIF, JPG, PNG types handled

## Getting Started

### Dependencies 

* Windows 7 or above

### Installing

* pip install Wand


### Executing program

* Run the program
* Tool will ask to enter the path of the input image file
* Tool execute the Images and create the grayscale converted images in the "Grayscale" folder of the same input file  path

### Help


## Version History

* 0.1
    * Initial Release
* 0.2
    * Simplified program, previously used Pillow library.
    * Using the Pillow library the converted images output in TIFF lower version, (i.e. pillow changed the higher version image to lower version image).
    * So now we used ImageMagick library and the converted output tiff version will be 5.0 
