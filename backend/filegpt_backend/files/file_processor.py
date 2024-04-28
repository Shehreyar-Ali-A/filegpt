

from PyPDF2 import PdfReader
from django.shortcuts import get_object_or_404
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS

from .embeddings import create_embeddings
from .models import UploadedFile
import os
from dotenv import load_dotenv
from pinecone import Pinecone
from PIL import Image
from pytesseract import image_to_string


load_dotenv()


pc = Pinecone(api_key=os.getenv('PINECONE_API_KEY'))


def create_chunks(text):

    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
      )
    chunks = text_splitter.split_text(text)
    return chunks


    

def process_file(file_id):
    file_obj = get_object_or_404(UploadedFile, pk=file_id)
    file_url = str(file_obj.file)

    #  if file exists then we break the file down into chunks make the embeddings and store them
    if file_url:
        if file_url.endswith(".pdf"):
            with open(f"./media/{file_url}", 'rb') as file:
                pdf_reader = PdfReader(file)
                text = ""
                for page in pdf_reader.pages:                
                    text += page.extract_text()

        elif file_url.endswith(".jpeg") or file_url.endswith(".jpg") or file_url.endswith(".png"):            
            text = image_to_string(Image.open(f"./media/{file_url}"))


    # create a new chat for the file that has just been processed

    chunks = create_chunks(text)
    print("\n\n CHUNKS: ", chunks,"\n\n")
    embeddings = create_embeddings(chunks)

    pinecone_index = pc.Index(name='filegpt')
    pinecone_index.upsert(
        vectors=[
            {'id':str(file_id), 'values':embeddings}
        ],
        namespace=file_url
    )

    

    # maybe delete the file from temp storage?
