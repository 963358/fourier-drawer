import tkinter as tk
import whiteboard
import filters
import os
import draw_epicycles

if __name__ == '__main__':
    # filename is null if click on load button
    root = tk.Tk()
    app = whiteboard.WhiteboardApp(root)
    root.mainloop()
    filename = app.path
    
    print("filename: ", filename)
    complex_data, img_shape = filters.start_filter(filename)

    draw_epicycles.constructPlane(complex_data)
    #scene = epicycles.createEpicycles()
    #scene.accessData(filename, complex_data, img_shape)
    #scene.render(scene)
#    open_media_file(scene.renderer.file_writer.movie_file_path)

