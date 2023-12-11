import cv2
import os
import csv

def calculate_metrics(image_path):
    # Read the image using OpenCV
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Get the dimensions (width and height)
    height, width = img.shape

    # Find contours of non-white areas
    contours, _ = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Calculate the radius (assuming circular shape)
    if contours:
        # Use the bounding circle of the largest contour
        (x, y), radius = cv2.minEnclosingCircle(max(contours, key=cv2.contourArea))
    else:
        # Default to zero if no contours are found
        radius = 0

    # Calculate the area of non-white pixels
    area = cv2.countNonZero(img)

    return height, width, radius, area

def process_folder(folder_path, output_csv):
    with open(output_csv, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Font', 'Height', 'Width', 'Radius', 'Area'])

        for filename in os.listdir(folder_path):
            if filename.endswith(".png") or filename.endswith(".jpg") or filename.endswith(".jpeg"):
                image_path = os.path.join(folder_path, filename)
                height, width, radius, area = calculate_metrics(image_path)
                csv_writer.writerow([filename, height, width, radius, area])

if __name__ == "__main__":
    images_folder = "Harvest Season_images"
    output_csv = images_folder+".csv"
    process_folder(images_folder, output_csv)

