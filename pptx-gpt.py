#Demogpt prompt: Create a system that is capable of generating a PowerPoint presentation as a .pptx file from a text description of the topic.

# Step-1 Write all the import statements from the Draft Code.
import streamlit as st
from langchain import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (ChatPromptTemplate,
                                    HumanMessagePromptTemplate,
                                    SystemMessagePromptTemplate)
from langchain.document_loaders import *
from langchain.chains.summarize import load_summarize_chain
import tempfile
from langchain.docstore.document import Document

# Step-2 Write all the function definitions
def presentationContentGenerator(description):
    chat = ChatOpenAI(
        model="gpt-3.5-turbo-16k",
        temperature=0.7
    )
    system_template = """You are an assistant designed to generate content for a PowerPoint presentation based on the given text description: '{description}'."""
    system_message_prompt = SystemMessagePromptTemplate.from_template(system_template)
    human_template = """Based on the description: '{description}', please generate the content for the PowerPoint presentation."""
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
    chat_prompt = ChatPromptTemplate.from_messages(
        [system_message_prompt, human_message_prompt]
    )

    chain = LLMChain(llm=chat, prompt=chat_prompt)
    result = chain.run(description=description)
    return result # returns string   

def display_content(content):
    if content != "":
        st.markdown(f"**Generated Content:** {content}")
    else:
        st.markdown("No content generated yet.")

# Step-3 Get input from the user
st.title('PPTX-GPT')
description = st.text_area("Enter the text description of the topic here")

# Step-4 Put a submit button with an appropriate title
if st.button('Generate Presentation Content'):
    # Step-5 Call functions only if all user inputs are taken and the button is clicked.
    if description:
        content = presentationContentGenerator(description)
        display_content(content)
    else:
        st.markdown("Please enter a description.")