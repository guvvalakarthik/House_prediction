# -*- coding: utf-8 -*-
"""
Created on Mon Feb  2 18:24:59 2026

@author: manoj
"""

import streamlit as st
import numpy as np
import pickle

# Load saved model
model = pickle.load(open('House_prediction.sav', 'rb'))

st.title("🏠 House Price Prediction System")

# Input fields
medinc = st.number_input("Median Income (MedInc)", min_value=0.0)
houseage = st.number_input("House Age (HouseAge)", min_value=0.0)
averooms = st.number_input("Average Rooms (AveRooms)", min_value=0.0)
avebedrms = st.number_input("Average Bedrooms (AveBedrms)", min_value=0.0)
population = st.number_input("Population", min_value=0.0)
aveoccup = st.number_input("Average Occupancy (AveOccup)", min_value=0.0)
latitude = st.number_input("Latitude", min_value=0.0)
longitude = st.number_input("Longitude", min_value=0.0)

# Prediction button
if st.button("Predict House Price"):
    input_data = np.array([[medinc, houseage, averooms, avebedrms,
                             population, aveoccup, latitude, longitude]])
    
    prediction = model.predict(input_data)

    st.success(f"🏡 Predicted House Price: {prediction[0]:.2f}")
