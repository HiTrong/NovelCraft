# ====== Import Libraries ======
import PIL.Image
import streamlit as st
from API_handle import get_picture_response

# ====== Image Generation ======
def image_generate(url: str, prompt):
    img = get_picture_response(url, prompt, lambda: st.warning("Please check your API and content moderation. Something went wrong!"))
    if img is None:
        return PIL.Image.open("./img_app/error_image.png")
    return img

