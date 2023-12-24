#!/bin/bash

# Specify the folder containing ZIP files
zip_folder="../fonts"

# Change to the ZIP folder
cd "$zip_folder"

# Iterate through each ZIP file and unzip its contents
for zip_file in *.zip; do
    # Extract the contents to a folder with the same name as the ZIP file (without extension)
    unzip -d "${zip_file%.zip}" "$zip_file"
done

