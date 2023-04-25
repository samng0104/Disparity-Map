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


# Global Variables

width = 640
height = 480
art_left_image = cv2.imread(r'./Stereo_Images/Art/view1.png', cv2.IMREAD_COLOR)
art_right_image = cv2.imread(r'./Stereo_Images/Art/view5.png', cv2.IMREAD_COLOR)

dolls_left_image = cv2.imread(r'./Stereo_Images/Dolls/view1.png', cv2.IMREAD_COLOR)
dolls_right_image = cv2.imread(r'./Stereo_Images/Dolls/view5.png', cv2.IMREAD_COLOR)

reindeer_left_image = cv2.imread(r'./Stereo_Images/Reindeer/view1.png', cv2.IMREAD_COLOR)
reindeer_rightt_image= cv2.imread(r'./Stereo_Images/Reindeer/view1.png', cv2.IMREAD_COLOR)


def display_image(left_image, right_image, ground_truth):

    if left_image is None or right_image is None:
        print('Failed to load the images')
        exit(1)

    # Display the left and right images
    cv2.imshow('Left Image', left_image)
    cv2.imshow('Right Image', right_image)

    # Wait for a key event and then close all windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def compute_disparity(left_image, right_image, ground_truth_disp_map):
    # Create a StereoBM object
    stereo_bm = cv2.StereoBM_create(numDisparities=16, blockSize=15)

    # Compute the disparity map
    disparity_map = stereo_bm.compute(left_image, right_image)

    # Calculate the Peak Signal-to-Noise Ratio (PSNR)
    max_val = np.max(ground_truth)
    psnr = 10 * np.log10((max_val ** 2) / mse)

if __name__ == '__main__':
    # Check if the images are loaded successfully
    # display_image(art_left_image, art_right_image)
    kp_left, des_left = detect(art_left_image)

    