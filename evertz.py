import streamlit as st
import numpy as np
import pandas as pd
import time
import snowflake.connector

from PIL import Image

df=pd.read_csv(r'C:/Users/pavann/Downloads/easelive.csv')

st.write(df)





image = Image.open("C:/Users/pavann/Downloads/logo.png")
original_title = '<p style="font-family:Courier; color:Black; font-size: 50px; font-weight: bold;">Evertz</p>'
st.markdown(original_title, unsafe_allow_html=True)

st.image(image)

original_title = '<p style="font-family:Courier; color:Black; font-size: 50px; font-weight: bold;">Devices</p>'
st.markdown(original_title, unsafe_allow_html=True)

clo1,col2=st.columns(2)

