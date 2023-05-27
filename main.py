from ImageTransformation import image_to_one_dimension
from ImageTransformation import get_image_from_sequence
from LorenzEulerEncryption import discretization_lorenz_based_on_euler
from LorenzEulerEncryption import array_quantification


def xor_arrays(array1, array2):
    if len(array1) != len(array2):
        raise ValueError("Arrays must have the same length.")

    result = []
    for i in range(len(array1)):
        result.append(array1[i] ^ array2[i])

    return result


def xor_n(gray_array, cheie_fluida_octeti, n):
    enc_matrix1 = xor_arrays(gray_array, cheie_fluida_octeti)

    for i in range(n):
        x = xor_arrays(enc_matrix1, cheie_fluida_octeti)
        enc_matrix1 = x

    return enc_matrix1


def build_fluid_key(x_quantificated_sequence, length):
    return [int("0b" + "".join([str(x) for x in x_quantificated_sequence[k:k + 8]]), 2) for k in
            range(length)]


if __name__ == '__main__':
    image_path = r"C:\Users\pegeorge\Downloads/lfff.jpeg"
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

    decrypted_seq = xor_arrays(encryption_seq, fluid_key)

    decrypted_image = get_image_from_sequence(decrypted_seq, image_shape)
    decrypted_image.show()
