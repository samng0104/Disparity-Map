import cv2
left_image = cv2.imread('.\\Stereo_Image\\Art\\view1.png', cv2.IMREAD_COLOR)
right_image = cv2.imread('.\\Stereo_Image\\Art\\view5.png', cv2.IMREAD_COLOR)

def check_image():

    # Check if the images are loaded successfully
    if left_image is None or right_image is None:
        print('Failed to load the images')
        exit(1)

def display_image():

    # Display the left and right images
    cv2.imshow('Left Image', left_image)
    cv2.imshow('Right Image', right_image)

    # Wait for a key event and then close all windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()




# Perform further processing on the loaded images as needed
left_image_gray = cv2.cvtColor(left_image, cv2.COLOR_BGR2GRAY)
right_image_gray = cv2.cvtColor(right_image, cv2.COLOR_BGR2GRAY)


width = 640
height = 480
left_image_resized = cv2.resize(left_image, (width, height))
right_image_resized = cv2.resize(right_image, (width, height))


# Create a StereoBM object
stereo_bm = cv2.StereoBM_create(numDisparities=16, blockSize=15)

# Compute the disparity map
disparity_map = stereo_bm.compute(left_image_gray, right_image_gray)


if __name__ == '__main__':
    check_image()
    display_image()
    