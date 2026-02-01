import streamlit as st
import pandas as pd
import plotly.express as px

db = pd.read_csv('production.csv')

st.title("日本の食料生産量")
st.subheader('-日本国内の生産量を、1961年から2024年までのデータから種類別に調べることができます。-')
st.caption('画面左で条件指定')

col = st.columns(2)
kinds = [i for i in db.columns if i != "kind"] #kindを除く1列目の要素をリストにする
db['年'] = db['kind'] #年の1961~2024の列をdbに追加する

with col[0].container(border=True):
    st.subheader('調べる種類')
    kind = st.selectbox('選択してください', kinds)
    st.subheader('グラフの種類')
    chart = st.radio('選択してください', ["折れ線", "棒グラフ"])

fdb = db[["年", kind]] #選択したkindだけ取る

if chart == "折れ線":
    fig = px.line(fdb, x="年", y=kind, labels={kind:f'{kind}  (1000トン)'})
elif chart == "棒グラフ":
    fig = px.bar(fdb, x="年", y=kind)

with col[1].container():
    st.text(f"現在選択中  --{kind}--")
    st.plotly_chart(fig)

activated = st.toggle("すべてのデータ")
if activated == True:
    st.bar_chart(db, x="年")
    st.table(db)

st.subheader("グラフからわかること")
st.text('食料生産量は品目別にみても1980年頃～2000年頃がピークであり、それ以降は年々生産量は落ちてきている。')