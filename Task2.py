import json

def text_to_json(input_text_filename, output_json_filename):
    # Initialize a dictionary structure for storing annotations
    annotations = {
        "annotations": [
            {
                "result": []  # List to hold individual object annotations
            }
        ],
        "data": {
            "image": "C:/Users/Salma Ashraf/OneDrive/Desktop/ET3/images_dataset/Arla-Ecological-Medium-Fat-Milk_001.jpg" # The image path
        }
    }

    # Open the input text file for reading
    with open(input_text_filename, 'r') as txt_file:
        for line in txt_file:
            # Parse the line and extract relevant information
            parts = line.strip().split(' ')
            if len(parts) >= 5:
                label, x, y, width, height = map(float, parts[:5])

                # Create an annotation dictionary for each object
                annotation = {
                    "image_rotation": 0,
                    "value": {
                        "x": x,
                        "y": y,
                        "width": width,
                        "height": height,
                        "rotation": 0,
                        "rectanglelabels": ["object"]
                    }
                }
                # Append the annotation to the list of annotations
                annotations["annotations"][0]["result"].append(annotation)

    # Open the output JSON file for writing
    with open(output_json_filename, 'w') as json_file:
        # Write the annotations dictionary to the JSON file with indentation
        json.dump(annotations, json_file, indent=4)

def main():
    # Specify the input text file and desired output JSON filename
    input_text_filename = "C:/Users/Salma Ashraf/OneDrive/Desktop/ET3/image1.txt"  # The input text file
    output_json_filename = "output.json"  # The Output JSON file

    # Performing the transformation
    text_to_json(input_text_filename, output_json_filename)

if __name__ == "__main__":
    main()
