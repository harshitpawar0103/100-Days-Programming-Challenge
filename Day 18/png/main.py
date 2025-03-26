import cv2 as c 
from turtle import Turtle,Screen
import numpy as np
t = Turtle()
s = Screen()
img = c.imread("hs.jpg")
ret, bw_img = c.threshold(img,127,255,c.THRESH_BINARY)
width = int(img.shape[0])
height = int(img.shape[1])
s.screensize(width,height)
print(s.screensize)

