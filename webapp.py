import streamlit as st
import pyttsx3
import io

engine = pyttsx3.init()

st.title('Text to Audio App')

# Text Input
text_input = st.text_area("Enter Text to be converted to Audio 👇"
                  )

# Check if a file was uploaded
if text_input:
    # Display the contents of the file
    st.text(text_input)
    
    engine.save_to_file(text_input, 'output.mp3')
    engine.runAndWait()
    engine.stop()
    
    with open('output.mp3', "rb") as file:
        audio_bytes = file.read()
    
    # Display a download button for the .mp3 file
    st.download_button(label="Download .mp3", data=audio_bytes, file_name="audio_file.mp3")
   
    

