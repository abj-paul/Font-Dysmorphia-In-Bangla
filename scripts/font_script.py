import os
from fontforge import *

font_file = os.sys.argv[1]
font = open(font_file)

# Create a folder based on the font name
font_name = os.path.splitext(os.path.basename(font_file))[0]
output_folder = font_name + "_images"

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Export each glyph as an image
for glyph in font:
    if font[glyph].isWorthOutputting():
        output_path = os.path.join(output_folder, font[glyph].glyphname + ".png")
        font[glyph].export(output_path)
