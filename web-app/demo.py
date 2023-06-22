import numpy as np
import pickle
import streamlit as st
from PIL import Image

loaded_model = pickle.load(open('stacking.sav' , 'rb'))
st.set_page_config(page_title = "PulseGuard")

def heart_attack_prediction(input_data):
    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
        return st.success('This person is not in risk of a heart attack 😃👍')
    else:
        return st.warning('This person is more likely to have heart attack, Please consult a doctor ASAP 👨‍⚕️')


def main():
    image = Image.open("web-app\logo.png")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.write(' ')
    with col2:
        st.image(image, use_column_width=True)
    with col3:
        st.write(' ')

    st.markdown("<h1 style='text-align: center; color: white;'>PulseGuard</h1>", unsafe_allow_html=True)    
    st.write("<h5 style='text-align: center; color: gray;'>Heart Attack Prediction Application</h1>", unsafe_allow_html=True)    

    age = st.slider('Age', 0,120, 25)
    sex = st.selectbox("Choose Your Gender:", ('Male', 'Female'))
    if sex ==  'Male':
        sex=1
    else: 
        sex=0

    cp = st.selectbox('Chest Pain type:', ('Typical angina' , "Atypical angina", "Non-anginal pain", "Asymptomatic"))
    if cp == 'Typical angina':
        cp = 0
    elif cp == 'Atypical angina':
        cp = 1
    elif cp == 'Non-anginal pain':
        cp = 2
    else:
        cp = 3

    trtbps = st.slider('Resting blood pressure (in mm Hg):', 0,500,0)
    chol = st.slider('Cholestoral in mg/dl fetched via BMI sensor:',0,500,0)
    fbs = st.selectbox('Fasting blood sugar is more than 120 mg/dl',('Yes','No'))
    if fbs == 'Yes':
        fbs = 1
    else: 
        fbs = 0
    
    rest_ecg = st.selectbox('Resting electrocardiographic results:',('Normal','Abnormality','Hypertrophy'))
    if rest_ecg == 'Normal':
        rest_ecg = 0
    elif rest_ecg == 'Abnormality':
        rest_ecg = 1
    else: 
        rest_ecg = 2
    thalach = st.slider('Maximum heart rate achieved.', 0,500,0)
    exng = st.selectbox('Exercise induced angina:',('Yes','No'))
    if exng == 'Yes':
        exng = 1
    else:
        exng = 0
    
    oldpeak = st.slider('ST depression induced by exercise relative to rest', 0,5,0)    
    slp = st.selectbox('slope of the peak exercise ST segment:',('Upsloping','Flat','Downsloping'))
    if slp == 'Upsloping':
        slp = 0
    elif slp == 'Flat':
        slp = 1
    else:
        slp = 2
    caa = st.selectbox('Number of major vessels (0-3) colored by flourosopy',("0","1","2","3"))
    if caa == '0':
        caa = 0
    elif caa == '1':
        caa = 1
    elif caa == '2':
        caa = 2
    else:
        caa = 3

    thall = st.selectbox('A blood disorder called thalassemia',('Fixed Defect (no blood flow in some part of the heart)', 'Normal blood flow','Reversable Defect (a blood flow is observed but it is not normal)'))
    if thall == 'Fixed Defect (no blood flow in some part of the heart)':
        thall = 1
    elif thall == 'Normal blood flow':
        thall = 2
    else:
        thall = 3

    # creating a button for Prediction
    if st.button('Heart attack Test Result'):
        diagnosis = heart_attack_prediction([age, sex, cp, trtbps, chol, fbs, rest_ecg, thalach, exng, oldpeak, slp, caa, thall])

    
if __name__ == '__main__':
    main()
    
    
  