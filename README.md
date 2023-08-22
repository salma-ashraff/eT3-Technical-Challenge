Overview:
This documentation outlines the solution for two tasks: 
1. Processing a dataset of images stored in various folders and sub-folders.
2. Transforming the output of an image detection system into a JSON format suitable for further processing. The provided solution encompasses Python programming to achieve these tasks.

Task1.py file:

Involves collecting images from nested folders and placing them into a single folder while extracting relevant information about each image. The key steps involved are:

-Collecting images: The code extracts the images and move them to a specified destination folder named "images_dataset."

-Rename the images: The prefix of each image name is removed.

-Generate CSV Report: The code creates a CSV report named 'image_report.csv' that contains the following details for each image:
Image name (without the prefix)
Image size
Last modification date of the image content

Task2.py file:

Involves transforming the output of an image detection system, which consists of a TXT file with object detection information, into a JSON format for further processing. The steps to achieve this are:

-Parse TXT File: The code reads each line of the TXT file, the txt file used named 'image1.txt', and extracts object detection information, such as coordinates and dimensions of the detected objects.

-JSON Transformation: The extracted object detection information is transformed into a JSON structure, the output named "output.json" with the following attributes:
annotations: A list containing detection results, where each result is represented as a dictionary.
result: A list containing dictionaries, each representing a detected object with attributes like x, y, width, and height.

Running the Solution:
1. Ensure having Python installed on your system.
2. Open a terminal or command prompt and navigate to the directory containing the script.
4. The script will process the image dataset and generate a report CSV file. It will also transform the detection system's TXT output into a JSON file.
5. The generated images will be located in the "images_dataset" folder, and the CSV report and Output JSON file will be created in the same directory as the script.
   
