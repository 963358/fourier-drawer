import whiteboard


if __name__ == '__main__':
    # filename is null if click on load button
    filename = whiteboard.path
    print(filename)
    if not filename:
        # load image instead

