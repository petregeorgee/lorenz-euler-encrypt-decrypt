import os

from ImageTransformation import get_image_from_sequence, image_to_one_dimension
from LorenzEulerEncryption import encrypt
from LorenzEulerEncryption import decrypt

from ArrayPermutation import permute_pixel_array
from ArrayPermutation import unpermute_array


def encrypt_image(image_path, operation):
    image_to_one_dimension_array, image_shape = image_to_one_dimension(image_path)

    lorenz_encryption_sq = encrypt(image_to_one_dimension_array)
    permuted_pixels_array = permute_pixel_array(lorenz_encryption_sq, image_shape)

    encrypted_image = get_image_from_sequence(permuted_pixels_array, image_shape)
    # encrypted_image.show()
    write_image_to_disk(encrypted_image, image_path, operation)


def write_image_to_disk(image, image_path, operation):
    enc_filename = os.path.dirname(image_path) + "/" + os.path.basename(image_path).split(".")[
        0] + "_" + operation + ".png"
    image.convert('L').save(enc_filename)
    print(enc_filename)


def decrypt_image(image_path, operation):
    image_to_one_dimension_array, image_shape = image_to_one_dimension(image_path)

    unpermuted_pixels_array = unpermute_array(image_to_one_dimension_array, image_shape)
    lorenz_decrypted_sq = decrypt(unpermuted_pixels_array)

    decrypted_image = get_image_from_sequence(lorenz_decrypted_sq, image_shape)
    # decrypted_image.show()
    write_image_to_disk(decrypted_image, image_path, operation)
