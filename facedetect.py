import os
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.face import FaceClient

def get_face_client():
    """Create an authenticated FaceClient."""
    SUBSCRIPTION_KEY = os.environ["COGNITIVE_SERVICE_KEY"]
    ENDPOINT = os.environ["COGNITIVE_SERVICE_ENDPOINT"]
    credential = CognitiveServicesCredentials(SUBSCRIPTION_KEY)
    return FaceClient(ENDPOINT, credential)

face_client = get_face_client()

#url = "https://docs.microsoft.com/en-us/learn/data-ai-cert/identify-faces-with-computer-vision/media/clo19_ubisoft_azure_068.png"
url = "https://i.ibb.co/ckhVtpr/image4.png"

attributes = ["emotion", "glasses", "smile"]
include_id = True
include_landmarks = False

detected_faces = face_client.face.detect_with_url(url, include_id, include_landmarks, attributes, raw=True)

if not detected_faces:
    raise Exception('No face detected in image')

print(detected_faces.response.json())