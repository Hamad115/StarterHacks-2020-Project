import io
import os
from tkinter import *
window=Tk()
window.geometry("300x300")
window.title("WeCycle")

label1 = Label(window,text="WeCycle", fg = "blue" , bg = "yellow", font = ("arial", 16, "bold")).place (x = 110, y = 110)

button1= Button(window,text = "Upload Image", fg = "blue", bg="brown", font = ("arial",12,"bold"))
button1.place (x = 110, y = 110)

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

# Instantiates a client
client = vision.ImageAnnotatorClient()

# The name of the image file to annotate
file_name = os.path.abspath("C:\\Users\\hamad\\Desktop\\Images\\Water Bottle.jpg")

# Loads the image into memory
with io.open(file_name, 'rb') as image_file:
    content = image_file.read()

image = types.Image(content=content)

# Performs label detection on the image file
response = client.label_detection(image=image)
labels = response.label_annotations

print('Labels:')
for label in labels:
    print(label.description)

'''
from tkinter import *
root = Tk()
s = Canvas(root, width =  , maxheight, background = "white")
s.pack ()
s.update()
'''

window.mainloop()