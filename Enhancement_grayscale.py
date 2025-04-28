import cv2
import numpy as np

def histogram_equalization(img_path):
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    eq_img = cv2.equalizeHist(img)
    output_path = "C:\\Users\\mhima\\Downloads\\enhanced_histogram.jpg"
    cv2.imwrite(output_path, eq_img)
    
    print(f"Enhanced image saved at: {output_path}")
    return eq_img
image_path = "C:\\Users\\mhima\\Downloads\\images.jpg"
 Equalization
hist_eq_img = histogram_equalization(image_path)
