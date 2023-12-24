import os
from fontforge import *

def process_font(font_file):
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
            # Get the Unicode code point of the glyph
            unicode_code_point = ord(font[glyph].unicode)
            
            # Format the output filename with the Unicode code point
            output_filename = f"{unicode_code_point:04X}.png"
            
            output_path = os.path.join(output_folder, output_filename)
            font[glyph].export(output_path)

if __name__ == "__main__":
    # Specify the font file as a command-line argument
    font_file = os.sys.argv[1]
    
    process_font(font_file)

