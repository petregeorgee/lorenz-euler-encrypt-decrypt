from PIL import Image
import os


def change_pixel(image_path, pixel_coordinates, new_pixel_value):
    # Open the image using PIL
    image = Image.open(image_path)

    # Convert the image to RGB mode if it's not already
    image = image.convert("RGB")

    # Load the image pixels
    pixels = image.load()

    # Extract the coordinates of the pixel to be changed
    x, y = pixel_coordinates

    # Change the pixel value
    pixels[x, y] = new_pixel_value

    # Save the modified image
    filename = os.path.basename(image_path)
    new_image_path = os.path.join(os.path.dirname(image_path), f"modified_{filename}")
    image.save(new_image_path)

    return new_image_path
