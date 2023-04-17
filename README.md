# Disparity-Map
ASSIGNMENT 2 

CS4186 COMPUTER VISION AND IMAGE PROCESSING 

 

Given stereo image pairs (three stereo pairs are provided in   https://drive.google.com/drive/folders/1pdDkFpa59m4A02pLkUqI1H2Zb_GerLkK?usp=sharing  ),  you are required to write a program with C++ or Python or Matlab to compute the Disparity Maps of each left (view1) image.     

For each stereo pair, the two images (named view1.png and view5.png) are already rectified so that all image motion is purely horizontal. Ground-truth disparity maps of the left view (view1) are also provided for reference.  It should be noted that disparities are represented "as is", i.e., intensity 60 means the disparity is 60. The exception is intensity 0, which means unknown disparity. More details about the stereo pairs can be found in https://vision.middlebury.edu/stereo/data/scenes2005/.          

The reconstructed results will be evaluated by Peak_Signal-to-Noise_Ratio (PSNR): https://en.wikipedia.org/wiki/Peak_signal-to-noise_ratio . You can use the source code implemented by Matlab (https://www.mathworks.com/help/vision/ref/psnr.html) or Python ( https://cvnote.ddlee.cc/2019/09/12/psnr-ssim-python ) for PSNR calculation. The PSNR is calculated against the ground-truth disparity map. The higher PSNR you can achieve, the better performance you will get.                                              
