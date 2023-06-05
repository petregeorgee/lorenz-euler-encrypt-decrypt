import sys
import numpy as np

from LorenzEulerEncryption import encrypt
from LorenzEulerEncryption import decrypt
from ImageHistogram import get_histogram_statistic_image
from Dascalescu import get_permutation
from Dascalescu import generate_logistic_map

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


if __name__ == '__main__':

    if sys.argv.__len__() > 1:
        path = sys.argv[1]
        operation = sys.argv[2]
    else:
        raise Exception("Not enough arguments provided. ")

    l_map = get_permutation(path)
    # print(l_map)
    #
    # pixeli = [100, 97, 10, 203, 48, 100, 56, 77]
    # print("  Pixeli initiali: ", pixeli)
    #
    # order = [7, 3, 2, 6, 4, 5, 1, 0]
    #
    # perm_pixels = permute_pixels(pixeli, order)
    # print(perm_pixels)
    #
    # restored_arr = restore_pixels(perm_pixels, order)
    # print(restored_arr)
    # if operation == 'ENCRYPT':
    #     encrypt(path)
    # elif operation == 'DECRYPT':
    #     decrypt(path)
    # elif operation == 'HISTOGRAM':
    #     get_histogram_statistic_image(path)
