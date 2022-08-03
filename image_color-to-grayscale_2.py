import sys
import os
import glob
from wand.image import Image

# pip install Wand
# After tool execution the converted Image files will placed in the "Grayscale" folder of the tif file path
# TIFF file version will be 5.0

print("\n TIF, JPG, PNG: Color to Grayscale mode Conversion \n")


filepath = input("Enter the Input Image file path: ")
output_directory = "Grayscale"
output = filepath + "/" + output_directory + "/"

if os.path.exists(output):
    pass
else:
    os.mkdir(output)

# TIFF Image Process
for fname in glob.glob(filepath + "/" + "*.tif"):
	input_image = fname
	filename = os.path.basename(fname)
	print(filename)

	with Image(filename=input_image) as img:
		img.transform_colorspace("gray")
		img.save(filename=output + filename)

# JPG Image Process
for fname in glob.glob(filepath + "/" + "*.jpg"):
	input_image = fname
	filename = os.path.basename(fname)
	print(filename)

	with Image(filename=input_image) as img:
		img.transform_colorspace("gray")
		img.save(filename=output + filename)

# PNG Image Process
for fname in glob.glob(filepath + "/" + "*.png"):
	input_image = fname
	filename = os.path.basename(fname)
	print(filename)

	with Image(filename=input_image) as img:
		img.transform_colorspace("gray")
		img.save(filename=output + filename)


print("\n\n *** Process Completed *** \n")
