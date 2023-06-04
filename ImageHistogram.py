import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

from Constants import Constants
from Utils import get_image_name


def get_image_histogram(image_path):
    # Open the image file
    image = Image.open(image_path)

    # Convert the image to grayscale
    image_gray = image.convert('L')

    # Get the pixel values as a NumPy array
    pixels = np.array(image_gray)

    # Calculate the histogram using NumPy
    histogram, _ = np.histogram(pixels.flatten(), bins=256, range=[0, 256])

    return histogram


def save_histogram(histogram, image_name):
    plt.figure()
    plt.bar(range(256), histogram, color='gray')
    plt.title('Image Histogram')
    plt.xlabel('Pixel Intensity')
    plt.ylabel('Frequency')

    # Save the histogram plot
    output_path = Constants.OUTPUT_DIR + image_name + '_histogram.png'
    print (output_path)
    plt.savefig(output_path)


def get_histogram_statistic_image(image_path):
    histogram = get_image_histogram(image_path)
    save_histogram(histogram, get_image_name(image_path))