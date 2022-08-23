# !/usr/bin/env python

import sys
import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

#import numpy as np  # Import Numpy library
from scipy.spatial.transform import Rotation as R
import math  # Math library

import pandas as pd
import numpy as np
import cv2
import keyboard
import random
import time


def flsr(a):
    return float('{:.5f}'.format(float(a)))


class image_converter:

    def __init__(self):
        self.bridge = CvBridge()
        self.image_sub = rospy.Subscriber("/camera/rgb/image_raw", Image, self.callback)
        self.start = 0

    def callback(self, data):
        try:
            self.cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
            self.start = 1

        except CvBridgeError as e:
            print(e)

    def capture(self):
        count = 0
        folderNumber = random.randint(0, 1000)
        print("folderNumber = ", folderNumber)
        while (True):

            frame = self.cv_image
            
            cv2.imshow("frame",frame)
            cv2.waitKey(3)

            if keyboard.is_pressed('s'):
                cv2.imwrite("ChessFrames" + str(folderNumber) + "/frame%d.jpg" % count, frame)
                count = count + 1
                time.sleep(2)
            if keyboard.is_pressed('q'):
                time.sleep(1)
                break


def main(args):
    ic = image_converter()
    rospy.init_node('gazebo_camera_opencv', anonymous=True)
    while True:
        if ic.start == 1:
            break
    ic.capture()
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down")
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main(sys.argv)


