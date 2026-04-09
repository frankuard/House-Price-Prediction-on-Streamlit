import streamlit as st
import numpy as np
import pickle

model = pickle.load(open("model.pkl", "rb"))

st.set_page_config(page_title="House Predictor", page_icon="🏡")


st.markdown(""" <h1 style='text-align: left; color: #4CAF50;'>
        🏠 House Price Prediction <span style='text-align: center; color: orange;'>
        App
    </h1>  """,unsafe_allow_html=True)

st.markdown("""<p style='text-align: left; font-size:18px; color:gray;'>
Enter the house details below and get an estimated price prediction.
</p>""", unsafe_allow_html=True)


st.subheader("Enter Details:")

st.markdown("""
<p style='font-size:20px; font-weight:bold; color:black;'>
Area (sq ft)
</p>
""", unsafe_allow_html=True)

area = st.slider("", min_value=1000, max_value=10000, value=500)

st.markdown("""
<p style='font-size:20px; font-weight:bold; color:black;'>
Bedrooms
</p>
""", unsafe_allow_html=True)

bedrooms = st.slider("",min_value=1,max_value=10, value=3)

st.markdown("""
<p style='font-size:20px; font-weight:bold; color:black;'>
Bathrooms
</p>
""", unsafe_allow_html=True)

bathrooms = st.slider("",min_value=1,max_value=5,value=2)

st.markdown("""
<p style='font-size:20px; font-weight:bold; color:black;'>
Stories
</p>
""", unsafe_allow_html=True)

stories = st.slider("",min_value=1,max_value=4,value=2)

st.markdown("""
<p style='font-size:20px; font-weight:bold; color:black;'>
Parking
</p>
""", unsafe_allow_html=True)

parking = st.slider("",min_value=0,max_value=5,value=1)

st.markdown("""
<p style='font-size:20px; font-weight:bold; color:black;'>
Air Conditioning
</p>
""", unsafe_allow_html=True)

airconditioning = st.selectbox("", ["Yes", "No"])

st.markdown("""
<p style='font-size:20px; font-weight:bold; color:black;'>
Main Road
</p>
""", unsafe_allow_html=True)

mainroad = st.selectbox(" ",["Yes", "No"])


st.markdown("""
<p style='font-size:20px; font-weight:bold; color:black;'>
Guest Room
</p>
""", unsafe_allow_html=True)

guestroom = st.selectbox("  ", ["Yes", "No"])

st.markdown("""
<p style='font-size:20px; font-weight:bold; color:black;'>
Basement
</p>
""", unsafe_allow_html=True)

basement = st.selectbox("   ", ["Yes", "No"])

st.markdown("""
<p style='font-size:20px; font-weight:bold; color:black;'>
Pref Area
</p>
""", unsafe_allow_html=True)

prefarea = st.selectbox("    ", ["Yes", "No"])

st.markdown("""
<p style='font-size:20px; font-weight:bold; color:black;'>
Furnishing
</p>
""", unsafe_allow_html=True)

furnishing = st.selectbox("     ", ["Furnished", "Semi", "Unfurnished"])



if st.button("Predict Price"):
    
    ## CATERGORICAL DATA TO NUMERIC
    airconditioning = 1 if airconditioning == "Yes" else 0
    mainroad = 1 if mainroad == "Yes" else 0
    guestroom = 1 if guestroom == "Yes" else 0
    basement = 1 if basement == "Yes" else 0
    prefarea = 1 if prefarea == "Yes" else 0

    ## FEATURE ENGINEERING
    area_per_bedroom = area / bedrooms
    area_per_bathroom = area / bathrooms
    total_rooms = bedrooms + bathrooms + stories

    furnishing_unfurnished = 1 if furnishing == "Unfurnished" else 0
    
    features = np.array([[area,bedrooms,bathrooms,stories,parking,mainroad,guestroom,basement,airconditioning,prefarea,furnishing_unfurnished,area_per_bedroom,area_per_bathroom,total_rooms]])

    prediction = model.predict(features)

    st.success(f"Predicted Price: {prediction[0]:,.2f}")