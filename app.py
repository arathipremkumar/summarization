from typing import Dict
import streamlit as st
import os
import warnings
warnings.filterwarnings("ignore")
from time import sleep
import random
from integrated_functions import integrated
@st.cache_data



def highlight_cells(val):
    return f"height: {100}px"
#function to display summary
def text_summary(text_input):
    df=integrated(text_input)
    st.dataframe(df)
    st.info("summary will be displayed here!")
#function for QnA
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

#UI

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
            text_summary(text_input)
    with tab2:
        question = st.selectbox(
            'What would you like to know about the patient?',
            (" ",'Medical history', 'Surgical history', 'Medication', 'Family history', 'Social history', 'Allergies', 'General related to physical')
            )
        answer(question)




    # with st.columns(3)[1]:
    #     st.image(resized_img)

first()









