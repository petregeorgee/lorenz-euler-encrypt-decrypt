import sys

from ImageHistogram import get_histogram_statistic_image
from EncryptionAlgoritm import encrypt_image
from EncryptionAlgoritm import decrypt_image
from StatisticalAnalysis import image_entropy
from StatisticalAnalysis import calculate_adjacent_correlation
from StatisticalAnalysis import calculate_mse

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

    # #5.4.2. Entropy
    # image_entropy("img.png")
    # image_entropy("img_ENCRYPT.png")
    #
    # #5.4.3. Correlation of Adjacent Pixels
    # print(calculate_adjacent_correlation("img.png"))
    # print(calculate_adjacent_correlation("img_ENCRYPT.png"))
    #
    # print("Abaterea medie patratica (MSE) dintre imaginea initiala si cea criptata:")
    # print(calculate_mse("img.png", "img_ENCRYPT.png"))
