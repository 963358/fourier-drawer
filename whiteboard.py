import tkinter as tk
from PIL import ImageGrab, Image
import cv2

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

        self.save_button = tk.Button(root, text="Save", command=self.save_canvas)
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
    
    # def save_canvas(self):
    #     im2 = ImageGrab.grab(bbox =(0, 0, self.width, self.height))
    #     im2.show()
    # def save_canvas(self):
    #     # save postscipt image 
    #     fileName = "saved_image"
    #     self.canvas.postscript(file = fileName + '.eps') 
    #     # use PIL to convert to PNG 
    #     img = Image.open(fileName + '.eps') 

    #     #img.save(fileName + '.png', 'png')
    #     #img.show()
    
    def save_canvas(self):
        widget = self.canvas
        x=self.root.winfo_rootx()+widget.winfo_x()
        y=self.root.winfo_rooty()+widget.winfo_y()
        # x1=x+widget.winfo_width()*2
        # y1=y+widget.winfo_height()
        x1 = x + 1000
        y1 = y + 700
        img2 = ImageGrab.grab(bbox = (x, y, x1, y1))
        #.crop((x,y,x1,y1))
        img2.show()
        self.root.destroy()
        return img2

    def clear_canvas(self):
        self.canvas.delete("all")

# app = WhiteboardApp(None)
# app.mainloop()
if __name__ == "__main__":
    
    root = tk.Tk()
    app = WhiteboardApp(root)
    img2 = root.mainloop()
    print(img2)