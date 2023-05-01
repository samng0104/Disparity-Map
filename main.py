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
from PIL import Image

def compute_disparity(left_image, right_image):

    stereo = cv2.StereoBM_create(numDisparities=16, blockSize=5)
    # Compute the disparity map
    disparity_map = stereo.compute(left_image, right_image)
    # disparity_map = cv2.normalize(disparity_map, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)
    return disparity_map

if __name__ == '__main__':
    
    Stereo_Images = ["Art", "Dolls", "Reindeer"]
    for i in range(3):

        left_image_name = r'./Stereo_Images/' + Stereo_Images[i] + r'/view1.png'
        right_iamge_name = r'./Stereo_Images/' + Stereo_Images[i] + r'/view5.png'

        left_image = np.asarray(Image.open(left_image_name).convert('L'))
        right_image = np.asarray(Image.open(right_iamge_name).convert('L'))

        if Stereo_Images[i] == 'Art':
            left_image = cv2.GaussianBlur(left_image, (5, 5), 0)
            right_image = cv2.GaussianBlur(right_image, (5, 5), 0)
        else:
            left_image = cv2.GaussianBlur(left_image, (7, 7), 0)
            right_image = cv2.GaussianBlur(right_image, (7, 7), 0)


        pred_disp = compute_disparity(left_image, right_image)

        pred_disp = cv2.GaussianBlur(pred_disp, (19, 19), 0)

        disp_name = r'./pred/' + Stereo_Images[i] + r'/disp1.png'
        cv2.imwrite(disp_name, pred_disp)