import cv2
import numpy as np

"""
Global Variables
"""
width = 640
height = 480
art_left_image = cv2.imread('.\\Stereo_Image\\Art\\view1.png', cv2.IMREAD_COLOR)
art_right_image = cv2.imread('.\\Stereo_Image\\Art\\view5.png', cv2.IMREAD_COLOR)

dolls_left_image = cv2.imread('.\\Stereo_Image\\Dolls\\view1.png', cv2.IMREAD_COLOR)
dolls_right_image = cv2.imread('.\\Stereo_Image\\Dolls\\view5.png', cv2.IMREAD_COLOR)

reindeer_left_image = cv2.imread('.\\Stereo_Image\\Reindeer\\view1.png', cv2.IMREAD_COLOR)
reindeer_rightt_image= cv2.imread('.\\Stereo_Image\\Reindeer\\view1.png', cv2.IMREAD_COLOR)


def display_image(left_image, right_image):

    # Check if the images are loaded successfully
    if left_image is None or right_image is None:
        print('Failed to load the images')
        exit(1)

    # Display the left and right images
    cv2.imshow('Left Image', left_image)
    cv2.imshow('Right Image', right_image)

    # Wait for a key event and then close all windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def convert_grayscale(left_image, right_image):
    left_image_gray = cv2.cvtColor(left_image, cv2.COLOR_BGR2GRAY)
    right_image_gray = cv2.cvtColor(right_image, cv2.COLOR_BGR2GRAY)

    return left_image_gray, right_image_gray

def resize_image(left_image, right_image):

    left_image_resized = cv2.resize(left_image, (width, height))
    right_image_resized = cv2.resize(right_image, (width, height))
    
    return left_image_resized, right_image_resized

def compute_disparity(left_image, right_image, ground_truth_disp_map):
    # Create a StereoBM object
    stereo_bm = cv2.StereoBM_create(numDisparities=16, blockSize=15)

    # Compute the disparity map
    disparity_map = stereo_bm.compute(left_image, right_image)

    ground_truth_disp_map_resized = cv2.resize(ground_truth_disp_map, (width, height))

    # Calculate the Peak Signal-to-Noise Ratio (PSNR)
    max_val = np.max(ground_truth_disp_map_resized)
    psnr = 10 * np.log10((max_val ** 2) / mse)

if __name__ == '__main__':
    display_image()
    