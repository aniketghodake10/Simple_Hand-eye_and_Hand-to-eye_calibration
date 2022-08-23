# !/usr/bin/env python

import sys
import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError


import math  # Math library

#import pandas as pd
import numpy as np
import cv2
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

        print("JK JK JK JK JK Jk JK JK JK JK JK Jk JK JK JK JK JK Jk JK JK JK JK JK Jk")
        while (True):
            n=str(count)
            n = n.zfill(8)
            frame = self.cv_image
            cv2.imshow("frame",frame)
            k = cv2.waitKey(1)
            if k == 27:
                cv2.destroyAllWindows()
                break
            elif k==ord("s"):
                cv2.imwrite(f"ChessFrames3/frame{n}.jpg", frame)
                print(f"Image Captured = {n}")
                count = count + 1
     
                


def main(args):
    ic = image_converter()
    rospy.init_node('gazebo_camera_opencv', anonymous=True)
    while True:
        if ic.start == 1:
            break
    ic.capture()
    print("JK JK JK JK JK Jk JK JK JK JK JK Jk JK JK JK JK JK Jk JK JK JK JK JK Jk")


if __name__ == '__main__':
    main(sys.argv)


