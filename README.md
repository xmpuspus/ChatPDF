# PDF Chatbot with LangChain and OpenAI

![Demo](sample_demo.gif)

This repository contains a Streamlit application that allows users to chat with the content of an uploaded PDF file using OpenAI's GPT-3. The application leverages LangChain for managing conversation flow and embedding PDFs into a vector database for efficient querying.

## Features

- **PDF Upload**: Upload multi-page PDFs to the application.
- **Vector Embedding**: Parse and embed PDF content into a vector store using OpenAI embeddings.
- **Chat Interface**: Interact with the uploaded PDF content through a chat interface.
- **State-of-the-Art Technologies**: Uses the latest versions of Streamlit, LangChain, and OpenAI APIs.

## Packages Used

- `streamlit`: For creating the web application interface.
- `langchain`: For managing the conversation flow and integrating with OpenAI.
- `PyPDF2`: For parsing PDF documents.
- `FAISS`: For efficient vector storage and similarity search.
- `openai`: For accessing OpenAI's GPT-3 API.

## Directory Structure
```markdown
ChatPDF/
├── app.py
├── requirements.txt
├── install_requirements.sh
├── sample_webapp.png
├── sample_demo.gif
```


## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/xmpuspus/ChatPDF.git
    cd ChatPDF
    ```

2. Install the required packages:
    ```bash
    bash install_requirements.sh
    ```

3. Run the Streamlit application:
    ```bash
    streamlit run app.py
    ```

## Application Overview

### Sidebar Inputs

- **OpenAI API Key**: A text input for the user to enter their OpenAI API key.
- **PDF Upload**: A file uploader for users to upload their PDF documents.

### Main Pane

- **Chat Interface**: Displays the chat history and allows users to input their questions.

### Approach

1. **PDF Upload and Parsing**:
    - When a user uploads a PDF, it's saved temporarily and parsed using `PyPDF2`.
    - The extracted text from each page is concatenated into a single string.

2. **Vector Embedding**:
    - The parsed PDF text is embedded into a vector store using `OpenAIEmbeddings` from LangChain.
    - `FAISS` is used to store these embeddings and perform similarity searches efficiently.

3. **Chat Handling**:
    - User inputs are taken from the chat interface.
    - The most relevant text from the vector store is retrieved based on the user's query.
    - This relevant text, combined with the user's query, is used as a prompt for OpenAI's GPT-3 to generate a response.
    - The response is displayed in the chat interface.

## User Experience

1. **Upload PDF**: Users upload their PDF documents through the sidebar.
2. **Enter API Key**: Users input their OpenAI API key to enable AI responses.
3. **Chat Interaction**: Users can ask questions related to the PDF content, and the AI will respond based on the parsed PDF text.

## Security Considerations

- **Injection-Proof**: The application ensures that user inputs cannot override system instructions by strictly defining the prompt template and conversation flow.

## Future Improvements

- **Enhanced Parsing**: Improve PDF parsing to handle complex documents better.
- **Customization**: Allow users to customize the prompt template and other settings.
- **Multi-PDF Support**: Enable handling of multiple PDFs for a broader range of queries.

## Contributions

Contributions are welcome! Please open an issue or submit a pull request for any improvements or features you would like to see.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
