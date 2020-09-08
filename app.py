from pycaret.regression import load_model, predict_model
import streamlit as st
import pandas as pd 
from numpy import mean
from numpy import asarray
from numpy import std
from sklearn.datasets import make_regression
from sklearn.model_selection import RepeatedKFold
import keras
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
import os, urllib, cv2




# https://pycaret.org/ for documentation

# Load trained model for predictions
model = load_model('ScrapeOB_lr_model_0907')

# define function to call 
def predict(model, input_df):
    predictions_df = predict_model(estimator=model, data=input_df)
    predictions = predictions_df['Label'][0]
    return predictions

# main functino starts here

def run():
    st.title('Growth Hackers: Online Business Price Predictor')
    from PIL import Image
    # gets images to populate
    image = Image.open('ecomm.jpg')
    image_building = Image.open('shop2.jpg')

    st.image(image,use_column_width=False)

    # this adds a sidebar
    add_selectbox = st.sidebar.selectbox(
        "How would you like to predict?",
        ('Price Predictor 🔮', 'Find Your Growth Target 🎯')
    )

    st.sidebar.info('This app is created to predict prices for Online Business')
    st.sidebar.success('https://github.com/alxanderpierre/growth_hackers')

    st.sidebar.image(image_building)

    
    st.markdown('This project is for predicting 🔮 sell prices 💰 of Online Businesses 🖥 . As well as predicting Growth Targets📈📊for Online Business owners 👩‍💻👨‍💻.')
    st.markdown('What are Growth Targets 🎯 you may ask ?? 🤔. Simple, it is a target for a business to reach in order to sell at a particular price 😁.')
    
    st.markdown(' 👈 **Please select  _Price Predictor_ or _Find Your Growth Target_ in the sidebar to start.**')
    
    # for online predictions
    if add_selectbox == 'Price Predictor 🔮':

        # capturing all inputs required for prediction using streamlit widgets
        monthly_revenue = st.number_input('Monthly Revenue', min_value = 1500, max_value = 100000, value=2500)
        # price = st.number_input('Price',min_value= 30000, max_value = 5000000)
        
        net = st.number_input('Net', min_value=1000, max_value=100000, value=5000)
        page_views = st.number_input('Page Views', min_value=200, max_value=3000000, value= 1000)
        unique_users = st.number_input('Unique Users',min_value=50, max_value=2000000, value= 1000)

        platfrom = st.multiselect('Platform',options= ['Shopify','WordPress','Amazon FBA','Other'])
        monetization = st.multiselect(
            'Monetization', options= [
            'Affiliate','Amazon Associates','Amazon FBA','Amazon FBM',
            'Amazon KDP','Amazon Merch','Application','DropShipping','Digital Product',
            'Display Advertising','Digital Product','eCommerce',
            'Info Product ','Lead Gen','Other', 'SaaS',' Service', 'Subscription'])

        pricing_period = st.slider('Pricing Period',min_value=3, max_value=12, value=6)
        domain_type = st.multiselect('Domain Type', options= ['.com','.co','.uk','.ca','.it',
                                                                '.fr','.de','.es','.jp','.au','.app',
                                                                '.net', '.biz', '.reviews', '.org'])
       
    
        output=""

        input_dict = {'monthly_revenue' : monthly_revenue, 'net' : net, 'page_views':page_views, 'unique_users' : unique_users, 'platfrom' : platfrom, 'monetization' : monetization,'pricing_period': pricing_period, 'domain_type': domain_type}
        input_df = pd.DataFrame([input_dict])

        # calling predict function when predict button is clicked
        if st.button('Predict'):
            output = predict(model=model, input_df=input_df)
            output = int(output)
            st.success('Perdicted Price {}'.format(output))



   
        


if __name__ == '__main__':
    run()