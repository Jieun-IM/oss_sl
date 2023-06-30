import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import graphviz as graphviz

st.title("Total_Investment")
st.subheader("IMF, 2021~2023, 총투자")  # https://kosis.kr/statHtml/statHtml.do?orgId=101&tblId=DT_2WEO009&vw_cd=MT_RTITLE&list_id=R_SUB_OTITLE_OTIT_IMFTIT_001&scrId=&seqNo=&lang_mode=ko&obj_var_id=&itm_id=&conn_path=MT_RTITLE&path=%252FstatisticsList%252FstatisticsListIndex.do

df = pd.read_csv('./data/Total_Investment_20230522224509.csv')


df['Continent'] = 'ASIA'

df.iloc[45:48, 4] = 'NORTH AMERICA'
df.iloc[49:78, 4] = 'SOUTH AMERICA'
df.iloc[79:119, 4] = 'EUROPE'
df.iloc[120:170, 4] = 'AFRICA'
df.iloc[171: , 4] = 'OCEANIA'
df.drop([0, 44, 48, 78, 119, 170], axis=0, inplace=True)

groups_two = df.groupby(['Continent', 'Country'])
multi_index = groups_two.first()

if st.button('data copyright link'):
    st.write('https://kosis.kr/statHtml/statHtml.do?orgId=101&tblId=DT_2WEO009&vw_cd=MT_RTITLE&list_id=R_SUB_OTITLE_OTIT_IMFTIT_001&scrId=&seqNo=&lang_mode=ko&obj_var_id=&itm_id=&conn_path=MT_RTITLE&path=%252FstatisticsList%252FstatisticsListIndex.do')
    
if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(multi_index)
