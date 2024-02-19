import os
from langchain_google_genai import ChatGoogleGenerativeAI
import google.generativeai as genai
from langchain.chains import LLMChain
from dotenv import load_dotenv
load_dotenv()
from local_prompts.coustom_promps import set_costom_prompt
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
from logs import logger

def load_llm():
    llm = ChatGoogleGenerativeAI(model="gemini-pro",
                                 temperature=0.7)
    return llm

def html_generation(layout):
    prompt = set_costom_prompt()
    llm = load_llm()
    chain = LLMChain(prompt=prompt, llm=llm)
    output = chain.run(layout=layout)
    logger.info(f'--------------------\n {output}\n----------------------')
    return output