import cv2
import numpy as np

def histogram_equalization_color(img_path):
  img =cv2.imread(img_path)
    
    
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
 
    hsv[:, :, 2] = cv2.equalizeHist(hsv[:, :, 2])
    
  
    enhanced_img = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    
    
    output_path = "C:\\Users\\mhima\\Downloads\\enhanced_colored.jpg"
    cv2.imwrite(output_path, enhanced_img)
    
    print(f"Enhanced image saved at: {output_path}")
    return enhanced_img


image_path = "C:\\Users\\mhima\\Downloads\\images.jpg"


enhanced_colored_img = histogram_equalization_color(image_path)
