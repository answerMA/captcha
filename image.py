#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 9/25/2017 4:29 PM
# @Author  : Ruiming_Ma
# @Site    : 
# @File    : image.py
# @Software: PyCharm Community Edition


from PIL import Image
import tesserocr

def getImage():
    path = r'E:\Python_files\captcha\captcha.png'
    image = Image.open(path)
    image = image.convert('P')

    return image

def getColors():
    his = getImage().histogram()
    rgb = {}

    for i in range(256):
        rgb[i] = his[i]

    rgb = sorted(rgb.items(), key = lambda x:x[1], reverse= True)
    for j,k in rgb[:10]:
        print(j,k)

def createImage(image, arg1, arg2):
    image2 = Image.new('P',image.size,255)
    for x in range(image.size[1]):
        for y in range(image.size[0]):
            pix = image.getpixel((y,x))
            if pix == arg1 or pix == arg2:
                image2.putpixel((y,x),0)

    #image2.show()
    return image2

def main():
    getColors()
    newImage = createImage(getImage(), 0, 15)
    print(tesserocr.image_to_text(newImage))

main()
