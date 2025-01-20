import streamlit as st
import pickle

# source .venv/bin/activate
# streamlit run app.py

model = pickle.load(open('model.pkl', 'rb'))

st.title('Spam ⚔️ Ham: Battle Royal')

message = st.text_input('Enter your message')

submit = st.button('Predict')

if submit:
    prediction = model.predict([message])
    if prediction[0] == 'spam':
        st.warning('Bloody Bastards! This message is SPAM!')
    else:
        st.success('Congrats! This message is legit!')
    st.balloons()