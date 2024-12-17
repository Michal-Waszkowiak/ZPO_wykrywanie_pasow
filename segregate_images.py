import os
import shutil
from pathlib import Path

def segregate_images(input_folder, output_folder):
    """
    Segregates images into separate folders based on their format (JPG and PNG).

    Parameters:
        input_folder (str): Path to the folder containing images.
        output_folder (str): Path to the folder where sorted images will be saved.
    """
    # Define paths for output folders
    jpg_folder = os.path.join(output_folder, 'jpg')
    png_folder = os.path.join(output_folder, 'png')

    # Create output folders if they don't exist
    os.makedirs(jpg_folder, exist_ok=True)
    os.makedirs(png_folder, exist_ok=True)

    # Iterate through all files in the input folder
    for file in Path(input_folder).iterdir():
        if file.is_file():
            # Check the file extension and move to the appropriate folder
            if file.suffix.lower() == '.jpg':
                shutil.move(str(file), os.path.join(jpg_folder, file.name))
            elif file.suffix.lower() == '.png':
                shutil.move(str(file), os.path.join(png_folder, file.name))

if __name__ == "__main__":
    input_folder = "C:\\Users\\User1\\Downloads\\dawid\\test"
    output_folder = "C:\\Users\\User1\\Downloads\\output"

    segregate_images(input_folder, output_folder)
    print("Obrazy zostały posegregowane.")