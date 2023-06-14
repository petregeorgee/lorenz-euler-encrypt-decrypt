import numpy as np
import skimage.io as io
from scipy.stats import entropy
from ImageHistogram import get_image_histogram
from PIL import Image


def image_entropy(image_path):
    histogram = get_image_histogram(image_path)
    histogram = histogram.astype(float) / np.sum(histogram)
    image_entropy = entropy(histogram, base=2)

    print("Image entropy:", image_entropy)


def calculate_adjacent_correlation(image_path):
    # Open the image file
    image = Image.open(image_path)

    # Convert the image to grayscale
    gray_image = image.convert('L')

    # Normalize the pixel values to the range [0, 1]
    normalized_image = np.asarray(gray_image, dtype=float) / 255.0

    # Calculate correlations along vertical, horizontal, and diagonal directions
    vertical_correlation = np.corrcoef(normalized_image[:-1, :].flatten(), normalized_image[1:, :].flatten())[0, 1]
    horizontal_correlation = np.corrcoef(normalized_image[:, :-1].flatten(), normalized_image[:, 1:].flatten())[0, 1]
    diagonal_correlation = np.corrcoef(normalized_image[:-1, :-1].flatten(), normalized_image[1:, 1:].flatten())[0, 1]

    return vertical_correlation, horizontal_correlation, diagonal_correlation


def calculate_mse(image1_path, image2_path):
    # Load the images
    image1 = np.array(Image.open(image1_path))
    image2 = np.array(Image.open(image2_path))

    # Convert the images to grayscale
    gray_image1 = np.mean(image1.flatten())
    gray_image2 = np.mean(image2.flatten())

    # Calculate the Mean Squared Deviation (MSE)
    mse = np.mean((gray_image1 - gray_image2) ** 2)

    return mse
