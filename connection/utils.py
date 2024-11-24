import numpy as np

import cv2

import tensorflow as tf

from streamlit_webrtc import webrtc_streamer, VideoTransformerBase

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import os
import base64

classifier =tf.keras.models.load_model("vgg_model.h5")
#classifier2 =load_model("custom_model.h5") 

# load weights into new model
classifier.load_weights("vgg_model.h5")


emotion_dict = ["Angry","Disgust","Fear","Happy","Neutral","Sad","Surprise"]
class VideoTransformer_1(VideoTransformerBase): 
    def transform(self, img):
        # img = frame.to_ndarray(format="bgr24")
        face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        #image gray
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(
            image=img_gray, scaleFactor=1.3, minNeighbors=5)
        for (x, y, w, h) in faces:
            cv2.rectangle(img=img, pt1=(x, y), pt2=(
                x + w, y + h), color=(255, 0, 0), thickness=2)
            roi_gray = img_gray[y:y + h, x:x + w]
            roi_gray = cv2.resize(roi_gray, (48, 48), interpolation=cv2.INTER_AREA)
            if np.sum([roi_gray]) != 0:
                roi = roi_gray.astype('float') / 255.0
                roi = tf.keras.preprocessing.image.img_to_array(roi)
                roi = np.expand_dims(roi, axis=0)
                prediction = classifier.predict(roi)[0]
                maxindex = int(np.argmax(prediction))
                finalout = emotion_dict[maxindex]
                output = str(finalout)
            label_position = (x, y)
            cv2.putText(img, output, label_position, cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        plt.imshow(img)
        plt.show()

        return img

def conversion(x):
    image = cv2.cvtColor(x, cv2.COLOR_BGR2RGB)

    # Encode the image to base64 format
    _, buffer = cv2.imencode('.jpg', image)
    base64_img = base64.b64encode(buffer).decode('utf-8')
    return base64_img
    
def base64_to_3d_array(base64_string):
    try:
        # Remove the header if it exists
        if base64_string.startswith('data:image'):
            base64_string = base64_string.split(',')[1]

        # Decode the base64 string to binary image data
        image_data = base64.b64decode(base64_string)

        # Convert the binary image data to a numpy array
        nparr = np.frombuffer(image_data, np.uint8)

        # Decode the numpy array to an image using OpenCV
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        # Check if the image is not empty
        if img is not None:
            # Convert the image to a 3D numpy array
            img_array = np.array(img)
        else:
            print("Failed to decode image data.")
    except Exception as e:
        print("Error:", e)

    obj=VideoTransformer_1()
    x=obj.transform(img_array)
    return "data:image/jpeg;base64,"+ conversion(x)