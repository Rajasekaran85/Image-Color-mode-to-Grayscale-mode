import sys
import os
from PIL import Image
import cv2
import re
import glob

# pillow library used
# OpenCV library used
# After tool execution the converted Image files will placed in the "Grayscale" folder of the sample tif file path

print("\n TIF, JPG, PNG: Color to Grayscale mode Conversion \n")


filepath = input("Enter the Input Image file path: ")
output_directory = "Grayscale"
output = filepath + "/" + output_directory + "/"

if os.path.exists(output):
    pass
else:
    os.mkdir(output)

for fname in glob.glob(filepath + "/" + "*.tif"):
	input_image = fname
	image = cv2.imread(input_image)
	filename = os.path.basename(fname)
	print(filename)

	# get the Image DPI value from the Input images
	image1 = Image.open(input_image)
	img_dpi = str(image1.info['dpi'])
	patn = re.sub(r"[\(\)]", "", img_dpi)
	sp = patn.split(",")[0]
	dpi_val = round(float(sp))

	# convert the Color image to Grayscale format
	image_conv = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
	save_image = Image.fromarray(image_conv)
	save_image.save(output + filename, dpi=(dpi_val,dpi_val))


for fname in glob.glob(filepath + "/" + "*.jpg"):
	input_image = fname
	image = cv2.imread(input_image)
	filename = os.path.basename(fname)
	print(filename)

	# get the Image DPI value from the Input images
	image1 = Image.open(input_image)
	img_dpi = str(image1.info['dpi'])
	patn = re.sub(r"[\(\)]", "", img_dpi)
	sp = patn.split(",")[0]
	dpi_val = round(float(sp))

	# convert the Color image to Grayscale format
	image_conv = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
	save_image = Image.fromarray(image_conv)
	save_image.save(output + filename, dpi=(dpi_val,dpi_val))



for fname in glob.glob(filepath + "/" + "*.png"):
	input_image = fname
	image = cv2.imread(input_image)
	filename = os.path.basename(fname)
	print(filename)

	# get the Image DPI value from the Input images
	image1 = Image.open(input_image)
	img_dpi = str(image1.info['dpi'])
	patn = re.sub(r"[\(\)]", "", img_dpi)
	sp = patn.split(",")[0]
	dpi_val = round(float(sp))

	# convert the Color image to Grayscale format
	image_conv = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
	save_image = Image.fromarray(image_conv)
	save_image.save(output + filename, dpi=(dpi_val,dpi_val))

print("\n\n *** Process Completed *** \n")
