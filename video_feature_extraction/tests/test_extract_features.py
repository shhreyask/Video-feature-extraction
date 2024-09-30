import unittest
from src.models.face_landmarks import get_facial_landmarks
import cv2

class TestFeatureExtraction(unittest.TestCase):
    def test_facial_landmarks(self):
        # Load a test frame (replace with actual path to an image for real test)
        frame = cv2.imread('data/frames/test_frame.jpg')
        features = get_facial_landmarks(frame)
        self.assertTrue(len(features) > 0, "No facial features detected")
