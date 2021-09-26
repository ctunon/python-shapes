# Carlos Tuñón 8-1066-1018
# Sergio Rodríguez 8-980-2414

from PIL import Image, ImageTk
from math import cos, sin, pi
from queue import Queue
import tkinter as tk
global imgtk


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)



window = tk.Tk()
window.geometry("600x400")

label1 = tk.Label(window, text="Hello", bg="red", fg="white" )
label1.pack(fill=tk.X)

canvas = tk.Canvas(window, width = 300, height = 300)
canvas.pack(side= tk.BOTTOM)  
  
boton_octagono = tk.Button(window, text="Octagono", bg="black", fg="white", command = lambda: draw_octagon(150,150,75))
boton_octagono.pack(side=tk.LEFT)

boton_rombo = tk.Button(window, text="rombo",  bg="black", fg="white", command = lambda: draw_diamond(150,150,75))
boton_rombo.pack(side=tk.LEFT)

boton_rectangulo = tk.Button(window, text="rectangulo",  bg="black", fg="white", command = lambda: draw_square())
boton_rectangulo.pack(side=tk.LEFT)


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

def dfs(img, x, y, new_color):
    w = img.width
    h = img.height
    old_color = img.getpixel((x,y))
    queue= Queue()
    queue.put((x,y))
    while not queue.empty():
        x, y = queue.get()
        if x < 0 or x >= w or y < 0 or y >= h or img.getpixel((x,y)) != old_color:
            continue
        else:   
            img.putpixel((x, y),new_color)
            queue.put((x+1, y))
            queue.put((x-1, y))
            queue.put((x, y+1))
            queue.put((x, y-1))


def draw_line(image, p0, p1):
    for pixel in get_line(p0, p1):
        image.putpixel(pixel, (255, 255, 255, 100))
    
def draw_octagon(x,y,r):

    img = Image.new("RGB", (300, 300))

    
    rad = (pi/180)*45

    for i in range(8):
        x0 = int(x + r * cos(rad*i))
        y0 = int(y + r * sin(rad*i))
        x1 = int(x + r * cos(rad*(i+1)))
        y1 = int(y + r * sin(rad*(i+1)))

        draw_line(img, (x0,y0), (x1,y1))

    dfs(img,150,150,RED)
    img.save(fp="images/octagon.jpg")

    imgtk = ImageTk.PhotoImage(Image.open("images/octagon.jpg"))
    canvas.create_image(20,20, anchor=tk.NW, image=imgtk) 
    canvas.image = imgtk 


def draw_diamond(x,y,r):

    img = Image.new("RGB", (300, 300))


    rad = (pi/180)*90

    for i in range(4):
        x0 = int(x + r * cos(rad*i))
        y0 = int(y + r * sin(rad*i))
        x1 = int(x + r * cos(rad*(i+1)))
        y1 = int(y + r * sin(rad*(i+1)))

        draw_line(img, (x0,y0), (x1,y1))
    
    dfs(img,150,150,RED)
    img.save(fp="images/diamond.jpg")
    imgtk = ImageTk.PhotoImage(Image.open("images/diamond.jpg"))
    canvas.create_image(20,20, anchor=tk.NW, image=imgtk) 
    canvas.image = imgtk

def draw_triangle(x,y,r):

    img = Image.new("RGB", (300, 300))

    
    rad = (pi/180)*120

    for i in range(3):
        x0 = int(x + r * cos(rad*i))
        y0 = int(y + r * sin(rad*i))
        x1 = int(x + r * cos(rad*(i+1)))
        y1 = int(y + r * sin(rad*(i+1)))

        draw_line(img, (x0,y0), (x1,y1))

    dfs(img,150,150,RED)
    img.save(fp="images/triangle.jpg")
    imgtk = ImageTk.PhotoImage(Image.open("images/octagon.jpg"))
    canvas.create_image(20,20, anchor=tk.NW, image=imgtk) 
    canvas.image = imgtk
    

def draw_square():

    img = Image.new("RGB", (300, 300))

        
    draw_line(img, (225,225),(75,225))
    draw_line(img, (75,225),(75,75))
    draw_line(img, (75,75),(225,75))
    draw_line(img, (225,75),(225,225))
    dfs(img,150,150,RED)
    img.save(fp="images/square.jpg")
    imgtk = ImageTk.PhotoImage(Image.open("images/square.jpg"))
    canvas.create_image(20,20, anchor=tk.NW, image=imgtk) 
    canvas.image = imgtk


window.mainloop()
