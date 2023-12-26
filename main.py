## Content Recommendation Engine

import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

## Function To get response from LLAma 2 model

def getLLamaresponse(input_text,no_words,content_type):

    ### LLama2 model
    llm=CTransformers(model='llama-2-7b-chat.ggmlv3.q8_0.bin',
                      model_type='llama',
                      config={'max_new_tokens':100,
                              'temperature':0.2})
    
    ## Prompt Template

    template="""
        Generate content for {content_type} for a topic {input_text}
        within {no_words} words.
            """
    
    prompt=PromptTemplate(input_variables=["content_type","input_text",'no_words'],
                          template=template)
    
    ## Generate the ressponse from the LLama 2 model
    response=llm(prompt.format(content_type=content_type,input_text=input_text,no_words=no_words))
    print(response)
    return response






st.set_page_config(page_title="Generate Content",
                    page_icon='🤖',
                    layout='centered',
                    initial_sidebar_state='collapsed')

st.header("Recommendation Engine 🤖")

input_text=st.text_input("Enter the Topic")

## creating to more columns for additonal 2 fields

col1,col2,col3=st.columns([4,5,3])

with col1:
    no_words=st.text_input('No of Words')
with col2:
    blog_style=st.selectbox('Create content for',
                            ('Scholars','Data Analysts','Common People','Bloggers','Business people'),index=0)
with col3:
    output_style=st.selectbox('Choose this style',('Paragraph','Bullet points','Only important keywords'),index=0)
content_type = blog_style    
submit=st.button("Generate")

## Final response
if submit:
    st.write(getLLamaresponse(input_text,no_words,content_type))