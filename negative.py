import csv
import os

import cv2


def sort_img():
    folder_dir = "C:/projects/negative/f_negative"
    list = []
    for i in os.listdir(folder_dir):
        img = cv2.imread(f'f_negative/{i}', cv2.IMREAD_GRAYSCALE)
        res_img = cv2.resize(img, (600, 600), cv2.INTER_NEAREST)
        grayscaleImage = cv2.equalizeHist(res_img)
        crop_img = grayscaleImage[400:600, 100:500]
        ret, threshold_image = cv2.threshold(crop_img, 110, 255, 0)
        (imageHeight, imageWidth) = threshold_image.shape[:2]
        whitePercent = cv2.countNonZero(threshold_image) / \
                                       (imageHeight * imageWidth)
        if whitePercent > 0.5:
            result = 'n'
        elif whitePercent < 0.5:
            result = 'p'
        dict = {'file_name': i, 'result': result}
        list.append(dict)
    with open('data.csv', 'w', encoding='utf-8', newline='') as f:
        fields = ['file_name', 'result']
        writer = csv.DictWriter(f, fields, delimiter=';')
        writer.writeheader()
        for i in list:
            writer.writerow(i)
    return


if __name__ == '__main__':
    sort_img()
