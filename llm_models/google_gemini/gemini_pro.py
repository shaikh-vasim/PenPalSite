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

# import torch
# from langchain_community.llms.ctransformers import CTransformers


# # Clear CUDA cache and check GPU availability
# torch.cuda.empty_cache()
# logger.info(f"---------isGPU-----------{torch.cuda.is_available()}")
# checkpoint = "./LaMini-T5-738M"
# cuda_available = torch.cuda.is_available()
# device = torch.device('cuda' if cuda_available else 'cpu')


# def load_llm():
#     """Load the Language Model.

#     Returns:
#         CTransformers: Loaded language model.
#     """
#     llm = CTransformers(
#         model="llama-2-7b-chat.ggmlv3.q8_0.bin",
#         model_type='llama',
#         max_new_tokens=10000,
#         temperature=0.5,
#     )
#     return llm

def html_generation(layout):
    prompt = set_costom_prompt()
    llm = load_llm()
    chain = LLMChain(prompt=prompt, llm=llm)
    output = chain.run(layout=layout)
    logger.info(f'--------------------\n {output}\n----------------------')
    return output