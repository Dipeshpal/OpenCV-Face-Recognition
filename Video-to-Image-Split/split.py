import cv2
import os


def split():

    dir_name = input("Enter folder name: ")
    video_name = input("Enter video name: ")

    os.mkdir(dir_name)

    vidcap = cv2.VideoCapture(video_name)
    success, image = vidcap.read()
    count = 0
    success = True
    while success:
        success, image = vidcap.read()
        cv2.imwrite(os.path.join(dir_name, "frame%d.jpg" % count), image)
        print('Read a new frame: ', success)
        count += 1

split()
