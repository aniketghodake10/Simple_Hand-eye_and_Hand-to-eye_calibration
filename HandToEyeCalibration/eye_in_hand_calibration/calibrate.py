import numpy as np
import cv2, PIL, os
from src.calibration_functions import *
import PyKDL

def main():

    # Read pose transforms from "images_transformation_info.txt"
    R_b2g, t_b2g = read_image_transforms("wrist2_wrt_base_transfromation_info.txt")
    R_t2c, t_t2c = read_image_transforms("target_wrt_cam_transfromation_info.txt")
    
    R_g2b, t_g2b = aniket_invert_transformation(R_b2g, t_b2g)
    R_c2t, t_c2t = aniket_invert_transformation(R_t2c, t_t2c)
    
    R_b2g, R_g2b = R_g2b, R_b2g
    t_b2g, t_g2b = t_g2b, t_b2g
    print(t_b2g)
    
    
    # perform eye_in_hand calibration to calculate cam2gripper transform
    R_c2g, t_c2g = calibrate_hand_eye(R_gripper2base=R_b2g, t_gripper2base=t_b2g, R_target2cam=R_c2t, t_target2cam=t_c2t)
    print("target_wrt_ee transformation...")
    print("\t\tRotation matrix:\n", R_c2g)
    print("\t\tTranslation vector:\n", t_c2g)
    
    
    f1 = PyKDL.Frame(PyKDL.Rotation.RPY(R_b2g[0][0], R_b2g[0][1],R_b2g[0][2]),  PyKDL.Vector(t_b2g[0][0], t_b2g[0][1],t_b2g[0][2]))
    f2 = PyKDL.Frame(PyKDL.Rotation(R_c2g[0][0],R_c2g[0][1],R_c2g[0][2], R_c2g[1][0],R_c2g[1][1],R_c2g[1][2], R_c2g[2][0],R_c2g[2][1],R_c2g[2][2]),  PyKDL.Vector(t_c2g[0], t_c2g[1],t_c2g[2])).Inverse()
    f3 = PyKDL.Frame(PyKDL.Rotation.RPY(R_c2t[0][0], R_c2t[0][1],R_c2t[0][2]),  PyKDL.Vector(t_c2t[0][0], t_c2t[0][1],t_c2t[0][2]))
    
    f = f1*f2*f3.Inverse()
    
    print("\n")
    print("camera_wrt_base transformation...")
    print("\t\tRotation matrix:\n", f.M.GetRPY())
    print("\t\tTranslation vector:\n", f.p)
    


if __name__ == "__main__":
    main()
