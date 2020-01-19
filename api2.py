import io
import os

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

# Instantiates a client
client = vision.ImageAnnotatorClient()


def getImageInfo(file_name):
    # The name of the image file to annotate
    file_name = os.path.abspath(file_name)

    # Loads the image into memory
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    # Performs label detection on the image file
    response = client.label_detection(image=image)
    labels = response.label_annotations

    info = []
    # print('Labels:')
    
    for label in labels:
        print(label.description)
        info.append(label.description)
    return info

# getImageInfo("C:\\Users\\hamad\\Desktop\\Images\\Water Bottle.jpg")
