#!/usr/bin/env python

import sys

import numpy as np  # Import Numpy library
from scipy.spatial.transform import Rotation as R
import math  # Math library
#import pandas as pd
import PyKDL


def flsr(a):
  return float('{:.5f}'.format(float(a)))

def euler_to_quaternion(r):
    (roll, pitch, yaw) = (r[0], r[1], r[2])
    qx = np.sin(roll/2) * np.cos(pitch/2) * np.cos(yaw/2) - np.cos(roll/2) * np.sin(pitch/2) * np.sin(yaw/2)
    qy = np.cos(roll/2) * np.sin(pitch/2) * np.cos(yaw/2) + np.sin(roll/2) * np.cos(pitch/2) * np.sin(yaw/2)
    qz = np.cos(roll/2) * np.cos(pitch/2) * np.sin(yaw/2) - np.sin(roll/2) * np.sin(pitch/2) * np.cos(yaw/2)
    qw = np.cos(roll/2) * np.cos(pitch/2) * np.cos(yaw/2) + np.sin(roll/2) * np.sin(pitch/2) * np.sin(yaw/2)
    return [qx, qy, qz, qw]
    
    
def quaternion_to_euler(x, y, z, w, unit = "deg"):
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

    if unit == "rad":
        roll_x = math.degrees(roll_x)
        pitch_y = math.degrees(pitch_y)
        yaw_z = math.degrees(yaw_z)

    return roll_x, pitch_y, yaw_z  # in radians

def matrix_to_rpy(rot):
    r2 = PyKDL.Rotation(rot[0], rot[1], rot[2], rot[3], rot[4], rot[5], rot[6], rot[7], rot[8])
    return  r2.GetRPY()

def rpy_to_matrix(r):
    r1 = PyKDL.Rotation.RPY(r[0], r[1], r[2])
    return r1

def rad2deg_and_vice_versa(listt, command = "rad2deg"):
    a = []
    if command == "rad2deg":
        for i in listt:
            a.append(math.degrees(i))
    else:
        for i in listt:
            a.append(math.radians(i))
    return a


#a = euler_to_quaternion([-2.443273482787532, 0.014326259575427666, -1.537888399992644])
a = euler_to_quaternion([-1.4355155040959022, -0.6126289048590672, 0.7793809123480208])
print(a)
print(quaternion_to_euler(a[0], a[1], a[2], a[3]))
b = matrix_to_rpy([0.70835141, 0.70505951, 0.03360599, 0.69987764, -0.7077369, 0.0963316, 0.69987764, -0.7077369, 0.0963316])
print("b", b)
print(rad2deg_and_vice_versa([b[0], b[1], b[2]]))
print(rpy_to_matrix([1.57,0,0]))