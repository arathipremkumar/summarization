from typing import Dict
import streamlit as st
import os
import warnings
warnings.filterwarnings("ignore")
from time import sleep
import random
from integrated_functions import integrated
import base64
from io import BytesIO
# import fitz
import PyPDF2


from azure.storage.blob import BlobServiceClient
@st.cache_data



def highlight_cells(val):
    return f"height: {100}px"
#function to display summary
def text_summary(text_input):
    df=integrated(text_input)
    for value in df['Summary']:
        st.markdown(value)
    # output='\n'.join(df['Summary'].astype(str))
    # st.markdown(output)
    # st.info("summary will be displayed here!")
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
            "Enter Patient EPIC Id "
        )

        # st.info('This is a purely informational message')
        if text_input:
            st.info("Patient Name: XXXNAMEXXX")
            st.info("DOB: XXXDOBXXX")
            st.info("Gender: Female/Male")
    tab1, tab2 = st.tabs(["Text Summary", "🗃 QnA"])

    with tab1:
        col1, col2= st.columns(2)
        with col1:
            if st.button('Generate Summary'):
                text_summary(text_input)

        with col2:
    
    
            connection_string = "DefaultEndpointsProtocol=https;AccountName=storageespoc;AccountKey=j0jDh4ShEGg5EPs3UXWhp+58VEcktkjakoHcjzMae9HKMl4F+FXJVyns1M4QmjpJYmiJpWryoFuT+AStGGKl3g==;EndpointSuffix=core.windows.net"
            blob_name = "patient004.pdf"
            blob_service_client = BlobServiceClient.from_connection_string(connection_string)
            blob_client = blob_service_client.get_blob_client(container="fileupload-patient004", blob=blob_name)
            
    
            
            # Download the PDF file as bytes
            pdf_bytes = blob_client.download_blob().content_as_bytes()
            
            pdf_bytesio = BytesIO(pdf_bytes)
            pdf_reader = PyPDF2.PdfFileReader(pdf_bytesio)
            Extract the content
            content = ""
            for page in range(pdf_reader.getNumPages()):
                content += pdf_reader.getPage(page).extractText()
            # Display the content
            st.write(content)
    
            # pdf_display = (
            # f'<iframe src="data:application/pdf;base64,{pdf_bytesio}" '
            # 'width="800" height="1000" type="application/pdf"></iframe>'
            # )
            # st.markdown(pdf_display, unsafe_allow_html=True)
    with tab2:
        question = st.selectbox(
            'What would you like to know about the patient?',
            (" ",'Medical history', 'Surgical history', 'Medication', 'Family history', 'Social history', 'Allergies', 'General related to physical')
            )
        answer(question)




    # with st.columns(3)[1]:
    #     st.image(resized_img)

first()









