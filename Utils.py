import os


def xor_arrays(array1, array2):
    if len(array1) != len(array2):
        raise ValueError("Arrays must have the same length.")

    result = []
    for i in range(len(array1)):
        result.append(array1[i] ^ array2[i])

    return result


def build_array_from_file(filename):
    array = []
    with open(filename, 'r') as file:
        for line in file:
            element = line.strip()
            array.append(int(element))
    return array


def get_image_name(path):
    # Get the base name of the file from the path
    file_name = os.path.basename(path)

    # Remove the extension from the file name
    image_name = os.path.splitext(file_name)[0]

    return image_name
