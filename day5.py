import pandas as pd
import streamlit as st

d = st.sidebar.multiselect("Pick first column", [1, 2, 3, 4])
v = st.sidebar.slider("Pick second column", 0, 40)
    
df = pd.DataFrame({
     'first column': [1, 2, 3, 4],
     'second column': [10, 20, 30, 40]
     })

st.dataframe(df[(df['second column'] <= v) & (df['first column'].isin(d))])