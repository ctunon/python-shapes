# Carlos Tuñón 8-1066-1018
# Sergio Rodríguez 8-980-2414

from PIL import Image
from math import cos, sin, pi
 

def get_line(p0, p1):
    
    x0, y0 = p0
    x1, y1 = p1
    dx = x1 - x0
    dy = y1 - y0
 
    is_steep = abs(dy) > abs(dx)
 
    if is_steep:
        x0, y0 = y0, x0
        x1, y1 = y1, x1
 
    swapped = False
    if x0 > x1:
        x0, x1 = x1, x0
        y0, y1 = y1, y0
        swapped = True
 
    dx = x1 - x0
    dy = y1 - y0
 
    error = int(dx / 2.0)
    ystep = 1 if y0 < y1 else -1
 
    y = y0
    points = []
    for x in range(x0, x1 + 1):
        coord = (y, x) if is_steep else (x, y)
        points.append(coord)
        error -= abs(dy)
        if error < 0:
            y += ystep
            error += dx
 
    if swapped:
        points.reverse()
    return points


def draw_line(image, p0, p1):
    for pixel in get_line(p0, p1):
        image.putpixel(pixel, (49, 210, 232, 91))
    
def draw_octagon(x,y,r):
    
    img = Image.new("RGB", (1280, 720))

    rad = (pi/180)*45

    for i in range(8):
        x0 = int(x + r * cos(rad*i))
        y0 = int(y + r * sin(rad*i))
        x1 = int(x + r * cos(rad*(i+1)))
        y1 = int(y + r * sin(rad*(i+1)))

        draw_line(img, (x0,y0), (x1,y1))

    img.show()

def draw_diamond(x,y,r):
    
    img = Image.new("RGB", (1280, 720))

    rad = (pi/180)*90

    for i in range(4):
        x0 = int(x + r * cos(rad*i))
        y0 = int(y + r * sin(rad*i))
        x1 = int(x + r * cos(rad*(i+1)))
        y1 = int(y + r * sin(rad*(i+1)))

        draw_line(img, (x0,y0), (x1,y1))

    img.show()

def draw_triangle(x,y,r):
    
    img = Image.new("RGB", (1280, 720))

    rad = (pi/180)*120

    for i in range(3):
        x0 = int(x + r * cos(rad*i))
        y0 = int(y + r * sin(rad*i))
        x1 = int(x + r * cos(rad*(i+1)))
        y1 = int(y + r * sin(rad*(i+1)))

        draw_line(img, (x0,y0), (x1,y1))

    img.show()

def draw_rectangle():
        
        img = Image.new("RGB", (1280, 720))
        draw_line(img, (1000,500),(300,500))
        draw_line(img, (300,500),(300,100))
        draw_line(img, (300,100),(1000,100))
        draw_line(img, (1000,100),(1000,500))

        img.show()



draw_rectangle()

