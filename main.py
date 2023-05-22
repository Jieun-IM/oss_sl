import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import graphviz as graphviz

st.title("Total_Investment")
st.subheader("IMF, 2021~2023, 총투자")  # https://kosis.kr/statHtml/statHtml.do?orgId=101&tblId=DT_2WEO009&vw_cd=MT_RTITLE&list_id=R_SUB_OTITLE_OTIT_IMFTIT_001&scrId=&seqNo=&lang_mode=ko&obj_var_id=&itm_id=&conn_path=MT_RTITLE&path=%252FstatisticsList%252FstatisticsListIndex.do

df = pd.read_csv('./data/Total_Investment_20230522224509.csv')
df.set_index = df[["2021", "2022", "2023"]]

if st.button('data copyright link'):
    st.write('https://kosis.kr/statHtml/statHtml.do?orgId=101&tblId=DT_2WEO009&vw_cd=MT_RTITLE&list_id=R_SUB_OTITLE_OTIT_IMFTIT_001&scrId=&seqNo=&lang_mode=ko&obj_var_id=&itm_id=&conn_path=MT_RTITLE&path=%252FstatisticsList%252FstatisticsListIndex.do')
    
if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(df)
