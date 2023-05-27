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


def image_to_gray_array(image_path):
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


def array_quantification(arr):
    transformed_arr = []
    sum_vals = 0

    for num in arr:
        abs_val = abs(num)
        # if abs_val < 0.1:
        #     transformed_arr.append(abs_val * 10)
        # elif abs_val > 1:
        #     transformed_arr.append(int(abs_val))
        # else:
        #     transformed_arr.append(abs_val)
        transformed_arr.append(decimal.Decimal(str(abs_val)).as_tuple().digits[-1])
        sum_vals += transformed_arr[-1]

    average = sum_vals / len(transformed_arr)

    transformed_arr1 = [1 if num > average else 0 for num in transformed_arr]

    return transformed_arr1


def discretization_lorenz_based_on_euler(x0, y0, z0, n_steps, h):
    # Initialize arrays to store the results
    x = [x0]
    y = [y0]
    z = [z0]

    # Perform the calculation for the specified number of steps
    for step in range(n_steps):
        x_prev = x[step]
        y_prev = y[step]
        z_prev = z[step]

        x_next = x_prev + 10 * (y_prev - x_prev) * h
        y_next = y_prev + (28 * x_prev - y_prev - x_prev * z_prev) * h
        z_next = z_prev + (x_prev * y_prev - 8 * z_prev / 3) * h

        # x_next = x_prev + 10 * (y_prev - x_prev) * h
        # y_next = y_prev + (x_prev * (28 - z_prev) - y_prev) * h
        # z_next = z_prev + (x_prev * y_prev - 8 * z_prev / 3) * h

        x.append(x_next)
        y.append(y_next)
        z.append(z_next)

    # Combine the arrays into a single three-dimensional array
    # result_array = np.array([x, y, z])
    y = array_quantification(y)
    return y
