
import streamlit as st
import textwrap
import google.generativeai as genai
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
import os

key = "key here"

pdf_path = 'bio.pdf' 

def generate_rag_prompt(query, context):
    escaped = context.replace("'", "").replace('"', "").replace("\n", " ")
    prompt = f"""
            You are a knowledgeable biologist and an excellent educator who explains 
            biology concepts in simple and relatable terms for non-technical learners. Carefully 
            read the question below and provide a clear, step-by-step explanation of the solution. 
            Define any scientific terms, explain biological processes involved, and ensure the answer 
            is accurate and easy to understand. If assumptions are needed, state them clearly and justify 
            their relevance."

            Structure your response as follows:
            1. Provide a clear **Header** summarizing the main topic.
            2. Include the **Main Point** in **bold**.
            3. Follow up with an explanation or additional details.

    Question: '{query}'
    CONTEXT: '{context}'
    """
    return prompt

def get_relevant_context_from_db(query):
    context = ""
    embedding_function = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2", model_kwargs={'device': 'cpu'}
    )
    vector_db = Chroma(persist_directory='./chroma_db', embedding_function=embedding_function)
    search_results = vector_db.similarity_search(query, k=4)  # Number of results to fetch
    for result in search_results:
        context += result.page_content + "\n"
    return context

# Function to wrap text to make it more readable
def wrap_text(text, width=111):
    wrapper = textwrap.TextWrapper(width=width)
    wrapped_text = wrapper.fill(text)
    return wrapped_text

# Function to generate the answer using the prompt
def generate_answer(prompt):
    genai.configure(api_key=key)
    model = genai.GenerativeModel(model_name='gemini-1.5-flash')
    answer = model.generate_content(prompt)
    return answer.text

# Streamlit Interface
st.set_page_config(page_title="Educator Bot", page_icon=":robot:", layout="wide")

# Add some styling for the header
st.markdown("""
    <style>
    .header {
        font-size: 30px;
        color: #4CAF50;
        font-weight: bold;
    }
    .subheader {
        font-size: 20px;
        color: #5A5A5A;
    }
    .output-container {
        background-color: #f4f4f9;
        border-radius: 8px;
        padding: 15px;
        margin-top: 20px;
    }
    .output-button {
        background-color: #4CAF50;
        color: white;
        padding: 10px 20px;
        border-radius: 5px;
        cursor: pointer;
    }
    </style>
""", unsafe_allow_html=True)

# Title and Instructions
st.markdown('<div class="header">Educator Bot</div>', unsafe_allow_html=True)
st.markdown('<div class="subheader">Ask any question, and get insightful answers!</div>', unsafe_allow_html=True)

# Process the PDF automatically
if os.path.exists(pdf_path):
    st.write("Processing PDF file from:", pdf_path)
    loaders = [PyPDFLoader(pdf_path)]  # Loading the PDF directly
    docs = []
    for loader in loaders:
        docs.extend(loader.load())
    
    # Split the documents for better context retrieval
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    docs = text_splitter.split_documents(docs)

    # Create the embedding function and vector store
    embedding_function = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2", model_kwargs={'device': 'cpu'}
    )
    vectorstore = Chroma.from_documents(docs, embedding_function, persist_directory="./chroma_db")
    st.write(f"Vector store now contains {vectorstore._collection.count()} documents.")
else:
    st.error(f"PDF file not found at {pdf_path}. Please check the file path.")

# Query input field
query = st.text_input("Enter your query:")

# Output Button to generate and display the answer
if query:
    if st.button("Get Answer", key="generate_answer"):
        context = get_relevant_context_from_db(query)
        prompt = generate_rag_prompt(query=query, context=context)
        answer = generate_answer(prompt=prompt)

        # Display the result in a styled output section
        st.markdown('<div class="output-container">', unsafe_allow_html=True)
        st.markdown("### **Response**")
        st.write(answer)
        st.markdown('</div>', unsafe_allow_html=True)
