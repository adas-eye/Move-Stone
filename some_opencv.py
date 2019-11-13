import cv2
import numpy as np
# ----------------------------compute the centroid from a mask image-------------------------
def compute_centroid(img_path):
    nThresh = 100
    nMaxThresh = 255
    if isinstance(img_path,str):
        img = cv2.imread(img_path)
    else:
        img = img_path
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    gray = cv2.blur(gray, (3,3))

    cannyImg = cv2.Canny(gray, nThresh, nThresh*2, 3)
    contours, hierarchy = cv2.findContours(cannyImg, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    mu = []
    mc = []
    retval = np.array([])
    for i in range(0, np.array(contours).shape[0]):
        retval = cv2.moments(contours[i], False)
        mu.append(retval)
    mu = np.array(mu)

    for i in range(0, np.array(contours).shape[0]):
        if mu[i]['m00'] == 0.0:
            a=0
            b=0
        else:
            a = mu[i]['m10'] / mu[i]['m00']  #centroid x coor
            b = mu[i]['m01'] / mu[i]['m00']  #centroid y coor

        

        mc.append([a,b])
    return np.array(mc) # the centroid
