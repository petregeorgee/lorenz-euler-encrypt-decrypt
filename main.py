from ImageTransformation import image_to_one_dimension
from ImageTransformation import get_image_from_sequence
from LorenzEulerEncryption import discretization_lorenz_based_on_euler
from LorenzEulerEncryption import array_quantification
import sys
import os

from ImageHistogram import get_image_histogram
from ImageHistogram import save_histogram

def xor_arrays(array1, array2):
    if len(array1) != len(array2):
        raise ValueError("Arrays must have the same length.")

    result = []
    for i in range(len(array1)):
        result.append(array1[i] ^ array2[i])

    return result


def build_fluid_key(x_quantificated_sequence, length):
    return [int("0b" + "".join([str(x) for x in x_quantificated_sequence[k:k + 8]]), 2) for k in
            range(length)]


def encrypt(image_path):
    image_to_one_dimension_array, image_shape = image_to_one_dimension(image_path)
    x0 = 0.02
    y0 = 0.01
    z0 = 0.03
    h = 0.001
    n_steps = image_to_one_dimension_array.size - 1
    x, y, z = discretization_lorenz_based_on_euler(x0, y0, z0, n_steps, h)
    x_quantificated_sequence = array_quantification(x)
    fluid_key = build_fluid_key(x_quantificated_sequence, len(image_to_one_dimension_array))

    encryption_seq = xor_arrays(image_to_one_dimension_array, fluid_key)

    encrypted_image = get_image_from_sequence(encryption_seq, image_shape)
    encrypted_image.show()
    enc_filename = os.path.dirname(image_path) + "/" + os.path.basename(image_path).split(".")[0] + "_encrypted" + ".png"
    encrypted_image.convert('L').save(enc_filename)
    print(enc_filename)


def build_array_from_file(filename):
    array = []
    with open(filename, 'r') as file:
        for line in file:
            element = line.strip()
            array.append(int(element))
    return array


def decrypt(image_path):
    image_to_one_dimension_array, image_shape = image_to_one_dimension(image_path)

    x0 = 0.02
    y0 = 0.01
    z0 = 0.03
    h = 0.001

    n_steps = image_to_one_dimension_array.size - 1
    x, y, z = discretization_lorenz_based_on_euler(x0, y0, z0, n_steps, h)
    x_quantificated_sequence = array_quantification(x)
    fluid_key = build_fluid_key(x_quantificated_sequence, len(image_to_one_dimension_array))

    decryption_seq = xor_arrays(image_to_one_dimension_array, fluid_key)
    decrypted_image = get_image_from_sequence(decryption_seq, image_shape)
    decrypted_image.show()
    decrypted_path = os.path.dirname(image_path) + "/" + os.path.basename(image_path).split(".")[0] + "_decrypted.jpeg"
    decrypted_image.convert('L').save(decrypted_path)
    print(decrypted_path)


def get_image_name(path):
    # Get the base name of the file from the path
    file_name = os.path.basename(path)

    # Remove the extension from the file name
    image_name = os.path.splitext(file_name)[0]

    return image_name


def get_histogram_statistic_image(image_path):
    histogram = get_image_histogram(image_path)
    save_histogram(histogram, get_image_name(image_path))


if __name__ == '__main__':
    if sys.argv.__len__() > 1:
        path = sys.argv[1]
        operation = sys.argv[2]
    else:
        raise Exception("Not enough arguments provided. ")

    if operation == 'ENCRYPT':
        encrypt(path)
    elif operation == 'DECRYPT':
        decrypt(path)
    elif operation == 'HISTOGRAM':
        get_histogram_statistic_image(path)
