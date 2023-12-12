import tkinter as tk
import whiteboard
import filters

if __name__ == '__main__':
    # filename is null if click on load button
    root = tk.Tk()
    app = whiteboard.WhiteboardApp(root)
    root.mainloop()
    filename = app.path
    
    print(filename)
    filters.start_filter(filename)

