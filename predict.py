import numpy as np
import pickle
import streamlit as st


loaded_model = pickle.load(open('trained_model.sav' , 'rb'))


def heart_attack_prediction(input_data):

    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
        return 'The person is not in risk of a heart attack'
    else:
        return 'The person is more likely to have heart attack'


def main():

    st.title('Heart Attack Prediction')
    
    age = st.slider('Age', 0,120, 25)
    sex = st.slider('Sex 0=female, 1=male', 0, 1, 0)
    cp = st.slider('Chest Pain type chest pain type (0= typical angina , 1= atypical angina, 2= non-anginal pain, 3= asymptomatic).', 0,3,0)
    trtbps = st.slider('Resting blood pressure (in mm Hg)', 0,500,0)
    chol = st.slider('Cholestoral in mg/dl fetched via BMI sensor',0,500,0)
    fbs = st.slider('Fasting blood sugar > 120 mg/dl) (1 = true; 0 = false)',0,1,0)
    rest_ecg = st.slider('Resting electrocardiographic results (0= normal, 1= having ST-T wave abnormality, 2= showing probable or definite left ventricular hypertrophy by Estes',0,2,0)
    thalach = st.slider('Maximum heart rate achieved.', 0,500,0)
    exng = st.slider('Exercise induced angina (1 = yes; 0 = no)',0,1,0)
    oldpeak = st.slider('ST depression induced by exercise relative to rest', 0,5,0)    
    slp = st.slider('slope of the peak exercise ST segment (0: upsloping , 1: flat, 2: downsloping)',0,2,0)
    caa = st.slider('Number of major vessels (0-3) colored by flourosopy',0,3,0)
    thall = st.slider('0 = normal; 1 = fixed defect; 2 = reversable defect ',1,3,0)

    # code for heart attack Prediction
    diagnosis = ''
    
    # creating a button for Prediction
    if st.button('Heart attack Test Result'):
        diagnosis = heart_attack_prediction([age, sex, cp, trtbps, chol, fbs, rest_ecg, thalach, exng, oldpeak, slp, caa, thall])

    st.success(diagnosis)
    

if __name__ == '__main__':
    main()
    
    
  