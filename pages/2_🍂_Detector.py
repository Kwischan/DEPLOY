import os
import streamlit as st
import numpy as np
from PIL import Image
from keras.models import load_model


model1 = load_model('Models/LettuceModel.h5')  # saved model from training
model2 = load_model('Models/CauliflowerModel.h5')  # saved model from training
model3 = load_model('Models/SugarcaneModel-1.h5')  # saved model from training
model4 = load_model('Models/PepperModel.h5')  # saved model from training

Lettuce_names = ["lettuce_BacterialLeafSpot", "lettuce_BotrytisCrownRot", "lettuce_DownyMildew", "lettuce_Healthy"]

Cauliflower_names = ["cauliflower_BlackRot", "cauliflower_DownyMildew", "cauliflower_Healthy", "cauliflower_SoftRot"]

Sugarcane_names = ["sugarcane_Healthy", "sugarcane_Mosaic", "sugarcane_RedRot", "sugarcane_Rust"]

Pepper_names = ["pepper_Healthy", "pepper_CercosporaLeafSpot", "pepper_Fusarium", "pepper_Leaf_Curl"]

folder_path = "saved_images"

def preprocess_image(image_path):
    img = Image.open(image_path)
    img = img.resize((256, 256))  # Resize image to match model's input shape
    img_array = np.array(img) / 255.0  # Normalize pixel values to range [0, 1]
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    return img_array

def L_predict_disease(image_path):
    preprocessed_img = preprocess_image(image_path)
    prediction = model1.predict(preprocessed_img)
    disease_index = np.argmax(prediction)  # Get the index of the predicted Lettuce class
    disease_class = Lettuce_names[disease_index] # Fetch the class name using the index
    return disease_class

def C_predict_disease(image_path):
    preprocessed_img = preprocess_image(image_path)
    prediction = model2.predict(preprocessed_img)
    disease_index = np.argmax(prediction)  # Get the index of the predicted Cauliflower class
    disease_class = Cauliflower_names[disease_index] # Fetch the class name using the index
    return disease_class

def S_predict_disease(image_path):
    preprocessed_img = preprocess_image(image_path)
    prediction = model3.predict(preprocessed_img)
    disease_index = np.argmax(prediction)  # Get the index of the predicted Sugarcane class
    disease_class = Sugarcane_names[disease_index] # Fetch the class name using the index
    return disease_class

def P_predict_disease(image_path):
    preprocessed_img = preprocess_image(image_path)
    prediction = model4.predict(preprocessed_img)
    disease_index = np.argmax(prediction)  # Get the index of the predicted Pepper class
    disease_class = Pepper_names[disease_index] # Fetch the class name using the index
    return disease_class

# selecting method for health assessment
st.subheader("SELECT A METHOD")
pick = st.selectbox("Select Method",('Upload','Camera'),label_visibility="hidden")

if pick == 'Camera':
    st.subheader("Camera Input")
    plantpic = st.camera_input("take a plant picture",label_visibility="hidden")

    st.subheader("Select A Plant")
    select = st.selectbox("Select Plant",('Lettuce','Cauliflower','Sugarcane','Pepper'),label_visibility="hidden")
        
    submit = st.button("submit",use_container_width=True)

    if submit:
        if not plantpic:
            st.write("take a photo!")
            
        elif select == 'Lettuce':
            # predicting Lettuce disease
            image_path = plantpic
            predicted_class = L_predict_disease(image_path)
            pred1 = "Predicted Disease Class: " + predicted_class
            st.image(plantpic,pred1)
            
        elif select == 'Cauliflower':
            # predicting Cauliflower disease
            image_path = plantpic
            predicted_class = C_predict_disease(image_path)
            pred2 = "Predicted Disease Class: " + predicted_class
            st.image(plantpic,pred2)
            
        elif select == 'Sugarcane':
            # predicting Sugarcane disease
            image_path = plantpic
            predicted_class = S_predict_disease(image_path)
            pred3 = "Predicted Disease Class: " + predicted_class
            st.image(plantpic,pred3)
            
        elif select == 'Pepper':
            # predicting Pepper disease
            image_path = plantpic
            predicted_class = P_predict_disease(image_path)
            pred4 = "Predicted Disease Class: " + predicted_class
            st.image(plantpic,pred4)
            
        
elif pick == 'Upload':
        
    st.subheader("Upload Image File")
    plantpic = st.file_uploader("upload",['jpg','png','gif','webp','tiff','psd','raw','bmp','jfif'],False,label_visibility="hidden")

    st.subheader("Select A Plant")
    select = st.selectbox("Select Plant",('Lettuce','Cauliflower','Sugarcane','Pepper'),label_visibility="hidden")

    submit1 = st.button("submit",use_container_width=True)
    if submit1:
        if not plantpic:
            st.write("take a photo!")
            
        elif select == 'Lettuce':
            # predicting Lettuce disease
            image_path = plantpic
            predicted_class = L_predict_disease(image_path)
            pred1 = "Predicted Disease Class: " + predicted_class
            st.image(plantpic,pred1)
            
        elif select == 'Cauliflower':
            # predicting Cauliflower disease
            image_path = plantpic
            predicted_class = C_predict_disease(image_path)
            pred2 = "Predicted Disease Class: " + predicted_class
            st.image(plantpic,pred2)
            
        elif select == 'Sugarcane':
            # predicting Sugarcane disease
            image_path = plantpic
            predicted_class = S_predict_disease(image_path)
            pred3 = "Predicted Disease Class: " + predicted_class
            st.image(plantpic,pred3)
            
        elif select == 'Pepper':
            # predicting Pepper disease
            image_path = plantpic
            predicted_class = P_predict_disease(image_path)
            pred4 = "Predicted Disease Class: " + predicted_class
            st.image(plantpic,pred4)
                
    

