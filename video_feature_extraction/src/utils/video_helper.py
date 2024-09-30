import cv2

def display_frame(frame, window_name='Frame'):
    """
    Displays a single frame in a window.
    
    :param frame: The image (frame) to display.
    :param window_name: The name of the display window.
    """
    cv2.imshow(window_name, frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def save_frame(frame, path):
    """
    Saves a single frame to disk.
    
    :param frame: The image (frame) to save.
    :param path: Path to save the frame (including filename and extension).
    """
    cv2.imwrite(path, frame)
