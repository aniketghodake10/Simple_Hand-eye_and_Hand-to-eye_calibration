import cv2  # Import the OpenCV library
import numpy as np  # Import Numpy library
from scipy.spatial.transform import Rotation as R
import math  # Math library

def flsr(a):
    return float('{:.5f}'.format(float(a)))


def euler_to_quaternion(yaw, pitch, roll):

        qx = np.sin(roll/2) * np.cos(pitch/2) * np.cos(yaw/2) - np.cos(roll/2) * np.sin(pitch/2) * np.sin(yaw/2)
        qy = np.cos(roll/2) * np.sin(pitch/2) * np.cos(yaw/2) + np.sin(roll/2) * np.cos(pitch/2) * np.sin(yaw/2)
        qz = np.cos(roll/2) * np.cos(pitch/2) * np.sin(yaw/2) - np.sin(roll/2) * np.sin(pitch/2) * np.cos(yaw/2)
        qw = np.cos(roll/2) * np.cos(pitch/2) * np.cos(yaw/2) + np.sin(roll/2) * np.sin(pitch/2) * np.sin(yaw/2)

        return [qx, qy, qz, qw]
        

print(euler_to_quaternion(0.71856*0.017453278, 9.92419*0.017453278, 171.10053*0.017453278))
print(euler_to_quaternion(1.34732*0.017453278, 4.79766*0.017453278, 171.18559*0.017453278))
