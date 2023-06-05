import sys

from ImageHistogram import get_histogram_statistic_image
from EncryptionAlgoritm import encrypt_image
from EncryptionAlgoritm import decrypt_image


if __name__ == '__main__':

    if sys.argv.__len__() > 1:
        path = sys.argv[1]
        operation = sys.argv[2]
    else:
        raise Exception("Not enough arguments provided. ")


    if operation == 'ENCRYPT':
        encrypt_image(path, operation)
    elif operation == 'DECRYPT':
        decrypt_image(path, operation)
    elif operation == 'HISTOGRAM':
        get_histogram_statistic_image(path)
