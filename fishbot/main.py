import streamlit as st
import google.generativeai as genai
from IPython.display import Markdown, clear_output, display
import time


st.title("FishBot X :rainbow[Gemini]🐠✨")
st.subheader("How can I help you?")


# Koneksi API Gemini
API_KEY = st.secrets["API_GEMINI"]["API_KEY_GEMINI"]

#Jawban Dari AI Gemini
def JawabanAI():
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel(model_name='gemini-1.0-pro')
    response = model.generate_content(prompt, stream=True)
    buffer = []
    for chunk in response:
        for part in chunk.parts:
            buffer.append(part.text)
        clear_output()
        display(Markdown(''.join(buffer)))

    for word in response.text:
        yield word
        time.sleep(0.02)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])



if prompt := st.chat_input("Enter a prompt for fishbot"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        stream = JawabanAI()
        response = st.write_stream(stream)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
