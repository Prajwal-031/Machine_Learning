import cv2
import os
from PIL import Image
 
 
def process_image(image_path):
    """Process a single image and determine its type."""
    # Load the image in an unchanged format
    image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
    
    # Check if the image was loaded successfully
    if image is None:
        return f"Error: Unable to load the image at '{image_path}'."
    
    # Determine the image type based on its shape
    if len(image.shape) == 2:
        return f"The image is grayscale with shape: {image.shape}"
    elif len(image.shape) == 3:
        if image.shape[2] == 3:
            return f"The image is an RGB image with shape: {image.shape}"
        elif image.shape[2] == 4:
            return f"The image is an RGBA image with shape: {image.shape}"
        else:
            return f"The image has an unexpected number of channels: {image.shape[2]} (shape: {image.shape})"
    else:
        return f"Unexpected image shape: {image.shape}"

def process_dataset(folder_path):
    """Process all images in a folder and subfolders."""
    if not os.path.exists(folder_path):
        print(f"Error: Folder path '{folder_path}' does not exist.")
        return

    # Traverse the folder and process each image file
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                result = process_image(file_path)
                print(f"File: {file_path}\n{result}\n")
            except Exception as e:
                print(f"Error processing file '{file_path}': {e}")

# Input folder path or file path
folder_path = input("Enter the folder path containing MRI images: ").strip()
process_dataset(folder_path)
