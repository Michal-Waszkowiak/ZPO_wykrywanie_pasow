import os
from PIL import Image

def convert_png_to_jpg(input_folder, output_folder):
    """
    Converts all PNG images in the input_folder to JPG format and saves them to the output_folder.

    Args:
        input_folder (str): Path to the folder containing PNG images.
        output_folder (str): Path to the folder to save converted JPG images.
    """
    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Iterate through files in the input folder
    for file_name in os.listdir(input_folder):
        if file_name.lower().endswith('.png'):
            # Full path to the PNG file
            png_path = os.path.join(input_folder, file_name)

            # Open the image
            with Image.open(png_path) as img:
                # Convert to RGB (JPG does not support transparency)
                rgb_image = img.convert('RGB')

                # Save as JPG with the same base name
                jpg_file_name = os.path.splitext(file_name)[0] + '.jpg'
                jpg_path = os.path.join(output_folder, jpg_file_name)

                rgb_image.save(jpg_path, format='JPEG')

                print(f"Converted: {file_name} -> {jpg_file_name}")

# Example usage
input_folder = "C:\\Users\\User1\\Downloads\\Plewiska-Komorniki-20241213T104306Z-001\\Plewiska-Komorniki\\Images"  # Replace with the path to your folder with PNG images
output_folder = "C:\\Users\\User1\\Downloads\\Plewiska-Komorniki-20241213T104306Z-001\\Plewiska-Komorniki\\jpg"  # Replace with the path where JPG images should be saved

convert_png_to_jpg(input_folder, output_folder)