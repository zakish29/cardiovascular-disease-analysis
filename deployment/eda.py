import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image
import json


with open('list_cat_cols.txt', 'r') as file_1:
    list_cat_cols = json.load(file_1)

with open('list_num_cols.txt', 'r') as file_2:
    list_num_cols = json.load(file_2)

st.set_page_config(
    page_title='Heart Disease',
    layout= 'wide',
    initial_sidebar_state= 'expanded'
)


# Create Run Function
def run():
    # Membuat Title
    st.title('Heart Disease Prediction')

    # Subheader
    st.subheader('EDA for death caused by heart disease')

    # Menambahkan gambar
    image = Image.open('national-cancer-institute-701-FJcjLAQ-unsplash.jpg')
    st.image(image)

    # Menambahkan deskripsi
    st.write('## Introduction')
    st.write('Cardiovascular disease (CVD) is a group of conditions that affect the heart and blood vessels. It is one of the leading causes of death worldwide and a significant burden on global health systems. CVD includes coronary artery disease, heart failure, stroke, and other conditions that damage the heart and blood vessels. Risk factors for CVD include high blood pressure, high cholesterol, diabetes, smoking, obesity, and physical inactivity. Due to changes in lifestyle and diet, CVD has become a critical issue to tackle in the modern world. Preventing and managing CVD requires early detection and intervention, making accurate prediction of CVD outcomes a crucial area of research.')

    # Membuat garis lurus
    st.markdown('-'*42)

    st.write('## Table')
    # Show DF
    df = pd.read_csv('h8dsft_P1G3_zaki.csv')
    df['sex'] = df['sex'].apply(lambda x: 'Male' if x == 1 else 'Female')
    

    # Change numerical value in categorical column to Yes if 1 and No for 0
    def replace_values(df):
        for index, row in df.iterrows():
            for column in df.columns:
                if row[column] == 1:
                    df.at[index, column] = "Yes"
                elif row[column] == 0:
                    df.at[index, column] = "No"
        return df

    df = replace_values(df).reset_index()
    df = df.drop('index', axis=1)
    st.dataframe(df)

    st.write('## Heart Disease Factor')
    # create df only for death_event == 1
    df_died = df[df['DEATH_EVENT'] == 'Yes']
    category = st.selectbox('Choose Factors: ', (list_cat_cols))
    death_perc_anaemia = df_died[category].value_counts(normalize=True)
    fig = px.pie(names=death_perc_anaemia.index, values=death_perc_anaemia.values, hole=.4)
    st.plotly_chart(fig)

    if category == 'anaemia':
        st.write('Anaemia is a medical condition characterized by a low red blood cell count or a low hemoglobin level. In the dataset analyzed, 47.9% of patients with anaemia died due to CVD. This suggests that anaemia may be a significant risk factor for CVD-related deaths. One possible explanation for this is that anaemia reduces the amount of oxygen that reaches the tissues, which can lead to damage and inflammation. This inflammation can then contribute to the development of CVDs.')
    elif category == 'diabetes':
        st.write('Diabetes is a medical condition characterized by high blood sugar levels. In the dataset analyzed, 41.7% of patients with diabetes died due to CVD. This suggests that diabetes is also a significant risk factor for CVD-related deaths. One possible explanation for this is that diabetes can cause damage to the blood vessels, which can then lead to the development of CVDs.')
    elif category == 'high_blood_pressure':
        st.write('Hypertension is a medical condition characterized by high blood pressure. In the dataset analyzed, 40.6% of patients with hypertension died due to CVD. This suggests that hypertension is also a significant risk factor for CVD-related deaths. One possible explanation for this is that high blood pressure can cause damage to the blood vessels and increase the workload on the heart, which can then lead to the development of CVDs.')
    elif category == 'sex':
        st.write('In the dataset analyzed, 64.6% of male patients died due to CVD. This suggests that gender is a significant risk factor for CVD-related deaths. One possible explanation for this is that males tend to have higher levels of testosterone, which can contribute to the development of CVDs. Additionally, males may engage in riskier behaviors such as smoking and excessive alcohol consumption, which can further increase the risk of CVDs.')
    elif category == 'smoking':
        st.write('In the dataset analyzed, 31.3% of smokers died due to CVD. This suggests that smoking is also a significant risk factor for CVD-related deaths. One possible explanation for this is that smoking can cause damage to the blood vessels, increase blood pressure, and reduce the amount of oxygen that reaches the tissues, which can then lead to the development of CVDs.')

    # Membuat Plotly Plot
    st.write('## Distribution Of Factor')
    x = st.selectbox('Choose Category: ', (list_cat_cols))
    y = st.selectbox('Choose Factors: ', (list_num_cols))
    fig = px.scatter(df, x=x,y= y, color='DEATH_EVENT')
    st.plotly_chart(fig)

# calling function
if __name__ == '__main__':
   run()