#!/usr/bin/python3

verbose = False


import sys
import argparse
from wand.image import Image

def v_print(message):
	if verbose == True:
		print(message)

	return


def main(argv):
	global verbose

	# The place you plan on storing the images in, in case they are
	# in a different location than the HTML page.
	# http://www.foo.com/folder/
	image_location_url = ""

	# The URL the negstrip file can be found at
	# http://www.foo.com/images/negstrip.jpg"
	negstrip = "negstrip.jpg"

	# The URL your stylesheet for this page can be found at
	# https://www.foo.com/style.css
	style_sheet = "style.css"

	# The name of the generated HTML page
	html_page = "index.html"

	# The maximum width of any of the images. Used to calculate nedstrip width.
	max_width = 0

	negstrip_width = 0;

	# Instantiate the parser
	parser = argparse.ArgumentParser(description='Rename images and videos from cameras')
	parser.add_argument('--softresize', type=int, default=0, help='Resize to specified in HTML only, without resizing image')
	parser.add_argument('--title', help='Title for the top of the HTML page')
	parser.add_argument('--htmlpage', help='Name of generated HTML page. Default is index.html')
	parser.add_argument('--style', help='URL where the style sheet will be found')
	parser.add_argument('--imagelocation', help='URL where the images will be stored if not in the same place as html')
	parser.add_argument('-v', action='store_true', help='Be Verbose')
	parser.add_argument('--nofilename', action='store_true', help="Don't include file names under each image")
	parser.add_argument('-f', required=True, nargs='+', help='Image files to process')
	args = parser.parse_args()

	verbose = args.v

	if verbose:
		print("Argument Values:")
		print("softresize   :", args.softresize)
		print("title        :", args.title)
		print("htmlpage     :", args.htmlpage)
		print("style        :", args.style)
		print("imagelocation:", args.imagelocation)
		print("verbose      :", args.v)
		print("Images       :", args.f)
		print()
		print()

	if args.softresize > 0:
		# TODO - Fix this. If all images are vertical then this will be too wide.
		max_width = args.softresize
	else:
		# Iterate each image and find the max width
		for x in args.f:
			with Image(filename=x) as img:
				if img.width > max_width:
					max_width = img.width

	print("width:", max_width)
	negstrip_width = max_width + 100

	# Overwrite default output page if new one specified
	if args.htmlpage:
		html_page = args.htmlpage

	# Set image location URL
	if args.imagelocation:
		image_location_url = args.imagelocation

	# TODO - check if already exists and fail
	# TODO - check if creation fails

	htmlfile = open(html_page, "w")

	if args.style:
		style_sheet = args.style

	if args.title:
		title = args.title
	else:
		title = ""

	htmlfile.write("<!DOCTYPE html PUBLIC \"-//W3C//DTD HTML 4.01//EN\" \"http://www.w3.org/TR/html4/strict.dtd\">")
	htmlfile.write("<html>\n<head><meta content=\"text/html; charset=ISO-8859-1\" http-equiv=\"content-type\">\n<title>%s</title>\n" % title)
	htmlfile.write("<link rel=\"stylesheet\" type=\"text/css\" href=\"%s\">\n" % style_sheet)
	htmlfile.write("</head>\n")
	htmlfile.write("<body>\n")
	htmlfile.write("<div style=\"text-align:center;\">\n")
	htmlfile.write("<h2>%s</h2>\n<br><br><br>\n</div>\n" % title)
	htmlfile.write("<div style=\"text-align:center; background: transparent url(%s) repeat-y fixed center; background-size: %d" % (negstrip, negstrip_width))
	htmlfile.write("px;\">\n")
	htmlfile.write("<br><br><br>\n\n")

	# Iterate and process each image
	for x in args.f:
		print("Input File:", x)

		with Image(filename=x) as img:
			print("size:", img.size)

			width = img.width
			height = img.height

			if args.softresize > 0:
				if width < height:
					height = args.softresize
					width = (height/img.height) * width
				else:
					width = args.softresize
					height = (width/img.width) * height

#			htmlfile.write("<hr style=\"width: 500px; height: 2px;\">\n")
			htmlfile.write("<hr style=\"width: %dpx; height: 2px;\">\n" % max_width)
			htmlfile.write("<img style=\"border: 5px solid white;\" alt=\"\" src=\"%s" % image_location_url)
			htmlfile.write("%s\" width=%d height=%d vspace=\"20\">\n\n" % (x, width, height))

			if args.nofilename == False:
				htmlfile.write("<br><br>%s\n\n" % x)

			htmlfile.write("<br><br><br><br>\n")

	# write the closing html info for the big thumbnail file
	htmlfile.write("<hr style=\"width: %dpx; height: 2px;\">\n" % max_width)
	htmlfile.write("<br><br><br><br>\n")
	htmlfile.write("</div>\n")
	htmlfile.write("<div style=\"text-align:center;\">\n<br><br><br><br><br><br><br><hr style=\"width: 100%; height: 2px;\"><br>\n")
	htmlfile.write("All images are protected under copyright and may not be used, copied, altered, or reproduced in any way without the expressed written permission of the author.\n")
	htmlfile.write("</div>\n")
	htmlfile.write("</body>\n</html>\n")

	htmlfile.close()

if __name__ == "__main__":
	main(sys.argv)
