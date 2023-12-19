import streamlit as st
from openai import OpenAI
from PIL import Image

image = Image.open("lyzr-logo.png")
st.image(image, caption="", width=150)

def text_to_speech(text, model="tts-1-hd", voice="echo"):
    api_key = st.secrets["apikey"] # Replace with your Streamlit secrets path
    
    client = OpenAI(api_key=api_key)
    response = client.audio.speech.create(
        model=model,
        voice=voice,
        input=text,  
    )
    
    # Save the synthesized speech to a file named "tts_output.mp3"
    response.stream_to_file("tts_output.mp3")
    

# Title of the web app
st.title('Text to Speech Using OpenAI')

# Text input box for the user to enter a string
user_input = st.text_input("Enter the text you want to convert into Audio", value='Bring your Text to life using OpenAI TTS')

# Voice Style ['alloy', 'echo', 'fable', 'onyx', 'nova', 'shimmer']
voice = st.radio('Voice Style', ['alloy', 'echo', 'fable', 'onyx', 'nova', 'shimmer'])


# Voice Style ['alloy', 'echo', 'fable', 'onyx', 'nova', 'shimmer']
model = st.radio('Model', ["tts-1","tts-1-hd"])


# A button to submit the input
submit = st.button('Submit')

# If the user clicks the submit button, display the input string
if submit:
    text_to_speech(user_input, model, voice)
    st.write(f'You entered: {user_input}')
    st.subheader("Lyzr TTS output")
    st.audio("tts_output.mp3")
    st.write(f'Selected voice style: {voice}')
    st.write(f'Selected model: {model}')