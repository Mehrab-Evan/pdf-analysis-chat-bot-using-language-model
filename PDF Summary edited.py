# pip install pycryptodome too
# with open('env_vars.json', 'r') as f:
#    env_vars = json.load(f)
# openai.api_key = env_vars["OPENAI_API_KEY"]
import os
import openai
import tiktoken
import gradio as gr
from langchain import OpenAI, PromptTemplate
from langchain.chains.summarize import load_summarize_chain
from langchain.document_loaders import PyPDFLoader

OPENAI_API_KEY = "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"

# https://github.com/openai/openai-cookbook/blob/main/examples/How_to_count_tokens_with_tiktoken.ipynb
import tiktoken


# def num_tokens_from_string(string: str, encoding_name: str) -> int:
#     """Returns the number of tokens in a text string."""
#     encoding = tiktoken.get_encoding(encoding_name)
#     num_tokens = len(encoding.encode(string))
#     return num_tokens

# import gradio as gr
# from langchain import OpenAI, PromptTemplate
# from langchain.chains.summarize import load_summarize_chain
# from langchain.document_loaders import PyPDFLoader
llm = OpenAI(openai_api_key=OPENAI_API_KEY,temperature=0)

# llm = OpenAI(temperature=0)

# PyPDFLoader??

def summarize_pdf(pdf_file_path):
    loader = PyPDFLoader(pdf_file_path)
    docs = loader.load_and_split()
    chain = load_summarize_chain(llm, chain_type="map_reduce")
    summary = chain.run(docs)
    return summary

# num_tokens_from_string("tiktoken is great!", "cl100k_base")
summarize = summarize_pdf("storybook1.pdf")
print(summarize)

# just to show you how it works
# loader = PyPDFLoader('/content/OA_Paper_2023_04_15.pdf')
# doc=loader.load_and_split()
# print(len(doc))
# doc[0]
