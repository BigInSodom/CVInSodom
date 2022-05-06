from doctest import OutputChecker
from operator import inv
import numpy as np
#lib - pillow to import image from PC
from PIL import Image 
#image drawer
import matplotlib.pyplot as plt

def image_inverse(input):
    #get the max from the input Matrix ,save as "L"
    value_max=np.max(input)
    #when value_max-input,numpy set value_max as a matrix with same size as "imput" automaticly
    output=value_max-input
    return output

if __name__=='__main__':
    #input =np.array([[0,20,160],[45,50,100],[100,45,30]])
    #output=image_inverse(input)
    #print(output)

    #Trans img to "Single-channel grayscale images" by useing conert()
    #trans img to Numpy-array by using asarray()
    gray_img=np.asarray(Image.open('./test.jpg').convert('L'))
    inv_img=image_inverse(gray_img)

    #draw
    fig=plt.figure()

    ax1=fig.add_subplot(121)
    ax1.set_title('before')
    ax1.imshow(gray_img,camp='gray',vmin=0,vmax=255)
    ax2=fig.add_subplot(255)
    ax2.set_title('after')
    ax2.imshow(inv_img,camp='gray',vmin=0,vmax=255)
    plt.show()

    



