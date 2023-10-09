import os
from dotenv import find_dotenv, load_dotenv
from llama_cpp import Llama
from transformers import pipeline
import requests
import streamlit as st

load_dotenv(find_dotenv())
HUGGINGFACE_TOKEN = os.getenv("HUGGINGFACE_TOKEN")
LLAMA_LOCAL_PATH = os.getenv("LLAMA_LOCAL_PATH")
headers = {"Authorization": f"Bearer {HUGGINGFACE_TOKEN}"}

# img2text
def img2text(url):
    print("STEP 1: img2text")
    img_to_text = pipeline("image-to-text", model="Salesforce/blip-image-captioning-base")
    text = img_to_text(url)[0]["generated_text"]
    
    print(text)
    return text

# LLM
'''
def LLM(prompt):
    # llm = pipeline("text-generation", model="bigscience/bloom-560m")
    # text = llm(f"Create a story with 500 words with the following context: {prompt}")[0]['generated_text']

    API_URL = "https://api-inference.huggingface.co/models/gpt2"
    fullprompt = f"Create a story with 500 words with the following context: {prompt}"
    payload = {
        "inputs": fullprompt,
        "return_full_text": False
    }
    text = requests.post(API_URL, headers=headers, json=payload).data
 
    print(text)
    return text
'''

def LLM(prompt):
    print("STEP 2: text2story")
    LLM = Llama(model_path=LLAMA_LOCAL_PATH)

    full_prompt = f"Create a story with 200 words with the following context: {prompt}"
    output = LLM(full_prompt, max_tokens=0)
    
    print(output["choices"][0]["text"])
    return output["choices"][0]["text"]

# text2speech
def text2speech(text):
    print("STEP 3: story2speech")
    API_URL = "https://api-inference.huggingface.co/models/espnet/kan-bayashi_ljspeech_vits"
    payload = {
        "inputs": text
    }
    response = requests.post(API_URL, headers=headers, json=payload)
    with open('audio.flac', 'wb') as file:
        file.write(response.content)
        

scenario = img2text("app/image2.jpg")
story = LLM(scenario)
text2speech(story)

# def main():
#     st.set_page_config(page_title="img2audio story", page_icon="🎂")
#     st.header("Turn img into audio story")
    
#     uploaded_file = st.file_uploader("Choose an image...", type="jpg")
    
#     if uploaded_file is not None:
#         print(uploaded_file)
#         bytes_data = uploaded_file.getvalue()
#         with open(uploaded_file.name, "wb") as file:
#             file.write(bytes_data)
#         st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
#         scenario = img2text(uploaded_file.name)
#         story = LLM(scenario)
#         text2speech(story)
        
#         with st.expander("scenario"):
#             st.write(scenario)
#         with st.expander("story"):
#             st.write(story)
            
#         st.audio("audio.flac")
        
# if __name__ == '__main__':
#     main()