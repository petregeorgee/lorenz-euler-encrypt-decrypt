# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from ImageTransformation import image_to_gray_array
from ImageTransformation import discretization_lorenz_based_on_euler
from ImageTransformation import image_processing
import numpy as np
from PIL import Image


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def xor_arrays(array1, array2):
    if len(array1) != len(array2):
        raise ValueError("Arrays must have the same length.")

    result = []
    for i in range(len(array1)):
        result.append(array1[i] ^ array2[i])

    return result

def test():
    import random

    pixeli = [100, 97, 10, 203, 48, 100, 56, 77]
    print("  Pixeli initiali: ", pixeli)
    # lungimea cheii fluide = 8 * numar_pixeli = 64 biti
    cheia_fluida_biti = [random.randint(0, 1) for x in range(8 * len(pixeli))]
    # print(cheia_fluida_biti)
    cheie_fluida_octeti = [int("0b" + "".join([str(x) for x in cheia_fluida_biti[k:k + 8]]), 2) for k in
                           range(len(pixeli))]
    print("     Cheie fluida: ", cheie_fluida_octeti)

    criptare = [0] * len(pixeli)

    for i in range(len(pixeli)):
        criptare[i] = pixeli[i] ^ cheie_fluida_octeti[i]
    print("Pixeli criptati: ", criptare)

    decriptare = [0] * len(pixeli)
    for i in range(len(pixeli)):
        decriptare[i] = criptare[i] ^ cheie_fluida_octeti[i]
    print("Pixeli decriptati: ", decriptare)


def xor_n(gray_array, cheie_fluida_octeti, n):
    enc_matrix1 = xor_arrays(gray_array, cheie_fluida_octeti)

    for i in range(n):
        x = xor_arrays(enc_matrix1, cheie_fluida_octeti)
        enc_matrix1 = x

    return enc_matrix1


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # test()
    image_path = r"C:\Users\pegeorge\Downloads/lfff.jpeg"
    gray_array, shape = image_to_gray_array(image_path)

    x0 = 0.02
    y0 = 0.01
    z0 = 0.03
    h = 0.001
    n_steps = gray_array.size - 1

    x_direction_output_sequence = discretization_lorenz_based_on_euler(x0, y0, z0, n_steps, h)
    cheie_fluida_octeti = [int("0b" + "".join([str(x) for x in x_direction_output_sequence[k:k + 8]]), 2) for k in
                           range(len(gray_array))]
    encryption_seq = xor_arrays(gray_array, cheie_fluida_octeti)
    # print(encryption_seq)

    # print(result_array)
    # image_processing(image_path)
    numpy_array = np.array(encryption_seq)
    # numpy_array
    enc_matrix = numpy_array.flatten().reshape(shape)
    # print(enc_matrix)

    image = Image.fromarray(enc_matrix)
    image.show()  # Display the image

    # decripted_matrix = image_to_gray_array(enc_matrix)
    dencrypted_seq = xor_arrays(encryption_seq, cheie_fluida_octeti)

    numpy_array = np.array(dencrypted_seq)
    # numpy_array
    denc_matrix = numpy_array.flatten().reshape(shape)
    image = Image.fromarray(denc_matrix)
    image.show()  # Display the image
