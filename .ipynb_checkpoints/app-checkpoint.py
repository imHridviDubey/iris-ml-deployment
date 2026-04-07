
import streamlit as st
import numpy as np
import pickle

#LOAD MODEL
model = pickle.load(open(r"C:\Users\Hridvi Dubey\IRISMLPROJECT\iris_model.pkl", "rb"))

#TITLE
st.title("IRIS FLOWER PREDICTION APP")

st.write("Enter flower measurements to predict species:")

#INPUT

sepal_length=st.number_input("Sepal Length",min_value=0.0,max_value=8.0)
sepal_width=st.number_input("Sepal Width",min_value=0.0,max_value=8.0)
petal_length=st.number_input("Petal Length",min_value=0.0,max_value=8.0)
petal_width=st.number_input("Petal Width",min_value=0.0,max_value=8.0)

#Prediction Button

if st.button("Predict"):
    data=np.array([[sepal_length,sepal_width,petal_length,petal_width]])
    prediction=model.predict(data)
    #Mapping
    if prediction[0]==0:
        result="Setosa"
    elif prediction[0]==1:
        result="Versicolor"
    else:
        result="Virginica"
    st.success(f"Predicted flower: {result}")








