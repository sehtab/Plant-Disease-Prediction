#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 18:07:42 2022

@author: Sehtab
"""

# import libraries
import numpy as np
import streamlit as st
import cv2
from tensorflow.keras.models import load_model

# loading the model
model = load_model('plant_disease.h5')

# name of classes
class_name = ['Corn-Common_rust', 'Potato-Early_blight', 'Tomato-Bacterial_spot']

# Setting title of App
st.title('Plant Disease Ditection')
st.markdown('Upload an image of the plant leaf')

# uploading the leaf image
plant_image = st.file_uploader("Choose an image...", type='jpg')
submit = st.button('Predict')

if submit:
    if plant_image is not None:
        
        # convert the file to an opencv image.
        file_bytes = np.asarray(bytearray(plant_image.read()), dtype=np.uint8)
        opencv_image = cv2.imdecode(file_bytes, 1)
        
        # Display the image
        st.image(opencv_image, channels='BGR')
        st.write(opencv_image.shape)
        # resizing the image
        opencv_image = cv2.resize(opencv_image,(256,256))
        # convert image to 4 dimensions
        opencv_image.shape = (1,256,256,3)
        # make prediction
        y_pred= model.predict(opencv_image)
        result = class_name[np.argmax(y_pred)]
        st.title(str('This is '+result.split('-')[0]+ 'leaf with ' +result.split('-')[1]))
        
