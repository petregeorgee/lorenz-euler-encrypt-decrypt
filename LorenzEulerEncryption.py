import decimal
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


def decrypt(image_array):
    x0 = 0.02
    y0 = 0.01
    z0 = 0.03
    h = 0.001

    n_steps = image_array.size - 1
    x, y, z = discretization_lorenz_based_on_euler(x0, y0, z0, n_steps, h)
    x_quantificated_sequence = array_quantification(x)
    fluid_key = build_fluid_key(x_quantificated_sequence, len(image_array))

    decryption_seq = xor_arrays(image_array, fluid_key)
    return decryption_seq


def build_fluid_key(x_quantificated_sequence, length):
    return [int("0b" + "".join([str(x) for x in x_quantificated_sequence[k:k + 8]]), 2) for k in
            range(length)]


def encrypt(image_array):
    x0 = 0.02
    y0 = 0.01
    z0 = 0.03
    h = 0.001
    n_steps = image_array.size - 1
    x, y, z = discretization_lorenz_based_on_euler(x0, y0, z0, n_steps, h)
    x_quantificated_sequence = array_quantification(x)
    fluid_key = build_fluid_key(x_quantificated_sequence, len(image_array))

    encryption_seq = xor_arrays(image_array, fluid_key)
    return encryption_seq
