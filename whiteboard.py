import tkinter as tk
from tkinter.messagebox import askyesno
from PIL import ImageGrab, Image
import cv2
import time
import os

class WhiteboardApp:
    def __init__(self, root):

        self.root = root
        self.root.title("Whiteboard")

        self.canvas = tk.Canvas(root, width=1000, height=700, bg="white")
        self.canvas.pack()

        self.width = 1000
        self.height = 700


        self.draw_button = tk.Button(root, text="Draw", command=self.start_draw)
        self.draw_button.pack(side=tk.LEFT)

        self.erase_button = tk.Button(root, text="Erase", command=self.start_erase)
        self.erase_button.pack(side=tk.LEFT)

        self.clear_button = tk.Button(root, text="Clear", command=self.clear_canvas)
        self.clear_button.pack(side=tk.LEFT)

        self.save_button = tk.Button(root, text="Save and generate fourier epicycles", command=self.save_canvas)
        self.save_button.pack(side=tk.LEFT)

        self.drawing = False
        self.erasing = False
        self.last_x, self.last_y = None, None

        self.canvas.bind("<Button-1>", self.start_action)
        self.canvas.bind("<B1-Motion>", self.draw_or_erase)
        self.canvas.bind("<ButtonRelease-1>", self.stop_action)

    def start_action(self, event):
        if self.drawing:
            self.start_draw(event)
        elif self.erasing:
            self.start_erase(event)

    def stop_action(self, event):
        if self.drawing:
            self.stop_draw(event)
        elif self.erasing:
            self.stop_erase(event)

    def start_draw(self, event=None):
        self.drawing = True
        self.erasing = False
        if event:
            self.last_x, self.last_y = event.x, event.y

    def stop_draw(self, event=None):
        self.drawing = False
        self.erasing = False

    def start_erase(self, event=None):
        self.erasing = True
        self.drawing = False
        if event:
            self.last_x, self.last_y = event.x, event.y

    def stop_erase(self, event=None):
        self.erasing = False
        self.drawing = False

    def draw_or_erase(self, event):
        if self.drawing:
            x, y = event.x, event.y
            self.canvas.create_line(self.last_x, self.last_y, x, y, fill="black", width=2)
            self.last_x, self.last_y = x, y
        elif self.erasing:
            x, y = event.x, event.y
            self.canvas.create_rectangle(x - 5, y - 5, x + 5, y + 5, fill="white", outline="white")
    
    def save_canvas(self):
        filename = time.ctime()
        
        message = f"Generating fourier epicycles will lose the ability to further edit your drawings but will save it as a png inside the project image folder as (/images/{filename})"
        
        answer = askyesno("Confirmation", message)
        
        if not answer:
            return

        self.canvas.postscript(file=filename+'.eps')
        saved_img = Image.open(filename + '.eps')
        
        path = os.path.join(os.getcwd(), 'images', filename) + ".png"
        
        saved_img.save(path, 'png')

        
        
    def clear_canvas(self):
        self.canvas.delete("all")

global path

root = tk.Tk()
app = WhiteboardApp(root)
root.mainloop()
