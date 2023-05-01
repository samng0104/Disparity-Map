"""
Two rectified images
Write own program to infer depth
Define own matching criteria
locate the corresponding position of the match point
Based on this pos. and original pos.
Calculate the disparity and use disparity to infer the depth
Compare to the ground truth
"""
import cv2
import numpy as np

def display_image(left_image, right_image):

    if left_image is None or right_image is None:
        print('Failed to load the images')
        exit(1)

    cv2.imshow('Left Image', left_image)
    cv2.imshow('Right Image', right_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

def convert_grayscale(left_image, right_image):
    return cv2.cvtColor(left_image, cv2.COLOR_BGR2GRAY), cv2.cvtColor(right_image, cv2.COLOR_BGR2GRAY)

def compute_disparity(left_image, right_image):
    window_size = 3
    min_disp = 0
    max_disp = 16

    # Create a StereoBM object
    stereo = cv2.StereoSGBM_create(minDisparity=min_disp,
                                numDisparities=max_disp,
                                blockSize=window_size,
                                P1=8*3*window_size**2,
                                P2=32*3*window_size**2,
                                disp12MaxDiff=1,
                                uniquenessRatio=10,
                                speckleWindowSize=100,
                                speckleRange=32)
    # Compute the disparity map
    disparity_map = stereo.compute(left_image, right_image)
    disparity_map = cv2.normalize(disparity_map, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)
    return disparity_map

if __name__ == '__main__':
    
    Stereo_Images = ["Art", "Dolls", "Reindeer"]
    for i in range(3):

        left_image_name = r'./Stereo_Images/' + Stereo_Images[i] + r'/view1.png'
        right_iamge_name = r'./Stereo_Images/' + Stereo_Images[i] + r'/view5.png'

        left_image = cv2.imread(left_image_name, cv2.IMREAD_COLOR)
        right_image = cv2.imread(right_iamge_name, cv2.IMREAD_COLOR)

        # Check if the images are loaded successfully
        # display_image(left_image, right_image)

        # convert_grayscale(left_image, right_image)

        reconstructed_result = compute_disparity(left_image, right_image)
        disp_name = r'./pred/' + Stereo_Images[i] + r'/disp1.png'
        cv2.imwrite(disp_name, reconstructed_result)