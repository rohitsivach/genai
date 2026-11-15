# Streamlit क्या है?

# Streamlit एक Python framework है जिससे आप Data Science, Machine Learning और AI applications के लिए interactive web apps बहुत कम code में बना सकते हैं।

# अगर आपने Python में कोई ML model या AI chatbot बनाया है, तो Streamlit की मदद से उसे एक web application में बदल सकते हैं।

# आसान उदाहरण

# मान लीजिए आपने Python में एक Calculator बनाया।

# सिर्फ terminal में चलाने की बजाय, Streamlit से आप उसके लिए buttons, text boxes और web page बना सकते हैं।

# Python Script → Streamlit → Web App

# Streamlit क्यों Use करते हैं?
# Python से Web App बनाना आसान
# HTML, CSS, JavaScript की जरूरत नहीं (basic apps के लिए)
# Machine Learning models को deploy करना
# AI Chatbots बनाना
# Dashboards बनाना
# Data Visualization
# Streamlit कहाँ-कहाँ Use होता है?
# AI Chatbot
# Data Dashboard
# Machine Learning Model Demo
# Data Analysis Dashboard
# Image Classification App
# PDF Chatbot
# Generative AI Projects

#R:\Visual Studio\GenAI Course\Streamlit> streamlit run app.py ye cmd run kre

import streamlit as st

st.title("My First Streamlit App")

st.write("Hello Rohit!")
st.header("Welcome")


a = st.number_input("Enter First Number")
b = st.number_input("Enter Second Number")

if st.button("Add"):
    st.success(a + b)




st.title("My First Streamlit App")

st.write("Hello Rohit!")
st.header("Welcome")
if st.button("Click Me"):
    st.write("Button Clicked")




name = st.text_input("Enter Name")
st.write(name)

age = st.number_input("Enter Age")
city = st.selectbox(
    "Select City",
    ["Delhi", "Jaipur", "Mumbai"]
)

st.write(city)
file = st.file_uploader("Upload File")
if file is not None: 
    st.write("File Uploaded Successfully")
    st.write(file.name)
    st.write(file.type)
    st.write(file.size)