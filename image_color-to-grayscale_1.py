import sys
import os
from PIL import Image
import re

# pillow library used
# After tool execution the converted Image files will placed in the "Grayscale" folder of the sample tif file path

print("\n TIF, JPG, PNG: Color to Grayscale mode Conversion \n")


filepath = input("Enter the Input Image file path: ")
output_directory = "Grayscale"
output = filepath + "/" + output_directory

if os.path.exists(output):
    pass
else:
    os.mkdir(output)

for fname in os.listdir(filepath):
	if fname.endswith(".tif"):
		print(fname)

		input_image = filepath + "/" + fname
		image = Image.open(input_image)
		output_name = output + "/" + fname

		# get the Image DPI value from the Input images
		img_dpi = str(image.info['dpi'])
		patn = re.sub(r"[\(\)]", "", img_dpi)
		sp = patn.split(",")[0]
		dpi_val = round(float(sp))

		# convert the Color image to Grayscale format
		image_conv = image.convert('L')
		image_conv.save(output_name, dpi=(dpi_val,dpi_val))

	if fname.endswith(".jpg"):
		print(fname)
		input_image = filepath + "/" + fname
		image = Image.open(input_image)
		output_name = output + "/" + fname

		# get the Image DPI value from the Input images
		img_dpi = str(image.info['dpi'])
		patn = re.sub(r"[\(\)]", "", img_dpi)
		sp = patn.split(",")[0]
		dpi_val = round(float(sp))

		# convert the Color image to Grayscale format
		image_conv = image.convert('L')
		image_conv.save(output_name, dpi=(dpi_val,dpi_val))

	if fname.endswith(".png"):
		print(fname)
		input_image = filepath + "/" + fname
		image = Image.open(input_image)
		output_name = output + "/" + fname

		# get the Image DPI value from the Input images
		img_dpi = str(image.info['dpi'])
		patn = re.sub(r"[\(\)]", "", img_dpi)
		sp = patn.split(",")[0]
		dpi_val = round(float(sp))

		# convert the Color image to Grayscale format
		image_conv = image.convert('L')
		image_conv.save(output_name, dpi=(dpi_val,dpi_val))
