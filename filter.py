from PIL import Image
import numpy as np
img = Image.open(input())
pixels = np.array(img)

def get_gray(pix_width, pix_height, x, y):
    result = np.sum(pixels[pix_width: pix_width + x,pix_height: pix_height + y ]) / 3
    result = int(result // (x * y))
    return result


def replace_pixels(pix_width, x, pix_height, y, step_gray):
    gray = get_gray(pix_width, pix_height, x, y)
    pixels[pix_width: pix_width + x,pix_height: pix_height + y ] = int(gray // step_gray) * step_gray


def get_gray_img(x, y, step_gray):
    height = len(pixels)
    width = len(pixels[1])
    pix_width = 0
    while pix_width < height:
        pix_height = 0
        while pix_height < width:
            replace_pixels(pix_width, x, pix_height, y, step_gray)
            pixels_y = pix_height + y
        pix_width = pix_width + x
    return pixels

mozaik = input(('Enter width, height, gray step')).split()
name = input(('Enter name of the result file')) + '.jpg'

Image.fromarray(get_gray_img(int(mozaik[0]), int(mozaik[1]), int(mozaik[2]))).save(name)
