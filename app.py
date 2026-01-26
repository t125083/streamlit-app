import streamlit as st
import pandas as pd
import plotly.express as px

db1 = pd.read_csv('consumption.csv')
db2 = pd.read_csv('production.csv')

st.title('日本の食料自給率')