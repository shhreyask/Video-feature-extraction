import requests
import cv2
import base64
import os

# Face++ API credentials
API_KEY = 'YE5AQ6tYG1DzulgFWrSTBUGps65Buf3V'
API_SECRET = 'a4Rws5ur6Ynij3SgeQ_jc-eZtJgONX-I'

def frame_to_base64(frame):
    """
    Convert a video frame (image) to a base64-encoded string for the Face++ API.
    """
    _, buffer = cv2.imencode('.jpg', frame)
    base64_str = base64.b64encode(buffer).decode('utf-8')
    return base64_str

def extract_face_attributes(frame):
    """
    Send the frame to the Face++ API to extract facial attributes.
    
    :param frame: The image frame (numpy array).
    :return: Dictionary of facial attributes (e.g., skin tone, hair color).
    """
    url = 'https://api-us.faceplusplus.com/facepp/v3/detect'
    image_base64 = frame_to_base64(frame)
    
    data = {
        'api_key': API_KEY,
        'api_secret': API_SECRET,
        'image_base64': image_base64,
        'return_attributes': 'gender,age,smiling,ethnicity,beauty,mouthstatus,skinstatus',
    }
    
    response = requests.post(url, data=data)
    attributes = process_faceplusplus_response(response.json())
    return attributes

def process_faceplusplus_response(response_json):
    """
    Process the JSON response from Face++ to extract relevant attributes.
    
    :param response_json: The JSON response from the Face++ API.
    :return: A dictionary containing the relevant facial attributes.
    """
    faces = response_json.get('faces', [])
    if not faces:
        return {}

    attributes = faces[0].get('attributes', {})
    
    # Example: Extracting specific attributes like hair color, skin status, etc.
    extracted_attributes = {
        "age": attributes.get('age', {}).get('value', 'N/A'),
        "gender": attributes.get('gender', {}).get('value', 'N/A'),
        "ethnicity": attributes.get('ethnicity', {}).get('value', 'N/A'),
        "beauty": {
            "male_score": attributes.get('beauty', {}).get('male_score', 'N/A'),
            "female_score": attributes.get('beauty', {}).get('female_score', 'N/A')
        },
        "skin_status": attributes.get('skinstatus', {}),
        
    }
    
    return extracted_attributes
