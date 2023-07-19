import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings, HuggingFaceInstructEmbeddings
from langchain.vectorstores import FAISS

# Receiving the PDFs and working
def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        # Creates pdf objects that has pages. Loop through the pages and added the texts
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

def get_text_chunks(text):
    # will seperate through by new lines,
    # chunk size means small portions will be most 1000 characters,
    # chunk_overlap means, when a chunk ends in a small range then the end of a chunk
    # could be in a middle of sentences for overcoming this we use overlap
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=200,
        chunk_overlap=5,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    return chunks

def get_vectorestore(text_chunks):
    # embeddings = OpenAIEmbeddings()
    embeddings = HuggingFaceInstructEmbeddings()
    # embedding_vectors = [embeddings.encode(text) for text in text_chunks]
    vectorestore = FAISS.from_texts(texts=text_chunks, embeddings=embeddings)
    return vectorestore

def main():
    load_dotenv()
    st.set_page_config("SOLVRZ", page_icon=":books:")
    st.header("SOLVR :books:")
    st.text_input("Ask a question about your documents : ")

    with st.sidebar:
        st.subheader("Your Documents")
        pdf_docs = st.file_uploader("Upload Your PDFs here and click on process", accept_multiple_files=True)
        if st.button("Process"):
            with st.spinner("I AM WORKING.."):
                # Sending the PDFS to the function
                #Getting the PDFs' Texts
                raw_text = get_pdf_text(pdf_docs)
                # st.write(raw_text)

#             Getting the text Chunks
                text_chunks = get_text_chunks(raw_text)
                # st.write(text_chunks)
#             Creating Vector Store
                vector_store = get_vectorestore(text_chunks)
                st.write(vector_store)

if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pychar