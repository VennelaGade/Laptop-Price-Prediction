import streamlit as st
import joblib
import pandas as pd

# Load the trained model
model = joblib.load('laptop_price_model.pkl')  # Ensure the model path is correct

# Title for the app
st.title('Laptop Price Prediction')

# Sidebar for user input
st.sidebar.header('Laptop Features')

def user_input_features():
    # Get user input from sidebar
    brand = st.sidebar.selectbox('Brand', ['Dell', 'HP', 'Apple', 'Acer', 'Asus', 'Lenovo', 'MSI', 'Microsoft', 'Toshiba', 'Samsung'])
    laptop_type = st.sidebar.selectbox('Type', ['Ultrabook', 'Notebook', 'Netbook', 'Gaming', '2 in 1 Convertible'])
    ram = st.sidebar.slider('RAM (GB)', 4, 64, 8)
    weight = st.sidebar.slider('Weight (kg)', 1.0, 4.0, 2.5)
    touchscreen = st.sidebar.selectbox('Touchscreen', ['Yes', 'No'])
    ips_display = st.sidebar.selectbox('IPS Display', ['Yes', 'No'])
    screen_size = st.sidebar.slider('Screen Size (inches)', 10.0, 18.0, 15.6)
    screen_resolution = st.sidebar.selectbox('Screen Resolution', ['1920x1080', '1366x768', '1600x900', '3200x1800', '3840x2160'])
    cpu = st.sidebar.selectbox('CPU', ['Intel Core i3', 'Intel Core i5', 'Intel Core i7', 'Intel Core i9', 'AMD Ryzen 3', 'AMD Ryzen 5', 'AMD Ryzen 7'])
    hdd = st.sidebar.slider('HDD (GB)', 0, 2048, 0)  # Slider from 0 GB to 2 TB
    ssd = st.sidebar.slider('SSD (GB)', 0, 2048, 256)  # Slider from 0 GB to 2 TB
    gpu = st.sidebar.selectbox('GPU', ['Intel', 'Nvidia', 'AMD', 'No GPU'])
    os = st.sidebar.selectbox('Operating System', ['Windows', 'MacOS', 'Linux', 'Chrome OS', 'No OS'])

    # Create a dataframe for the input data
    data = {
        'Brand': brand,
        'Type': laptop_type,
        'RAM': ram,
        'Weight': weight,
        'Touchscreen': touchscreen,
        'IPS': ips_display,
        'Screen Size': screen_size,
        'Screen Resolution': screen_resolution,
        'CPU': cpu,
        'HDD': hdd,
        'SSD': ssd,
        'GPU': gpu,
        'OS': os
    }
    
    features = pd.DataFrame([data])
    return features

# Get user input
input_df = user_input_features()

# Display the input data
st.subheader('User Input:')
st.write(input_df)

# Make prediction when the user clicks "Predict"
if st.button('Predict'):
    prediction = model.predict(input_df)  # Use the model to make predictions
    st.subheader('Predicted Laptop Price:')
    st.write(f"${prediction[0]:.2f}")
