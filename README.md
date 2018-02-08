# make_html_image_page
Python script to create html pages of images

This is a pretty simple script that will create an HTML page consisting of a vertical column of supplied images. The images will be bordered by a negative strip image to give it a film roll sort of look.

There are several command line options where you can specify the location of a style sheet, the negative strip, final remote location of images, and tell the script to "soft" resize the images. This option will set the image size in the HTML but not physically resize the images.

If none of these options are set then the generated HTML looks for everything locally.

The script depends on the Wand image processing module for Pyhon.
