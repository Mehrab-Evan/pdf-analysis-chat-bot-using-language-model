import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader

# Receiving the PDFs and working
def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        # Creates pdf objects that has pages. Loop through the pages and added the texts
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

def main():
    load_dotenv()
    st.set_page_config("SOLVR", page_icon=":books:")
    st.header("SOLVR :books:")
    st.text_input("Ask a question about your documents : ")

    with st.sidebar:
        st.subheader("Your Documents")
        pdf_docs = st.file_uploader("Upload Your PDFs here and click on process", accept_multiple_files=True)
        if st.button("Process"):
            with st.spinner("I AM WORKING.."):
                # Sending the PDFS to the function
                raw_text = get_pdf_text(pdf_docs)
                st.write(raw_text)
#             Getting the PDFs' Texts
#             Getting the text Chunks
#             Creating Vector Store

if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pychar