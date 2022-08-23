#!/usr/bin/env python

import sys
import rospy
import cv2
from sensor_msgs.msg import Image
from std_srvs.srv import Empty,EmptyResponse
from cv_bridge import CvBridge, CvBridgeError

import numpy as np  # Import Numpy library
from scipy.spatial.transform import Rotation as R
import math  # Math library
#import pandas as pd

import tf2_ros
import geometry_msgs.msg
import time


def flsr(a):
  return float('{:.5f}'.format(float(a)))

def euler_from_quaternion(x, y, z, w):
    """
    Convert a quaternion into euler angles (roll, pitch, yaw)
    roll is rotation around x in radians (counterclockwise)
    pitch is rotation around y in radians (counterclockwise)
    yaw is rotation around z in radians (counterclockwise)
    """
    t0 = +2.0 * (w * x + y * z)
    t1 = +1.0 - 2.0 * (x * x + y * y)
    roll_x = math.atan2(t0, t1)

    t2 = +2.0 * (w * y - z * x)
    t2 = +1.0 if t2 > +1.0 else t2
    t2 = -1.0 if t2 < -1.0 else t2
    pitch_y = math.asin(t2)

    t3 = +2.0 * (w * z + x * y)
    t4 = +1.0 - 2.0 * (y * y + z * z)
    yaw_z = math.atan2(t3, t4)

    return roll_x, pitch_y, yaw_z  # in radians




class image_converter:

  def __init__(self):
    s1 = rospy.Service('take_transformations_tf', Empty, self.take_it)
    s2 = rospy.Service('save_transformations_tf', Empty, self.save_it)
    
    self.kisst = ""
    self.ccc = 0
    
    
    self.transform_translation_x = 0
    self.transform_translation_y = 0
    self.transform_translation_z = 0
    
    self.roll_x = 0
    self.pitch_y = 0
    self.yaw_z = 0
    
    
  def take_it(self,req):
    resp = EmptyResponse()
    self.kisst = self.kisst + "\n\n" + str(self.ccc) + ":\nRotation:\n" + str([self.roll_x, self.pitch_y, self.yaw_z]) + "\nTranslation:\n" + str([self.transform_translation_x, self.transform_translation_y, self.transform_translation_z])
    print("tranformations taken = " + str(self.ccc))
    self.ccc = self.ccc + 1
    return resp
  
  def save_it(self,req):
    resp = EmptyResponse()
    with open("transformations txt files/wrist2_wrt_base_transfromation_info.txt", "w") as f:
      f.write(self.kisst)
    return resp
    

  def capture(self):
    tfBuffer = tf2_ros.Buffer()
    listener = tf2_ros.TransformListener(tfBuffer)

    time.sleep(0.5)
    while not rospy.is_shutdown():
        try:
            trans = tfBuffer.lookup_transform('base', 'wrist_2_link', rospy.Time())
        except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException) as e:
            continue

        
        roll_x, pitch_y, yaw_z = euler_from_quaternion(trans.transform.rotation.x,
                                                         trans.transform.rotation.y,
                                                         trans.transform.rotation.z,
                                                         trans.transform.rotation.w)
                                                         
        self.transform_translation_x = trans.transform.translation.x
        self.transform_translation_y = trans.transform.translation.y
        self.transform_translation_z = trans.transform.translation.z
        self.roll_x = roll_x
        self.pitch_y = pitch_y
        self.yaw_z = yaw_z
        
        print(" transform_translation_x: {}".format(self.transform_translation_x))
        print(" transform_translation_y: {}".format(self.transform_translation_y))
        print(" transform_translation_z: {}".format(self.transform_translation_z))
        print(" roll_x: {}".format(self.roll_x))
        print(" pitch_y: {}".format(self.pitch_y))
        print(" yaw_z: {}".format(self.yaw_z))
        print()




def main(args):
  ic = image_converter()
  rospy.init_node('save_wrist2Link_wrt_base_transformations', anonymous=True)
  ic.capture()
  try:
      rospy.spin()
  except KeyboardInterrupt:
      print("Shutting down")

if __name__ == '__main__':
    main(sys.argv)
