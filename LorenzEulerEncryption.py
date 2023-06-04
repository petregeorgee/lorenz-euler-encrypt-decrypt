import decimal
import os
from ImageTransformation import image_to_one_dimension
from ImageTransformation import get_image_from_sequence
from Utils import xor_arrays


def array_quantification(arr):
    transformed_arr = []
    sum = 0

    for num in arr:
        abs_val = abs(num)
        transformed_arr.append(get_last_digit_of_float(abs_val))
        sum += transformed_arr[-1]

    average = sum / len(transformed_arr)

    transformed_arr1 = [1 if num > average else 0 for num in transformed_arr]

    return transformed_arr1


def get_last_digit_of_float(abs_val):
    return decimal.Decimal(str(abs_val)).as_tuple().digits[-1]


def discretization_lorenz_based_on_euler(x0, y0, z0, n_steps, h):
    x = [x0]
    y = [y0]
    z = [z0]

    for step in range(n_steps):
        x_prev = x[step]
        y_prev = y[step]
        z_prev = z[step]

        x_next = x_prev + 10 * (y_prev - x_prev) * h
        y_next = y_prev + (28 * x_prev - y_prev - x_prev * z_prev) * h
        z_next = z_prev + (x_prev * y_prev - 8 * z_prev / 3) * h

        x.append(x_next)
        y.append(y_next)
        z.append(z_next)

    return x, y, z


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
    # decrypted_image.show()
    decrypted_path = os.path.dirname(image_path) + "/" + os.path.basename(image_path).split(".")[0] + "_decrypted.jpeg"
    decrypted_image.convert('L').save(decrypted_path)
    print(decrypted_path)


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
    # encrypted_image.show()
    enc_filename = os.path.dirname(image_path) + "/" + os.path.basename(image_path).split(".")[
        0] + "_encrypted" + ".png"
    encrypted_image.convert('L').save(enc_filename)
    print(enc_filename)