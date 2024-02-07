import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Load the selling price model
with open ("C:\\Users\\User\\Downloads\\copper_model_regression_final.pkl", 'rb') as f:
    selling_price_model = pickle.load(f)

# Load the status prediction model

with open("C:\\Users\\User\\Downloads\\copper_model_class_final.pkl", 'rb') as f:
    model = pickle.load(f)


# data set features 
status_options = ['Won', 'Draft', 'To be approved', 'Lost', 'Not lost for AM', 'Wonderful', 'Revised', 'Offered', 'Offerable']
item_type_options = ['W', 'WI', 'S', 'Others', 'PL', 'IPL', 'SLAWR']
country_options = [28., 25., 30., 32., 38., 78., 27., 77., 113., 79., 26., 39., 40., 84., 80., 107., 89.]
application_options = [10., 41., 28., 59., 15., 4., 38., 56., 42., 26., 27., 19., 20., 66., 29., 22., 40., 25., 67., 79., 3., 99., 2., 5., 39., 69., 70., 65., 58., 68.]
product_options = ['611112', '611728', '628112', '628117', '628377', '640400', '640405', '640665', '611993', '929423819', '1282007633', '1332077137', '164141591', '164336407', '164337175', '1665572032', '1665572374', '1665584320', '1665584642', '1665584662', '1668701376', '1668701698', '1668701718', '1668701725', '1670798778', '1671863738', '1671876026', '1690738206', '1690738219', '1693867550', '1693867563', '1721130331', '1722207579']

# Streamlit app
st.title("Copper Selling Price Prediction & Copper Status Prediction")

# Collect user input for selling price prediction
st.write("## Selling Price Prediction")
status = st.selectbox("Status", status_options, key=1)
item_type = st.selectbox("Item Type", item_type_options, key=2)
country = st.selectbox("Country", country_options, key=3)
application = st.selectbox("Application", application_options, key=4)
product_ref = st.selectbox("Product Reference", product_options, key=5)

quantity_tons = st.text_input("Enter Quantity Tons (Min:611728 & Max:1722207579)", key=6)
thickness = st.text_input("Enter Thickness (Min:0.18 & Max:400)", key=7)
width = st.text_input("Enter Width (Min:1, Max:2990)", key=8)
customer = st.text_input("Customer ID (Min:12458, Max:30408185)", key=9)

if st.button("Predict Selling Price"):
    try:
        new_sample = np.array([[np.log(float(quantity_tons)), application, np.log(float(thickness)), float(width), country, float(customer), int(product_ref), item_type]])

        # One-hot encode categorical variables
        new_sample_encoded = pd.get_dummies(pd.DataFrame(new_sample, columns=['quantity_tons', 'application', 'thickness', 'width', 'country', 'customer', 'product_ref', 'item_type']), columns=['item_type'])

        # Convert to NumPy array for prediction
        new_sample_array = new_sample_encoded.values

        # Make the prediction
        predicted_selling_price = selling_price_model.predict(new_sample_array)
        st.write(f"Predicted Selling Price: {np.exp(predicted_selling_price)}")
    except Exception as e:
        st.write(f"Error: {e}")

# Collect user input for selling price in log scale
st.write("## Selling Price in Log Scale")
selling_price_log = st.text_input("Enter Selling Price (log scale):", key=10)

if st.button("Predict Selling Price (Log Scale)"):
    try:
        selling_price_log = float(selling_price_log)
        new_sample = np.array([[np.log(float(quantity_tons)), application, np.log(float(thickness)), float(width), country, float(customer), int(product_ref), item_type, status, selling_price_log]])

        # One-hot encode categorical variables
        new_sample_encoded = pd.get_dummies(pd.DataFrame(new_sample, columns=['quantity_tons', 'application', 'thickness', 'width', 'country', 'customer', 'product_ref', 'item_type', 'status']), columns=['item_type', 'status'])

        # Convert to NumPy array for prediction
        new_sample_array = new_sample_encoded.values

        # Make the prediction
        predicted_selling_price = selling_price_model.predict(new_sample_array)
        st.write(f"Predicted Selling Price: {np.exp(predicted_selling_price)}")
    except Exception as e:
        st.write(f"Error: {e}")

# Collect user input for status prediction
st.write("## Status Prediction")
item_type_status = st.selectbox("Item Type", item_type_options, key=11)
country_status = st.selectbox("Country", country_options, key=12)
application_status = st.selectbox("Application", application_options, key=13)
product_ref_status = st.selectbox("Product Reference", product_options, key=14)

quantity_tons_status = st.text_input("Enter Quantity Tons (Min:611728 & Max:1722207579)", key=15)
thickness_status = st.text_input("Enter Thickness (Min:0.18 & Max:400)", key=16)
width_status = st.text_input("Enter Width (Min:1, Max:2990)", key=17)
customer_status = st.text_input("Customer ID (Min:12458, Max:30408185)", key=18)

if st.button("Predict Status"):
    try:
        new_sample_status = np.array([[np.log(float(quantity_tons_status)), application_status, np.log(float(thickness_status)), float(width_status), country_status, float(customer_status), int(product_ref_status), item_type_status]])

        # One-hot encode categorical variables
        new_sample_encoded_status = pd.get_dummies(pd.DataFrame(new_sample_status, columns=['quantity_tons', 'application', 'thickness', 'width', 'country', 'customer', 'product_ref', 'item_type']), columns=['item_type'])

        # Convert to NumPy array for prediction
        new_sample_array_status = new_sample_encoded_status.values

        # Make the prediction
        predicted_status = status_model.predict(new_sample_array_status)
        if predicted_status == 1:
            st.write('## :green[The Status is Won] ')
        else:
            st.write('## :red[The status is Lost] ')
    except Exception as e:
        st.write(f"Error: {e}")

# Display app creator information
st.write("## App Created by THangam")
