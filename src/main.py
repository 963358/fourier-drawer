import tkinter as tk
import whiteboard
import filters
import os
import epicycles

if __name__ == '__main__':
    # filename is null if click on load button
    root = tk.Tk()
    app = whiteboard.WhiteboardApp(root)
    root.mainloop()
    filename = app.path
    
    print(filename)
    polar = filters.start_filter(filename)
    #cords = filters.getCords()

#    print(polar)    
    scene = epicycles.createEpicycles()
    scene.accessData(filename, polar)
    scene.render(scene)
#    open_media_file(scene.renderer.file_writer.movie_file_path)

