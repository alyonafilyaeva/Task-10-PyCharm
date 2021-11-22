from PIL import Image
import numpy as np
img = Image.open('img2.jpg')
pixels = np.array(img)

def get_gray(pix_width, pix_height, x, y):
    result = np.sum(pixels[pix_width: pix_width + x,pix_height: pix_height + y ]) / 3
    result = int(result // (x * y))
    return result


def replace_pixels(pix_width, x, pix_height, y, step_gray):
    gray = get_gray(pix_width, pix_height, x, y)
    pixels[pix_width: pix_width + x,pix_height: pix_height + y] = int(gray // step_gray) * step_gray


def get_gray_img(x, y, step_gray):
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



Image.fromarray(get_gray_img(10, 10, 50)).save('yes.jpg')
