from PIL import Image,ImageDraw,ImageFont
import numpy as np
import matplotlib.pyplot as plt
import cv2
img = Image.open("./3.jpg")
def plotting_img():
    plt.imshow(np.array(img))
    plt.show()

img = cv2.imread("./3.jpg")

def certificate(img,name):
    generated_image = img.copy()
    font = cv2.FONT_HERSHEY_COMPLEX
    coordinates = (113,189)
    font_size = 1.2
    font_color = (51,51,51)
    font_thickness = 2
    cv2.putText(generated_image,name,coordinates,font,font_size,font_color,font_thickness)
    return generated_image

def save_image(img,name):
    path = "./3_{}.jpg".format(name)
    print(cv2.imwrite(path,img))


plotting_img()
name=input("Enter your name:")
generated_image = certificate(img,name)
save_image(generated_image,name)





