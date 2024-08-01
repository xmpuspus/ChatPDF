import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferWindowMemory
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from PyPDF2 import PdfReader
import tempfile

# Prompt template
prompt = PromptTemplate(
    input_variables=["chat_history", "question"],
    template="""You are a very kind and friendly AI assistant. You are
    currently having a conversation with a human. Answer the questions
    in a kind and friendly tone but in a professional manner. 
    
    chat_history: {chat_history},
    Human: {question}
    AI:"""
)

# Streamlit page configuration
st.set_page_config(
    page_title="PDF Chatbot",
    page_icon="📄",
    layout="wide"
)

# Sidebar inputs for API key and PDF upload
st.sidebar.title("Settings")
openai_api_key = st.sidebar.text_input("OpenAI API Key", type="password")
uploaded_pdf = st.sidebar.file_uploader("Upload PDF", type=["pdf"])

# Chat title
st.title("PDF Chatbot")

# Check if messages exist in session state, if not initialize
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello there, I am your PDF chatbot."}
    ]
if "vector_store" not in st.session_state:
    st.session_state.vector_store = None

# Display all chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Handle PDF upload
if uploaded_pdf is not None:
    # Save uploaded PDF to a temporary file
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file.write(uploaded_pdf.read())
        tmp_file_path = tmp_file.name

    # Parse PDF content
    reader = PdfReader(tmp_file_path)
    pdf_text = ""
    for page in reader.pages:
        pdf_text += page.extract_text()

    # Initialize vector store with PDF content
    embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
    vector_store = FAISS.from_texts([pdf_text], embeddings)

    # Save vector store in session state
    st.session_state.vector_store = vector_store

    # Notify user of successful PDF processing
    st.success("PDF uploaded and processed successfully!")

# User input
user_prompt = st.chat_input()

if user_prompt is not None and st.session_state.vector_store is not None:
    # Add user message to session state
    st.session_state.messages.append({"role": "user", "content": user_prompt})
    with st.chat_message("user"):
        st.write(user_prompt)

    # Generate AI response using vector store
    llm = ChatOpenAI(openai_api_key=openai_api_key)
    memory = ConversationBufferWindowMemory(memory_key="chat_history", k=10)
    llm_chain = LLMChain(
        llm=llm,
        memory=memory,
        prompt=prompt
    )

    with st.chat_message("assistant"):
        with st.spinner("Loading..."):
            # Get the most relevant text from vector store
            relevant_text = st.session_state.vector_store.similarity_search(user_prompt, k=1)
            combined_prompt = f"{relevant_text[0].page_content}\n\n{user_prompt}"
            ai_response = llm_chain.predict(question=combined_prompt)
            st.write(ai_response)

    # Add assistant message to session state
    st.session_state.messages.append({"role": "assistant", "content": ai_response})
elif user_prompt is not None:
    st.error("Please upload a PDF first.")
