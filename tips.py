# pylint: disable=E1101
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

st.set_page_config(page_title="Tips Dashboard 💰",page_icon='../images/tip.png',
                layout='wide',initial_sidebar_state='auto')

df=pd.read_csv('tips.csv')
# st.image('./images/Tips.jpg',
#          width=200, use_column_width='never', channels="RGB", output_format="auto")

##############################Side bar ###################################

# st.sidebar.markdown("<h1 style='text-align: center; font-size: 24px;'>Tips Dashboard 💸</h1>", unsafe_allow_html=True)
st.sidebar.title('Tips Dashboard 💸')
st.sidebar.image('./Images/tips.png',width=100)
st.sidebar.write('Explore tipping behavior with our Tips Dashboard! 📊 This educational tool leverages the Seaborn "Tips" dataset to educational purpose.')
st.sidebar.write('')
st.sidebar.markdown('Made by 💗 [Abdullah Moamen](https://www.linkedin.com/in/abdullah-moamen-b202701b4/)')
st.sidebar.write('')
st.sidebar.write('⛔ Filter Your Data:')
cat_filter=st.sidebar.selectbox('Categorical Filtering',['Sex','Smoker','Time','Day',None])
num_filter=st.sidebar.selectbox('Numerical Filtering',['Total_bill','Tip',None])
row_filter=st.sidebar.selectbox('Row Filter',['Sex','Smoker','Time','Day',None])
col_filter=st.sidebar.selectbox('Column Filter',['Sex','Smoker','Time','Day',None])

####################body###############################

#First row 
a1,a2,a3,a4=st.columns(4)
a1.metric('Max Total Bill',df['Total_bill'].max())
a2.metric('Max Tip',df['Tip'].max())
a3.metric('Min Total Bill',df['Total_bill'].min())
a4.metric('Min tip',df['Tip'].min())

#Second row 
st.write('Relation Between Total Bill And Tips')
fig = px.scatter(df,x='Total_bill',y='Tip',
                color=cat_filter,size=num_filter,
                facet_col=col_filter,facet_row=row_filter)
st.plotly_chart(fig,use_container_width=True)

#Third Row
c1,c2,c3=st.columns((4,3,3))

#Par_chart
with c1:
    st.text('Gender VS Total Bill')
    fig=px.bar(df,x='Sex',y='Total_bill',color=cat_filter)
    st.plotly_chart(fig,use_container_width=True)
    
#Pie_chart
with c2:
    st.text('Smoker || Non Smoker VS Tips')
    fig=px.pie(df,names='Smoker',values='Tip',color=cat_filter)
    st.plotly_chart(fig,use_container_width=True)
# Donut_chart
with c3:
    st.text('Gender VS Total Bill')
    fig=px.pie(df,names='Day',values='Tip',color=cat_filter,hole=0.4)
    st.plotly_chart(fig,use_container_width=True)
    

st.markdown('creates by 🖊️ [Abdullah Moamen](https://www.linkedin.com/in/abdullah-moamen-b202701b4/). All copy rights were reserved ©️')