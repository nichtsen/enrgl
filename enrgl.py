import os
import sys
from PIL import ImageDraw, Image
import numpy as np

width = 800
height = 800

def setblank():
	blank = Image.new("RGBA",(width,height),(255,255,255))
	obj = ImageDraw.Draw(blank)
	return obj, blank
	
def circle(r1, r2, theta):
	x = np.around(r1 * np.cos(theta))
	y = np.around(r1 * np.sin(theta))
	x2 = np.around(r2 * np.cos(theta))
	y2 = np.around(r2 * np.sin(theta))
	x = x[0]
	y = y[0]
	x2 = x2[0]
	y2 = y2[0]
	return x, y, x2, y2

def dlinecir(r1, r2):
	ob, bl = setblank()
	ob.ellipse((350,350,450,450), outline = 128, fill = "orange")
	for i in range(len(r1)):
		ob.ellipse((350-r1[i],350-r1[i],450+r1[i],450+r1[i]), outline = "blue")
	for i in range(len(r2)):
		ob.ellipse((350-r2[i],350-r2[i],450+r2[i],450+r2[i]), outline = "blue")
	bl.show()
	
def dpointcir(x, y, x2, y2):
	ob, bl = setblank()
	ob.ellipse((350,350,450,450), outline = 128, fill = "orange")
	for i in range(len(x)):
		ob.point((x[i],y[i]), fill = "blue")
	for i in range(len(x)):
		ob.point((x2[i],y2[i]), fill = "blue")
	bl.show()
	bl.save('test.png')
	
def main():
	ob, bl = setblank()
	r1 = np.around(np.random.normal(150,25,10000))
	r2 = np.around(np.random.normal(250,25,10000))
	theta = 2*np.pi*np.random.rand(1,10000)
	x, y, x2, y2 = circle(r1, r2, theta)
	x += 400
	y += 400
	x2 += 400
	y2 += 400
#	dlinecir(r1, r2)
	dpointcir(x, y, x2, y2)
	
if __name__ == '__main__':
    main()