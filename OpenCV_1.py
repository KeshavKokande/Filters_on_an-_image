import cv2
import numpy as np
import time

def gray_scale(path):
    img1=cv2.imread(path,0)
    cv2.imshow('image',img1)

def binary_img(img):
    ret,bw=cv2.threshold(img,127,255,cv2.THRESH_BINARY)#through thresholding we will try to provide the value the value through which we can put below the particular value we assign the value 0 and above it will be white. 
    cv2.imshow("Binary",bw)
    img1=bw    

def blue(img, height, width):
    B,G,R=cv2.split(img)
    zeros=np.zeros((height,width),dtype="uint8")
    cv2.imshow("Blue",cv2.merge([B,zeros,zeros]))
    img1=cv2.merge([B,zeros,zeros])

def green(img,height,width):
    B,G,R=cv2.split(img)
    zeros=np.zeros((height,width),dtype="uint8")
    cv2.imshow("Green",cv2.merge([zeros,G,zeros]))
    img1=cv2.merge([zeros,G,zeros])

def red(img,height,width):
    B,G,R=cv2.split(img)
    zeros=np.zeros((height,width),dtype="uint8")
    cv2.imshow("Red",cv2.merge([zeros,zeros,R]))
    img1=cv2.merge([zeros,zeros,R])

def smooth(img):
    bilateral=cv2.bilateralFilter(img,7,20,20)#9 ,75 and 75 are sigma color value and sigma space value affects cordinates space and color space 
    cv2.imshow("bilateral",bilateral)
    img1=bilateral

def blur(img):
    gaussian=cv2.GaussianBlur(img,(7,7),0)
    cv2.imshow("GaussianBlur",gaussian)
    img1=gaussian

def edge(img):
    canny=cv2.Canny(img,20,170)#This demand two thresholds from us i.e; 20 and 170 this is like lower and upper value 
    cv2.imshow("canny",canny)
    img1=canny

def saturation(img):
    img_HSV=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    cv2.imshow("saturation",img_HSV[:,:,1])
    img1=img_HSV[:,:,1]

def hue(img):
    img_HSV=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    cv2.imshow("Hue",img_HSV[:,:,0])
    img1=img_HSV[:,:,0]

def value(img):
    img_HSV=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    cv2.imshow("valuechannel",img_HSV[:,:,2])
    img1=img_HSV[:,:,2]

def crop(img):
    height,width=img.shape[:2]
    start_row,start_col=int(height*0.10),int(width*0.10)#starting pixel coordinates (topleft,of cropping rectangles)
    end_row,end_col=int(height*0.86),int(width*0.86)#ending pixel coordinates (bottom right),this can be changed
    cropped=img[start_row:end_row,start_col:end_col]
    cv2.imshow('cropped',cropped)
    img1=cropped

def double(img):
    resized=cv2.resize(img,(int(img.shape[1]*1.5),int(img.shape[0]*1.5)))#converting the float value into integer value
    cv2.imshow('resize',resized)
    img1=resized

def transpose(img):
    rotation_image=cv2.transpose(img)#this will covert the image of horizontal pixel elements into vertical pixel elements as in matrix
    cv2.imshow("legend",rotation_image)
    img1=rotation_image

def main():
    path="E:\\idiots.jpg"
    img=cv2.imread(path,1)
    dict_1={1:'Gray scale image',2:'Binary image',3:'Blue',4:'smoothing the image',5:'Blurring the image',6:'Detecting the edge of image',7:'saturation',8:'Green',9:'Red',10:'Value',11:'Hue',12:'cropping the image',13:'Doubling the image',14:'Transposing the image'}
    height=img.shape[0]
    width=img.shape[1]
    for i in range(1,len(dict_1)+1):
        print(i,'.',dict_1.get(i))
    while(True):
        num=input('Enter the number which type of image you want:')
        cv2.imshow('image',img)
        if num=='1':      #for gray scale image
            gray_scale(path)
        elif num=='2':    #for binary image
            binary_img(img)
        elif num=='3':    #for blue image
            blue(img,height,width)
        elif num=='4':    #for smoothing of image
           smooth(img)
        elif num=='5':    #for blurring of image
            blur(img)
        elif num=='6':    #for detecting edge
            edge(img)
        elif num=='7':    #for saturaation 
            saturation(img)
        elif num=='8':    #for green
            green(img,height,width)
        elif num=='9':     #for red 
            red(img,height,width)
        elif num=='10':    #for value
            value(img)
        elif num=='11':    #for hue
            hue(img)
        elif num=='12':    #for cropping the image
            crop(img)
        elif num=='13':    #for doubling the image
            double(img)
        elif num=='14':     #for transposing the image
            transpose(img)     
        else:
            print('invalid input')
        cv2.waitKey()
        cv2.destroyAllWindows()
        save=input('Do you want to save?y/n')
        if save=='y' or save == 'Y':
            file=input('Enter the image name to be saved')
            cv2.imwrite(file+'.jpg',img1)
        elif save=='n' or dsve == 'N':
            print('its ok')
        else:
            print('invalid input')
        a=input('Do you break?y/n')
        if a=='y' :
            break
        elif a=='n':
            print('its ok')
        else:
            print('invalid input')
            pass 

if __name__ == '__main__':
    main()