#!/bin/bash

FONT_FOLDER="../font/"
CONTOUR_SCRIPT="contour_script.py"

# Check if python3 command exists
if command -v python3 &> /dev/null; then
    PYTHON_COMMAND="python3"
else
    # Use python as a fallback if python3 is not found
    PYTHON_COMMAND="python"
fi

# Iterate over font files in the folder
for FONT_FILE in "$FONT_FOLDER"/*.ttf; do
    # Run fontforge script
    fontforge -script font_script.py "$FONT_FILE"

    # Extract font name from the font file
    FONT_NAME=$(basename "$FONT_FILE" .ttf)

    # Run contour script for the generated images
    "$PYTHON_COMMAND" "$CONTOUR_SCRIPT" "$FONT_NAME"_images
done

