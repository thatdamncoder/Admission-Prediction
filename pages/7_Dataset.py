import numpy as np
import pandas as pd
import streamlit as st

st.title("Take a look at the data!")
st.write("Data size:  500 x 8 ")
st.divider()

col1,col2=st.columns(2)

with col1:
    st.write("The DataFrame")
    df=pd.read_csv("admission_data.csv")
    st.dataframe(df)

with col2:
    st.write("Statistics of the Dataset")
    st.dataframe(df.describe())


