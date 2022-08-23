import pandas as pd
import numpy as np
import cv2
import keyboard
import random
import time



def main():
    cap = cv2.VideoCapture(1)
    count = 0
    folderNumber = random.randint(0, 1000)
    print("folderNumber = ", folderNumber)
    while (True):

        ret, frame = cap.read()

        if ret and keyboard.is_pressed('s'):
            cv2.imwrite("ChessFrames"+str(folderNumber)+"/frame%d.jpg" % count, frame)
            count = count + 1
            time.sleep(2)
        if keyboard.is_pressed('q'):
            time.sleep(1)
            break





    # Close down the video stream
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    print(__doc__)
    main()

