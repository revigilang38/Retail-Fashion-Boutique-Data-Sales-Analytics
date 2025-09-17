import pandas as pd
import prediction
import eda
import streamlit as st

nav = st.sidebar.selectbox("Navigation", ["EDA", "Prediction"])

if nav == "EDA":
    eda.run()
elif nav == "Prediction":
    prediction.run()
