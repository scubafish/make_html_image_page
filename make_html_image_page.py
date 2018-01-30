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

	# Instantiate the parser
	parser = argparse.ArgumentParser(description='Rename images and videos from cameras')
	parser.add_argument('--htmlpage', nargs='?', help='Name of generated HTML page. Default is index.html')
	parser.add_argument('-v', action='store_true', help='Be Verbose')
	parser.add_argument('--nofilename', action='store_true', help="Don't include file names under each image")
	parser.add_argument('-f', required=True, nargs='+', help='Image files to process')
	args = parser.parse_args()

	verbose = args.v

	if verbose:
		print("Argument Values:")
		print(args.htmlpage)
		print(args.v)
		print(args.f)


	# Iterate and process each image
	for x in args.f:
		print("Input File:", x)

		with Image(filename=x) as img:
			print("size:", img.size)



if __name__ == "__main__":
	main(sys.argv)
