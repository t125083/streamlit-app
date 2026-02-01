import streamlit as st
import pandas as pd
import plotly.express as px

db = pd.read_csv('production.csv')

st.title("日本の食料生産量")
st.subheader('-日本国内の生産量を、1961年から2024年までのデータから種類別に調べることができます。-')
st.caption('画面左のサイドバーで条件指定')

kind = [i for i in db.columns if i != "kind"]

with st.sidebar:
    st.subheader('調べる種類')
    kind = st.selectbox('選択してください', kind)
    st.subheader('調べる範囲')
    minyear = st.slider(label='開始年を選択', min_value=1961, max_value=2024, value=1961)
    maxyear = st.slider(label='終了年を選択', min_value=1961, max_value=2024, value=2024)
    chart = st.radio("グラフ選択", ["折れ線", "棒グラフ"])

fdb = [i for i in db if i != minyear]
if chart == "折れ線":
    st.line_chart(db)
elif chart == "棒グラフ":
    st.bar_chart(db)