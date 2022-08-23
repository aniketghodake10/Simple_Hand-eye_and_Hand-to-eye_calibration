import os
import re
import ast
import PyKDL
import numpy as np

import cv2, PIL
#from src.calibration_functions import *

def aniket_invert_transformation(R_a2b, t_a2b):
    R_b2a = []
    t_b2a = []
    
    for i in range(len(R_a2b)):
      R_b2a.append(list(PyKDL.Rotation.RPY(R_a2b[i][0], R_a2b[i][1], R_a2b[i][2]).Inverse().GetRPY()))
      t_b2a.append([-1*t_a2b[i][0], -1*t_a2b[i][1], -1*t_a2b[i][2]])
      

    return R_b2a, t_b2a
    
def read_image_transforms():
    """
    Take the transformation information about robot poses from a txt file.
    Reads and converts it into 2 lists of lists (rotation and translation).
    """

    R_list = []
    t_list = []

    os.chdir("..")
    image_dir = os.path.join(os.getcwd(), "eye_in_hand_calibration",  'images_transformation_info.txt')
    with open(image_dir) as f:
        lines = f.readlines()
        n = -1
        for line in lines:
            if not re.match(r'^\s*$', line):    
                line = line.strip('\n')
                line = line.strip('\t')
                if line[0]=='[':
                    line = ast.literal_eval(line)
                    #line = [n.strip() for n in line]
                    n+=1
                    if n%2 == 0:
                        # rotation here
                        r = line
                        R_list.append(r)
                    else:
                        t = line
                        t_list.append(t)

    
    print(R_list)
    print(t_list)
    return R_list, t_list


def read_image_transforms(txtfile):
    """
    Take the transformation information about robot poses from a txt file.
    Reads and converts it into 2 lists of lists (rotation and translation).
    """

    R_list = []
    t_list = []

    os.chdir("..")
    image_dir = os.path.join("/home/ictg-3/aniket_files/aaFinal_ArucoDetection/eye_in_hand_calibration", txtfile)
    with open(image_dir) as f:
        lines = f.readlines()
        n = -1
        for line in lines:
            if not re.match(r'^\s*$', line):    
                line = line.strip('\n')
                line = line.strip('\t')
                if line[0]=='[':
                    line = ast.literal_eval(line)
                    #line = [n.strip() for n in line]
                    n+=1
                    if n%2 == 0:
                        # rotation here
                        r = line
                        R_list.append(r)
                    else:
                        t = line
                        t_list.append(t)

    return R_list, t_list

def mainn():

    # Read pose transforms from "images_transformation_info.txt"
    R_b2g, t_b2g = read_image_transforms("wrist2_wrt_base_transfromation_info.txt")
    R_t2c, t_t2c = read_image_transforms("target_wrt_cam_transfromation_info.txt")
    
    R_g2b, t_g2b = aniket_invert_transformation(R_b2g, t_b2g)
    R_c2t, t_c2t = aniket_invert_transformation(R_t2c, t_t2c)
    
    
    


mainn()
