import streamlit as st
import pandas as pd
import plotly.express as px

db = pd.read_csv('production.csv')

st.title("日本の食料生産量")
st.subheader('-日本国内の生産量を、1960年から2024年までのデータから種類別に調べることができます。-')
st.caption('画面左のサイドバーで条件指定')
with st.sidebar:
    st.subheader('調べる種類')
    st.selectbox('選択してください', db['kind'].unique())
    st.subheader('調べる範囲')
    st.slider()

st.bar_chart(db)