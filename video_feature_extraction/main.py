from src.video_processor import extract_frames
from src.models.face_landmarks import get_facial_landmarks
from src.utils.json_helper import save_features_to_json

def main(video_path, output_json_path):
    # Step 1: Extract frames from the video
    frames = extract_frames(video_path)

    all_features = []
    # Step 2: Extract features for each frame
    for frame_num, frame in enumerate(frames, start=1):
        facial_features = get_facial_landmarks(frame)
        all_features.append({
            "frame_number": frame_num,
            "features": facial_features
        })

    # Step 3: Save features to JSON
    save_features_to_json(all_features, output_json_path)

if __name__ == "__main__":
    video_path = "data/videos/sample_video.mp4"
    output_json_path = "data/features/sample_video_features.json"
    main(video_path, output_json_path)
