import numpy as np


def get_average(numbers):
    # Перетворюємо список у масив numpy
    arr = np.array(numbers)
    # np.mean рахує середнє значення
    return np.mean(arr)
