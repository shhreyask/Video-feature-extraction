import unittest
from src.models.faceplusplus_attributes.py import get_facial_landmarks
import cv2

class TestFeatureExtraction(unittest.TestCase):
    def test_facial_landmarks(self):
        frame = cv2.imread('data/frames/test_frame.jpg')
        features = get_facial_landmarks(frame)
        self.assertTrue(len(features) > 0, "No facial features detected")
