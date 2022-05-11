import cv2
import os
from cv2 import threshold
from matplotlib.pyplot import show
import numpy as np


RADIUS = 10
THRESHOLD = 200


def show_image(image):
    cv2.imshow('image',image)
    c = cv2.waitKey()
    if c >= 0 : return -1
    return 0


def path(p):
    return os.getcwd() + p


def get_image(file):
    return cv2.imread(path(f'\images_source\{file}'))


def wrong_contour_dimensions(w, h):
    if w<RADIUS*3 or h < RADIUS*3:
       return True
    return False


def get_contours(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    median = cv2.medianBlur(gray,5)
    blur = cv2.bilateralFilter(median,8,75,75)
    _, threshold = cv2.threshold(blur, THRESHOLD, 255, cv2.THRESH_BINARY_INV)

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (RADIUS,RADIUS))
    gradient = cv2.morphologyEx(threshold, cv2.MORPH_GRADIENT, kernel)


    contours, chierarchy = cv2.findContours(gradient, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    return contours



def write_image(image, contour, name, id):
    x,y,w,h = cv2.boundingRect(contour)
    if wrong_contour_dimensions(w, h):
        return
    radius = int(RADIUS / 2) + 1
    ROI = image[y+radius:y+h-radius, x+radius:x+w-radius]
    cv2.imwrite(path(f'\images_target\{name}_{id}.png'), ROI)


def write_images(image, contours, name):
    for i, contour in enumerate(contours):
        write_image(image, contour, name, i)


def get_source_images(folder):
    source_path = path(folder)
    return [f for f in os.listdir(source_path) if os.path.isfile(os.path.join(source_path, f))]


def process_file(file):
    name = file.split('.')[0]
    image = get_image(file)
    contours = get_contours(image)
    write_images(image, contours, name)


def main():
    onlyfiles = get_source_images('\images_source')
    for file in onlyfiles:
        process_file(file)


if __name__ == '__main__':
    main()

