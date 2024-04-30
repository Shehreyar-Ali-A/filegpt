import os
from dotenv import load_dotenv
from pinecone import Pinecone
import openai
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_pinecone import PineconeVectorStore
from langchain.chains.question_answering import load_qa_chain
# from langchain_community.chat_models import ChatOpenAI
from langchain_community.callbacks import get_openai_callback

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
pc = Pinecone(api_key=os.getenv('PINECONE_API_KEY'))
pinecone_index_name=os.getenv('PINECONE_DB_INDEX')


def similarity_search(question, file_key):
    embeddings = OpenAIEmbeddings()
    vectorstore = PineconeVectorStore(
        index_name=pinecone_index_name,
        embedding=embeddings,
        namespace=file_key
    )
    response = vectorstore.similarity_search(query=question)
    return response


def process_question(question, file_key):

    context = f"""
AI assistant is a brand new, powerful, human-like artificial intelligence.
      The traits of AI include expert knowledge, helpfulness, cleverness, and articulateness.
      AI is a well-behaved and well-mannered individual.
      AI is always friendly, kind, and inspiring, and he is eager to provide vivid and thoughtful responses to the user.
      AI has the sum of all knowledge in their brain, and is able to accurately answer nearly any question about any topic in conversation.
      AI assistant is a big fan of Pinecone and Vercel.
      START CONTEXT BLOCK
      ${question}
      END OF CONTEXT BLOCK
      AI assistant will take into account any CONTEXT BLOCK that is provided in a conversation.
      If the context does not provide the answer to question, the AI assistant will say, "I'm sorry, but I don't know the answer to that question".
      AI assistant will not apologize for previous responses, but instead will indicated new information was gained.
      AI assistant will not invent anything that is not drawn directly from the context.
      AI assistant will not show the social security number
        """


    docs = similarity_search(question, file_key)

    llm = ChatOpenAI()
    chain = load_qa_chain(llm, chain_type="stuff")
    with get_openai_callback() as cb:
        response = chain.run(input_documents=docs, question=context)
        print(cb)
    
    return response

