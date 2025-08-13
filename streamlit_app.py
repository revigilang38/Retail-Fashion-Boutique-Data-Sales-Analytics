import streamlit as st
import prediction
import eda


navigation = st.sidebar.selectbox('Choose Page:', ('Model Prediction', 'EDA'))

if navigation == 'EDA':
    eda.run()
else:
    prediction.run()
