import tkinter as tk
from tkinter.messagebox import askyesno
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk
import time
import os


class WhiteboardApp:
    def __init__(self, root):

        self.path = ""
        
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

        self.load_button = tk.Button(root, text="Load an Image", command=self.load_image)
        self.load_button.pack(side=tk.LEFT)


        self.drawing = False
        self.erasing = False
        self.last_x, self.last_y = None, None

        self.canvas.bind("<Button-1>", self.start_action)
        self.canvas.bind("<B1-Motion>", self.draw_or_erase)


    def load_image(self):
        self.path = askopenfilename()
        ext = ["jpg", "jpeg", "png"]
        if (type(self.path) is not tuple and self.path != ""):
            if(self.path.split('.')[-1] in ext):
                print(self.path.split('.')[-1])
                self.root.destroy()



    def start_action(self, event):
        if self.drawing:
            self.start_draw(event)
        elif self.erasing:
            self.start_erase(event)

    def start_draw(self, event=None):
        self.drawing = True
        self.erasing = False
        if event:
            self.last_x, self.last_y = event.x, event.y

    def start_erase(self, event=None):
        self.erasing = True
        self.drawing = False
        if event:
            self.last_x, self.last_y = event.x, event.y

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
        
        message = f"Generating fourier epicycles will save the current canvas as a png inside the project image folder (/images/{filename})"
        
        answer = askyesno("Confirmation", message)
        
        if not answer:
            return

        self.canvas.postscript(file=filename+'.eps')
        saved_img = Image.open(filename + '.eps')
        
        self.path = os.path.join(os.getcwd(), 'images', filename) + ".png"
        print("yerherher", self.path)
        saved_img.save(self.path, 'png')

        os.remove(filename+'.eps')
        self.root.destroy()
    
    def clear_canvas(self):
        self.canvas.delete("all")
