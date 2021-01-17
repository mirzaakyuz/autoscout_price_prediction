import streamlit as st
import pickle
import pandas as pd
st.title('Car Price Prediction')
html_temp = """
<div style="background-color:tomato;padding:10px">
<h2 style="color:white;text-align:center;">Streamlit ML App </h2>
</div>"""

st.markdown(html_temp,unsafe_allow_html=True)
model = pickle.load(open("xgb_model.pkl", "rb"))
age=st.selectbox("What is the age of your car?", (1,2,3))
hp=st.slider("What is the hp of your car?", 60, 200, step=5)

km=st.slider("What is the km of your car", 0,100000, step=500)
car_model=st.selectbox("Select model of your car", ('A1', 'A2', 'A3','Astra','Clio','Corsa','Espace','Insignia'))

my_dict = {
    "age": age,
    "hp": hp,
    "km": km,
    "model": car_model
}
df = pd.DataFrame.from_dict([my_dict])
columns=['age',
 'hp',
 'km',
 'model_A1',
 'model_A2',
 'model_A3',
 'model_Astra',
 'model_Clio',
 'model_Corsa',
 'model_Espace',
 'model_Insignia']
df = pd.get_dummies(df).reindex(columns=columns, fill_value=0)
#st.table(df)
prediction = model.predict(df)
st.success("The estimated price of your car is €{}. ".format(int(prediction[0])))