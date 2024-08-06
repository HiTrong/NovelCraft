# ====== Import Libraries ======
import pathlib
import textwrap
import google.generativeai as genai
from datetime import datetime
import time
import streamlit as st
import os
import requests
import PIL.Image

# ====== Useful Functions ======
def get_time_stamp():
    now = datetime.now()
    timestamp = now.strftime('%Y%m%d%H%M%S')
    return timestamp

# ====== Gemini API ======
def get_gemini_model(api_key: str):
    genai.configure(api_key=api_key)
    return genai.GenerativeModel('gemini-1.5-pro')

def get_gemini_response(api_key: str, prompt, error_func):
    try_again = 5
    i=0
    while i<=try_again:
        try:
            model = get_gemini_model(api_key)
            response = model.generate_content(prompt)
            return response.text.replace('•', '  *')
        except Exception as e:
            print(e)
        i+=1
        st.write("Unable to connect...")
        time.sleep(2)
    error_func()
    return None
    
# ====== Diffusion Custom API ======  
def get_picture_response(url: str, prompt:str, error_func):
    try:
        payload = {"prompt": prompt}
        response = requests.post(url, json=payload)
        os.makedirs("./img_temp/",exist_ok=True)
        image_path ='./img_temp/' + get_time_stamp() + ".png"
        with open(image_path, 'wb') as f:
            f.write(response.content)
        img = PIL.Image.open(image_path)
        return img
    except:
        error_func()
        return None
        
        