import os
import random

import numpy as np

from ImageTransformation import image_to_one_dimension
from ImageTransformation import get_image_from_sequence


def generate_permutation(n, d):
    L = [0] * (n + 1)
    q = [0] * (n + 1)
    max_val = n + 1

    for i in range(1, n):
        q[i] = 1 + d[i] % n
        while L[q[i]] == 1:
            k = max_val - 1
            while L[k] == 1:
                k -= 1
            q[i] = k
            max_val = k
        L[q[i]] = 1

    return q[1:]


def get_permutation(image_path):
    image_to_one_dimension_array, image_shape = image_to_one_dimension(image_path)

    n = image_shape[0] * image_shape[1]
    d = generate_logistic_map(4, 0.12121212121, n)
    # print_array_to_file(d, "C:\Repo\images\\d.txt")

    permutation = generate_permutation(n, d)
    # print_array_to_file(permutation, "C:\Repo\images\\permutation.txt")

    # print_array_to_file(permutation, "C:\Repo\images\\y.txt")

    permuted_array = permute_pixels(image_to_one_dimension_array, permutation)
    permuted_image = get_image_from_sequence(permuted_array, image_shape)
    permuted_image.show()

    unpermuted_array = restore_pixels(permuted_array, permutation)
    unpermuted_image = get_image_from_sequence(unpermuted_array, image_shape)
    unpermuted_image.show()
    # permuted_filename = os.path.dirname(image_path) + "/" + os.path.basename(image_path).split(".")[
    #     0] + "_permuted" + ".png"
    # permuted_image.convert('L').save(permuted_filename)
    # print(permuted_image)


def generate_logistic_map(r, x0, n):
    array = [x0]

    for i in range(1, n + 1):
        difference = 1 - array[i - 1]
        difference = f'{difference:.16f}'
        xn = r * array[i - 1] * float(difference)
        array.append(xn)

    array1 = []
    for i in range(1, n + 1):
        frac = (int(float(str(array[i])[2:]))) % n + 1
        array1.append(frac)

    # array1.pop(0)
    return array1


def replace_repeating_elements(array):
    max_val = len(array)
    current_max = max(array)
    unique_set = set()

    for i in range(len(array)):
        if array[i] in unique_set:
            while current_max in unique_set:
                current_max -= 1
            array[i] = current_max
            unique_set.add(current_max)
            current_max -= 1
        else:
            unique_set.add(array[i])

    return array


def print_array_to_file(array, file_name):
    with open(file_name, 'w') as file:
        for element in array:
            file.write(str(element) + '\n')


def permute_pixels(pixel_array, order):
    assert len(pixel_array) == len(order), "Pixel array and order must have the same length"

    # Create a copy of the pixel array
    permuted_array = np.array(pixel_array, copy=True)

    # Generate the permutation indices
    permutation_indices = np.argsort(order)

    # Permute the pixel array
    permuted_array = permuted_array[permutation_indices]

    return permuted_array

def restore_pixels(permuted_array, order):
    assert len(permuted_array) == len(order), "Permuted array and order must have the same length"

    # Create a copy of the permuted array
    restored_array = np.array(permuted_array, copy=True)

    # Generate the inverse permutation indices
    inverse_indices = np.argsort(np.argsort(order))

    # Restore the pixel array
    restored_array = restored_array[inverse_indices]

    return restored_array

