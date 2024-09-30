import cv2

def extract_frames(video_path, frame_rate=10):
    """
    Extracts frames from the video at regular intervals defined by frame_rate.
    
    :param video_path: Path to the input video.
    :param frame_rate: The interval at which frames are captured (every nth frame).
    :return: A list of frames (images) extracted from the video.
    """
    video = cv2.VideoCapture(video_path)
    frames = []
    frame_count = 0

    while video.isOpened():
        ret, frame = video.read()
        if not ret:
            break

        if frame_count % frame_rate == 0:
            frames.append(frame)

        frame_count += 1

    video.release()
    return frames
