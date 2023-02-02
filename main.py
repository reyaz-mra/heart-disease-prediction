import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, accuracy_score
from sklearn.utils import resample

st.sidebar.image("medcare.png")
st.image("https://www.kokilabenhospital.com/blog/wp-content/uploads/2022/05/Heart-disease-know-your-risk.jpg")
col1, col2, col3 = st.columns(3)
with col1:
    age = st.number_input("Age")
with col2:
    sex = 0
    option = st.selectbox(
        'Gender',
        ('Male', 'Female'))
    if option == 'Male':
        sex = 0
    if option == 'Female':
        sex = 1

with col3:
    cp = 0
    option = st.selectbox(
        'Chest Pain Type',
        ('Typical Angina', 'Atypical Angina','Non-Anginal Pain','Asymptomatic'))
    if option == 'Typical Angina':
        cp = 0
    if option == 'Atypical Angina':
        cp = 1
    if option == 'Non-Anginal Pain':
        cp = 2
    if option == 'Asymptomatic':
        cp = 3

col1, col2, col3 = st.columns(3)

with col1:
    trestbps = st.number_input("Resting Blood Pressure(in mm Hg)")
with col2:
    chol = st.number_input('Serum Cholestoral in mg/dl')
with col3:
    fbs=0
    option = st.selectbox(
        'Fasting Blood Sugar',
        ('True', 'False'))
    if option == 'True':
        fbs = 1
    if option == 'False':
        fbs = 0
col1, col2, col3 = st.columns(3)

with col1:
    restecg = 0
    option = st.selectbox(
        'Resting Electrocardiographic Results',
        ('Normal','Having ST-T','Hypertrophy')
    )
    if option == 'Normal':
        restecg = 0
    if option == 'Having ST-T':
        restecg = 1
    if option == 'Hypertrophy':
        restecg = 2

with col2:
    thalach = st.number_input("Maximum Heart Rate Achieved")

with col3:
    exang = 0
    option = st.selectbox(
        'Exercise Induced Angina',
        ('Yes','No')
    )
    if option == 'Yes':
        exang = 1
    if option == 'No':
        exang = 0

col1, col2, col3 = st.columns(3)

with col1:
    oldpeak = st.number_input("ST depression")

with col2:
    slope = 0
    option = st.selectbox(
        ' slope of the peak exercise ST segment',
        ('Upsloping','Flat','Downsloping')
    )
    if option == 'Upsloping':
        slope = 0
    if option == 'Flat':
        slope = 1
    if option == 'Downsloping':
        slope = 2

with col3:
    ca = st.number_input("number of major vessels (0-4)")

col1, col2, col3 = st.columns(3)

with col1:
    thal = 0
    option = st.selectbox(
        'Thalassemia Value',
        ('Fixed Defect','Normal Blood Flow','Reversible Defect')
    )
    if option == 'Fixed Defect':
        thal = 1
    if option == 'Normal Blood Flow':
        thal = 2
    if option == 'Reversible Defect':
        thal = 3


df = pd.read_csv("heart.csv")
x = df.drop(['target'], axis=1)
y = df['target']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=4)
KNNClassifier = KNeighborsClassifier(n_neighbors=3)
KNNClassifier.fit(x_train.values, y_train)


if st.button('Heart Disease Test Result'):
    heart_prediction = KNNClassifier.predict(
        [[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])

    if (heart_prediction[0] == 1):
        heart_diagnosis = 'The person is having heart disease'
        st.error(heart_diagnosis)
    else:
        heart_diagnosis = 'The person does not have any heart disease'
        st.success(heart_diagnosis)




