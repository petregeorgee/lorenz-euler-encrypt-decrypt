import sys

from LorenzEulerEncryption import encrypt
from LorenzEulerEncryption import decrypt
from ImageHistogram import get_histogram_statistic_image


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
