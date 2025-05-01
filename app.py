import streamlit as st
from streamlit_option_menu import option_menu
import joblib


diabetes_model = joblib.load('models/diabetes_model.sav','rb')
heart_model= joblib.load('models/heart_model.sav','rb')



with st.sidebar:
    
    selected=option_menu('Multiple Disease Prediction',['Diabetes Disease Prediction','Heart Disease Prediction'],default_index=0,icons=['droplet', 'heart-pulse'],styles={"nav-link-selected": {"background-color": "#00AB32", "color": "white"}})

if(selected=='Diabetes Disease Prediction'):
    st.title('Diabetes Disease Prediction')
    Pregnancies=st.text_input('enter pregnancy value')
    Glucose=st.text_input('enter glucose value')
    BloodPressure=st.text_input('enter blood pressure value')
    SkinThickness=st.text_input('enter skin thickness value')
    Insulin=st.text_input('enter insulin value')
    BMI_unit=st.text_input('enter bmi unit value')
    DiabetesPedigreeFunction=st.text_input('enter diabetes pedigree function value')
    Age=st.text_input('enter age value')

    res=""
    if st.button('predict'):
        prediction=diabetes_model.predict([[int(Pregnancies),int(Glucose),int(BloodPressure),int(SkinThickness),int(Insulin),float(BMI_unit),float(DiabetesPedigreeFunction),int(Age)]])
        if(prediction[0]==1):
            res="positive"
        else:
            res="negative"
    st.success(res)

if(selected=='Heart Disease Prediction'):
    st.title('Heart Disease Prediction')
    Age=st.text_input('enter age value')
    Sex=st.text_input('enter sex value')
    cp=st.text_input('enter cp value')
    trestbps=st.text_input('enter trestbps value')
    chol=st.text_input('enter chol value')
    fbs=st.text_input('enter fbs value')
    restecg=st.text_input('enter restecg value')
    thalach=st.text_input('enter thalach value')
    exang=st.text_input('enter exang value')
    oldpeak=st.text_input('enter oldpeak value')
    slope=st.text_input('enter slope value')
    ca=st.text_input('enter ca value')
    thal=st.text_input('enter thal value')

    res=""
    if st.button('predict'):
        prediction=heart_model.predict([[
            int(Age),
            int(Sex),
            int(cp),
            int(trestbps),
            int(chol),
            int(fbs),
            int(restecg),
            int(thalach),
            int(exang),
            float(oldpeak),
            int(slope),
            int(ca),
            int(thal)
        ]])
        if(prediction[0]==1):
            res="positive"
        else:
            res="negative"
    st.success(res)



