import cv2
import numpy as np

image = cv2.imread('images/variant-9.jpg')

if image is None:
    print("Ошибка: Изображение не найдено.")
    exit()

def build_image_pyramid(image, levels=3):
    pyramid = [image]
    for _ in range(levels - 1):
        image = cv2.pyrDown(image)
        pyramid.append(image)
    return pyramid

pyramid = build_image_pyramid(image)

for i, level in enumerate(pyramid):
    cv2.imshow(f'Level {i}', level)
cv2.waitKey(0)
cv2.destroyAllWindows()
