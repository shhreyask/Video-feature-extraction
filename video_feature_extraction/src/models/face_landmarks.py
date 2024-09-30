import dlib
from imutils import face_utils
import cv2

# Load dlib's face detector and shape predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("models/shape_predictor_68_face_landmarks.dat")

def get_facial_landmarks(frame):
    """
    Detects facial landmarks in a single frame.

    :param frame: The image (frame) to process.
    :return: Dictionary of facial landmark coordinates.
    """
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)
    facial_features = []

    for face in faces:
        shape = predictor(gray, face)
        shape = face_utils.shape_to_np(shape)
        landmarks = {
            'jaw': shape[0:17].tolist(),
            'right_eyebrow': shape[17:22].tolist(),
            'left_eyebrow': shape[22:27].tolist(),
            'nose': shape[27:36].tolist(),
            'right_eye': shape[36:42].tolist(),
            'left_eye': shape[42:48].tolist(),
            'mouth': shape[48:68].tolist(),
        }
        facial_features.append(landmarks)

    return facial_features
