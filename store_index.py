from src.helper import load_pdf_files,filter_to_minimal_docs,text_split,download_embeddings
from langchain_pinecone.vectorstores import Pinecone, PineconeVectorStore
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from pinecone import Pinecone
from pinecone import ServerlessSpec
load_dotenv()

PINECONE_API_KEY=os.getenv("PINECONE_API_KEY")
os.environ["PINECONE_API_KEY"]=PINECONE_API_KEY

chat_model = ChatGroq(
    model="llama-3.3-70b-versatile",  
    api_key=os.getenv("GROQ_API_KEY")
)

extracted_data=load_pdf_files(data='data/')
filter_data=filter_to_minimal_docs(extracted_data)
texts_chunks=text_split(filter_data)

embeddings=download_embeddings()

pinecone_api_key = PINECONE_API_KEY
pc=Pinecone(api_key=pinecone_api_key)


index_name="medical-chatbot"
if not pc.has_index(index_name):
    pc.create_index(
        name=index_name,
        dimension=384, #dimension of the embedding m
        metric="cosine",
        spec=ServerlessSpec(cloud="aws",region="us-east-1")
    )

index=pc.Index(index_name)


docsearch=PineconeVectorStore.from_documents(
    documents= texts_chunks ,
    embedding=embeddings,
    index_name=index_name
)