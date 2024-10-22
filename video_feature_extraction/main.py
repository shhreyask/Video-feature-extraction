import cv2
from src.models.faceplusplus_attributes import extract_face_attributes
from src.utils.json_helper import save_features_to_json

def extract_frame_at_time(video_path, time_in_seconds):
    """
    Extracts a single frame from the video at the specified time (in seconds).
    
    :param video_path: Path to the video file.
    :param time_in_seconds: Time in seconds to extract the frame from.
    :return: The extracted frame (as a numpy array), or None if extraction fails.
    """
    # Open the video file
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print(f"Error opening video file {video_path}")
        return None

    # Get frame rate (fps) of the video
    fps = cap.get(cv2.CAP_PROP_FPS)

    # Calculate the frame number to capture
    frame_number = int(fps * time_in_seconds)

    # Set the video to the desired frame
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)

    # Read the frame
    success, frame = cap.read()

    if not success:
        print(f"Could not read frame at {time_in_seconds} seconds")
        return None

    # Release the video capture object
    cap.release()

    return frame

def main(video_path, output_json_path):
    # Extract the frame at the 2-second mark
    frame = extract_frame_at_time(video_path, 2)  # 2 seconds

    if frame is not None:
        # Extract facial attributes using the Face++ API
        attributes = extract_face_attributes(frame)

        # Save the attributes to a JSON file
        feature_data = {
            "frame_time_seconds": 2,
            "attributes": attributes
        }
        save_features_to_json([feature_data], output_json_path)

        print("Facial attributes extracted and saved to:", output_json_path)
    else:
        print("Failed to extract frame or extract attributes")

if __name__ == "__main__":
    video_path = "data/videos/sample_video.mp4"
    output_json_path = "data/features/sample_video_attributes.json"
    
    main(video_path, output_json_path)
