# Generative AI Projects using LangChain (OpenAI + Ollama)

This project contains two mini Generative AI apps built using **LangChain**:

1. A **Website Question Answering App** using **OpenAI's GPT-4o**
2. A **Chatbot Web App** using **Ollama's deepseek-r1** model and **Streamlit**

These projects are beginner-friendly and help you understand how to use LangChain with both cloud-based and local LLMs.



## Project 1: Website Q&A using OpenAI

This app can:
- Load data from a website.
- Split that data into smaller text chunks.
- Convert the text into vector format using **OpenAI embeddings**.
- Store and retrieve similar content using **FAISS** vector database.
- Use **GPT-4o** to answer questions based only on the website content.

### What it does:
- Loads this website: `https://docs.smith.langchain.com/administration/tutorials/manage_spend`
- Converts the text into vector embeddings.
- Stores them in a vector store.
- On user query, retrieves matching content and answers using GPT.

###  Libraries Used:
- `langchain`
- `openai`
- `langchain_community`
- `langchain_openai`
- `faiss-cpu`
- `python-dotenv`


##  Project 2: Chatbot Web App using Ollama (deepseek-r1) + Streamlit

This app can:
- Take user input from a simple web interface.
- Use a **local LLM** (`deepseek-r1`) powered by **Ollama**.
- Display the model's response on the webpage in real-time.

###  What it does:
- Creates a chatbot UI using **Streamlit**.
- Loads a prompt template that sets the system behavior.
- Sends the user’s question to the local **deepseek-r1** model using **LangChain’s Ollama wrapper**.
- Returns and displays the generated answer instantly.

###  Libraries Used:
- `langchain`
- `langchain_community`
- `streamlit`
- `python-dotenv`

###  Model Used:
- **deepseek-r1** (run locally via Ollama)

###  Requirements:
- Install [Ollama](https://ollama.com) on your system.
- Pull the required model:
  ```bash
  ollama pull deepseek-r1

### How to run
streamlit run app.py