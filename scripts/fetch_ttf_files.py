import os
import shutil

def find_ttf_file(folder):
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.lower().endswith('.ttf'):
                return os.path.join(root, file)
    return None

def process_fonts_recursive(current_folder, destination_folder):
    ttf_file = find_ttf_file(current_folder)
    if ttf_file:
        shutil.copy(ttf_file, destination_folder)
        print(f"Copied: {ttf_file}")
        return

    for subfolder in os.listdir(current_folder):
        subfolder_path = os.path.join(current_folder, subfolder)
        if os.path.isdir(subfolder_path):
            process_fonts_recursive(subfolder_path, destination_folder)

def main():
    # Specify the source folder containing font folders
    source_folder = "../fonts/"

    # Specify the destination folder for the selected TTF files
    destination_folder = "../fonts/ttf_files/"

    # Create the destination folder if it doesn't exist
    os.makedirs(destination_folder, exist_ok=True)

    # Iterate through each font folder in the source folder
    for font_folder in os.listdir(source_folder):
        font_folder_path = os.path.join(source_folder, font_folder)
        if os.path.isdir(font_folder_path):
            process_fonts_recursive(font_folder_path, destination_folder)

if __name__ == "__main__":
    main()

