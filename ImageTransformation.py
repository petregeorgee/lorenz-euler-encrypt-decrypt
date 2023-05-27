import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import decimal


def image_processing(image_path):
    # Load the image using PIL
    image = Image.open(image_path).convert('L')  # Convert to grayscale

    # Display the original image
    plt.subplot(1, 2, 1)
    plt.imshow(image, cmap='gray')
    plt.title('Original Image')

    # Convert the image to a NumPy array
    image_array = np.array(image)

    # Get the dimensions of the image
    height, width = image_array.shape

    # Convert the image matrix into a one-dimensional array
    flattened_array = image_array.flatten()

    # Display the flattened array
    plt.subplot(1, 2, 2)
    plt.plot(flattened_array)
    plt.title('Flattened Array')

    # Show the plots
    plt.tight_layout()
    plt.show()


def image_to_one_dimension(image_path):
    # Load the image
    image = Image.open(image_path).convert('L')

    # Save the image
    # image.save(r"C:\Users\pegeorge\Downloads\la\image.jpeg")

    # Convert the image to a grayscale pixel matrix
    gray_matrix = np.array(image)
    # Image.fromarray(gray_matrix).show()

    # Flatten the grayscale matrix into a one-dimensional array
    flat_array = gray_matrix.flatten()

    return flat_array, gray_matrix.shape


def get_image_from_sequence(encryption_seq, image_shape):
    global numpy_array

    numpy_array = np.array(encryption_seq)
    # numpy_array
    enc_matrix = numpy_array.flatten().reshape(image_shape)
    return Image.fromarray(enc_matrix)


