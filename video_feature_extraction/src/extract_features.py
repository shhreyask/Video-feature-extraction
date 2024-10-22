import unittest
from src.models.faceplusplus_attributes import extract_face_attributes
import cv2

class TestFaceAttributeExtraction(unittest.TestCase):
    def test_face_attributes(self):
        frame = cv2.imread('data/frames/test_frame.jpg')
        attributes = extract_face_attributes(frame)
        self.assertTrue("age" in attributes, "No age attribute detected")
        self.assertTrue("gender" in attributes, "No gender attribute detected")

if __name__ == '__main__':
    unittest.main()
