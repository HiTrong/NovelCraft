# ====== Import Libraries ======
import streamlit as st
from streamlit_option_menu import option_menu
from my_streamlit_pages import HomePage, LightNovelGenerator, TermsOfUse

# ====== Page Settings ====== 
st.set_page_config(
    page_title="NovelCraft",  
    page_icon=":sparkles:",  
    layout="centered", 
    initial_sidebar_state="auto" 
)

# ====== Sidebar ======
with st.sidebar:
    gemini_api = st.text_input("Gemini API:", type="password")
    img_generator_url = st.text_input("Image Generator URL:", type="password") 
    
    selected = option_menu("Menu",["Home Page","Light Novel Generator","Terms of use"],
                           icons=['house','book','flag'], menu_icon="cast", default_index=0,
                           styles={
                                "container": {"font-family": "Monospace"},
                                "icon": {"color":"#71738d"}, 
                                "nav-link": {"--hover-color": "#d2cdfa","font-family": "Monospace"},
                                "nav-link-selected": {"font-family": "Monospace","background-color": "#6694ed"},
                            }
                           )
    
    language_support = st.radio(label="Language Support", options=["Vietnamese", "English"] )

# ====== Pages ======    
if selected == "Home Page":
    HomePage(language_support)
elif selected == "Light Novel Generator":
    LightNovelGenerator(gemini_api, img_generator_url, language_support)
else:
    TermsOfUse(language_support)