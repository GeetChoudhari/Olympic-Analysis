import streamlit as st
import pandas as pd
from PIL import Image
from Summer_preprocess import summer
from Winter_preprocess import Winter
from home import home


st.set_page_config(
    page_title="Analysis of Olympics",
    page_icon="medal",
    layout="wide",
    initial_sidebar_state="auto",
)

user_menu = st.sidebar.selectbox(
    "Select The Season Of Olympics",
    ("Home", "Summer Olympics", "Winter Olympics"))

if user_menu == "Summer Olympics":
    summer()
elif user_menu == "Winter Olympics":
    Winter()
else:
    home()
