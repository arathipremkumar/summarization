from typing import Dict
import streamlit as st
from PIL import Image
import tensorflow as tf
import numpy as np
import os

from keras.preprocessing import image
import warnings
from st_aggrid import AgGrid, GridOptionsBuilder
warnings.filterwarnings("ignore")
from keras.models import load_model
import cv2
from time import sleep
import tensorflow_addons as tfa
import pandas as pd
from stqdm import stqdm
from st_aggrid import AgGrid
stqdm.pandas()
st.markdown("""

""", unsafe_allow_html=True)

import random

pid = []



@st.cache_data




def get_static_store() -> Dict:
    """This dictionary is initialized once and can be used to store the files uploaded"""
    return {}

def color_low_confidence(val):
    """
    Takes a scalar and returns a string with
    the css property `'background-color: red'` for
    values that match 'low confidence', and an
    empty string otherwise.
    """
    color = 'red' if val == 'low confidence' else ''
    return f'background-color: {color}'

def highlight_cells(val):
    return f"height: {100}px"

def text_summary():
    st.info("summary will be displayed here!")

def answer(question):
    if question == 'Medical history':
        st.info("Prints Medical history of the patient")
    elif question == 'Surgical history':
        st.info("Prints Surgical history of the patient")
    elif question == 'Family history':
        st.info("Prints Family history of the patient")
    elif question == 'Social history':
        st.info("Prints Social history of the patient")
    elif question == 'Medication':
        st.info("Prints  Medication of the patient")
    elif question == 'Allergies':
        st.info("Prints Allergies of the patient")
    elif question == 'General related to physical':
        st.info("Prints General related to physical of the patient")
    else:
        st.info("")








    # Define the height of each row in pixels

    # Use st.beta_columns to create two columns
    # Set the height of the rows in the left column using CSS styling





def first():

    st.markdown("<h3 style='text-align: center; color: green;'> Comprehensive Clinical Notes Summarization</h1>", unsafe_allow_html=True)

    st.sidebar.markdown("## Patient Information")
    with st.sidebar:
        text_input = st.text_input(
            "Enter Patient EPIC Id 👇"
        )

        # st.info('This is a purely informational message')
        if text_input:
            st.info("Patient Name: XXXNAMEXXX")
            st.info("DOB: XXXDOBXXX")
            st.info("Gender: Female/Male")
    tab1, tab2 = st.tabs(["Text Summary", "🗃 QnA"])

    with tab1:
        if st.button('Generate Summary'):
            text_summary()
    with tab2:
        question = st.selectbox(
            'What would you like to know about the patient?',
            (" ",'Medical history', 'Surgical history', 'Medication', 'Family history', 'Social history', 'Allergies', 'General related to physical')
            )
        answer(question)




    # with st.columns(3)[1]:
    #     st.image(resized_img)





    # if st.button('Submit'):
        # predict(result)

    uploaded_images = []
    button_states = []

    # Add a file uploader widget to allow the user to upload images

    # If an image is uploaded, load and preprocess it, and add it to the list of uploaded images and button states

first()









