import os

from PIL import Image

# Replace these paths with your desired input and output folders
input_images_folder = "./input"
output_images_folder = "./output"


def reduce_image_size(input_folder, output_folder, quality=85):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Loop through all files in the input folder
    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        if os.path.isfile(input_path):
            # Open the image using Pillow
            img = Image.open(input_path)

            # Compress and save the image with the specified quality
            img.save(output_path, optimize=True, quality=quality)
            print(f"Compressed {filename} saved to {output_folder}")


if __name__ == "__main__":
    # Call the function to reduce image sizes
    reduce_image_size(input_images_folder, output_images_folder)
