import torch
from transformers import pipeline
import PyPDF2

def extract_text_from_pdf(file_path):
    text = ""
    with open(file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

def chat_with_pdf(pdf_path, question):
    # Load the question answering pipeline
    tqa = pipeline(task="question-answering", model="distilbert-base-cased-distilled-squad")

    # Extract text from the PDF
    pdf_text = extract_text_from_pdf(pdf_path)

    # Chat with the PDF by asking the question
    result = tqa(question=question, context=pdf_text)

    # Print the answer
    print("Question:", question)
    print("Answer:", result["answer"])

if __name__ == "__main__":
    pdf_path = "MD. Mehrab Hossain Chowdhury.pdf"
    question = "How many names are mentioned here?"
    chat_with_pdf(pdf_path, question)
