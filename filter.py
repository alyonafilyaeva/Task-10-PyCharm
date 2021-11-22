import doctest

from PIL import Image
import numpy as np


def get_gray(pix_width, pix_height, x, y):
    """
        Вычисляет "шаг" серого цвета и возвращает среднюю яркость
        >>> get_gray(10, 10, 10, 10)
        19
         >>> get_gray(10, 20, 10, 20)
        20
    """
    result = np.sum(pixels[pix_width: pix_width + x,pix_height: pix_height + y ]) / 3
    result = int(result // (x * y))
    return result


def replace_pixels(pix_width, x, pix_height, y, step_gray):
    """
        Закрашивает каждый пиксель в один цвет средней яркости
    """
    gray = get_gray(pix_width, pix_height, x, y)
    pixels[pix_width: pix_width + x,pix_height: pix_height + y] = int(gray // step_gray) * step_gray


def get_gray_img(x, y, step_gray):
    """
        Возвращает новое обработанное фильтром изображение
    """
    height = len(pixels)
    width = len(pixels[1])
    pix_width = 0
    while pix_width < height:
        pix_height = 0
        while pix_height < width:
            replace_pixels(pix_width, x, pix_height, y, step_gray)
            pix_height = pix_height + y
        pix_width = pix_width + x
    return pixels

if __name__ == '__main__':
    doctest.testmod()

img = Image.open(input('Enter file name'))
pixels = np.array(img)

mozaik = input(('Enter width, height, gray step')).split()
name = input(('Enter name of the result file')) + '.jpg'

Image.fromarray(get_gray_img(int(mozaik[0]), int(mozaik[1]), int(mozaik[2]))).save(name)

