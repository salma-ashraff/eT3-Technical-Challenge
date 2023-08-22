#1. Extract and Organize Images:
import os
import shutil

def extract_images(source_folder, destination_folder):
    for root, _, files in os.walk(source_folder):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                source_path = os.path.join(root, file)
                shutil.copy(source_path, destination_folder)

def main():
    source_folder= 'C:/Users/Salma Ashraf/OneDrive/Desktop/ET3/dairies/dairies'
    destination_folder= 'C:/Users/Salma Ashraf/OneDrive/Desktop/ET3/images_dataset'
    
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    
    extract_images(source_folder, destination_folder)

if __name__ == "__main__":
    main()

#2. Extract images information while discarding the prefix from the images names:
import os
import csv
import datetime

# Function to extract the modified image name by discarding the prefix
def extract_info(image_filename):
    parts = image_filename.split("_", 1)  # Split the filename at the first underscore
    if len(parts) == 2:  # Check if there is a prefix 
        return parts[1]  # Return the part of the filename after the underscore
    return image_filename  # If no prefix, return the original filename

# Function to extract the modification date 
def format_modification_date(modification_timestamp):
    formatted_date = datetime.datetime.fromtimestamp(modification_timestamp).strftime('%a %b %d %H:%M:%S %Y')
    return formatted_date

# Function to extract the image size
def format_image_size(size_in_bytes):
    size_in_mb = size_in_bytes / (1024 * 1024)  # Convert bytes to megabytes
    formatted_size = f'{size_in_mb:.2f} MB'  # Format size with two decimal places
    return formatted_size

# Function to generate the CSV report
def generate_csv(images_folder, csv_filename):
    with open(csv_filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)  # Create a CSV writer object
        csv_writer.writerow(["Image Name", "Image Size", "Last Modification Date"])  # Write header row
        
        # Traverse through the files in the images_folder
        for root, _, files in os.walk(images_folder):
            for file in files:
                image_path = os.path.join(root, file) 
                image_name = extract_info(file)  # Extract modified image name using the function
                image_size = os.path.getsize(image_path)  # Get the size of the image in bytes
                modification_timestamp = os.path.getmtime(image_path)  # Get modification timestamp
                formatted_modification_date = format_modification_date(modification_timestamp)  # Format the date
                formatted_image_size = format_image_size(image_size)  # Format the image size
                
                # Write the extracted information to the CSV file
                csv_writer.writerow([image_name, formatted_image_size, formatted_modification_date])

def main():
    images_folder = "images_dataset"  # Path to the folder containing the images
    csv_filename = "image_report.csv"  # Name of the CSV report file
    
    generate_csv(images_folder, csv_filename)  # Call the function to generate the CSV report

if __name__ == "__main__":
    main()
