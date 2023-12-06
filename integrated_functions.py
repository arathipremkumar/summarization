import pandas as pd
import os
import openai
import requests
import time
import importlib

promptforqna=['Give me the medical diagnosis, past and present for the patient',
                'Give me the surgeries that the patient has undergone',
                'Find all the medications that the patient has been prescribed or they take',
                'What are the allergies that the patient has',
                 'What is family history of this patient',
                 'What is the social history of this patient']

promptforgpt=['Get all the current and past medical diagnosis from the below extracts, label the reponse as Past Medical Diagnosis',
                'Get all the surgeries from the below extracts, label it as Past Surgical History',
                'Get all the prescriber or taken medications from the below extracts, label it as Medications',
                'Get all the allergies of the patient from the below extracts, label it as Allergies',
                'Get all the Family history from the below extracts,label it as Family history ',
                'Get all the Social History fromt the below extracts, label it as Social history']

patientid=""

AI_API_KEY="acee3756d06a4c3993a7c378bb041829"
SEARCH_API_KEY="ET1LP48KFmyl8yzq6XUWUtmMZ7ojURUy2ZrzLerefsAzSeDiTKfG"

def searchdocs(prompt):


    openai.api_type = "azure"
    # Azure OpenAI on your own data is only supported by the 2023-08-01-preview API version
    openai.api_version = "2023-08-01-preview"

    # Azure OpenAI setup
    openai.api_base = "https://espoc.openai.azure.com/" # Add your endpoint here
    openai.api_key = AI_API_KEY # Add your OpenAI API key here
    deployment_id = "Summarizer-gpt-35-turbo-16k" # Add your deployment ID here

    # Azure AI Search setup
    search_endpoint = "https://searchaies.search.windows.net"; # Add your Azure AI Search endpoint here
    search_key = SEARCH_API_KEY; # Add your Azure AI Search admin key here
    search_index_name = patientid; # Add your Azure AI Search index name here

    def setup_byod(deployment_id: str) -> None:
        """Sets up the OpenAI Python SDK to use your own data for the chat endpoint.

        :param deployment_id: The deployment ID for the model to use with your own data.

        To remove this configuration, simply set openai.requestssession to None.
        """

        class BringYourOwnDataAdapter(requests.adapters.HTTPAdapter):

            def send(self, request, **kwargs):
                request.url = f"{openai.api_base}/openai/deployments/{deployment_id}/extensions/chat/completions?api-version={openai.api_version}"
                return super().send(request, **kwargs)

        session = requests.Session()

        # Mount a custom adapter which will use the extensions endpoint for any call using the given `deployment_id`
        session.mount(
            prefix=f"{openai.api_base}/openai/deployments/{deployment_id}",
            adapter=BringYourOwnDataAdapter()
        )

        openai.requestssession = session

    setup_byod(deployment_id)


    message_text = [{"role": "user", "content": prompt}]

    completion = openai.ChatCompletion.create(
        messages=message_text,
        deployment_id=deployment_id,
        dataSources=[  # camelCase is intentional, as this is the format the API expects
            {
                "type": "AzureCognitiveSearch",
                "parameters": {
                    "endpoint": search_endpoint,
                    "key": search_key,
                    "indexName": search_index_name,
                }
            }
        ]
    )

    return completion["choices"][0]["message"]["content"]


def summ(prompt,outputofaisearch):

  openai.api_type = "azure"
  openai.api_base = "https://espoc.openai.azure.com/"
  openai.api_version = "2023-07-01-preview"
  openai.api_key = AI_API_KEY
  # openai.requestssession = None

  message_text = [{"role":"system","content":prompt},{"role":"user","content":outputofaisearch}]

  completion = openai.ChatCompletion.create(
    engine="Summarizer-gpt-35-turbo-16k",
    messages = message_text,
    temperature=0.7,
    max_tokens=800,
    top_p=0.95,
    frequency_penalty=0,
    presence_penalty=0,
    stop=None
  )
  return completion["choices"][0]["message"]["content"]

def integrated(patientkey):

    df=pd.DataFrame()
    global patientid
    patientid=patientkey

    df['Search Prompts']=promptforqna
    df['Prompts to Summarize']=promptforgpt
    
    df['Search Results']=df['Search Prompts'].apply(searchdocs)
    # time.sleep(10)
    importlib.reload(openai) 
    df['Summary'] = df.apply(lambda row: summ(row['Prompts to Summarize'], row['Search Results']), axis=1)
    return df
