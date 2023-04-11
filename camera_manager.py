import cv2
import time
import os

cam_url = "Ссылка на камеру"
#Пример 'https://cctv-sa3-b2b.yar.vs.ertelecom.ru:18080/rtsp/281469713/a9712fafc57b84e503ab/playlist.m3u8'


def make_timelaps():
    while True:
        try:
            cap = cv2.VideoCapture(cam_url)
            cap.set(cv2.CAP_PROP_BUFFERSIZE, 3)
            counter = 0
            ret, frame = cap.read()
            print(str(ret))
            if ret:
                cv2.imwrite(os.path.join(os.getcwd(), 'images', str(time.time()) + '.jpg'), frame)
                counter = counter + 1
        except Exception as e:
            print(e)
            continue
        time.sleep(20)
