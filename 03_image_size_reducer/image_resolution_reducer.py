import os

from PIL import Image

# Replace these paths with your desired input and output folders
input_images_folder = "./input"
output_images_folder = "./output"

# Set the maximum dimension for the images (width or height)
max_image_dimension = 1920  # Change this value as needed


def reduce_image_size_with_resizing(
    input_folder, output_folder, max_dimension, quality=85
):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Walk through the directory structure
    for root, dirs, files in os.walk(input_folder):
        for filename in files:
            input_path = os.path.join(root, filename)
            relative_path = os.path.relpath(input_path, input_folder)
            output_path = os.path.join(output_folder, relative_path)

            if not os.path.exists(os.path.dirname(output_path)):
                os.makedirs(os.path.dirname(output_path))

            if os.path.isfile(input_path):
                # Open the image using Pillow
                img = Image.open(input_path)

                # Calculate new size while maintaining aspect ratio
                img.thumbnail((max_dimension, max_dimension))

                # Compress and save the image with the specified quality
                img.save(output_path, optimize=True, quality=quality)
                print(f"Resized and compressed {filename} saved to {output_folder}")


if __name__ == "__main__":
    # Call the function to reduce image sizes and resize if needed
    reduce_image_size_with_resizing(
        input_images_folder, output_images_folder, max_image_dimension
    )
