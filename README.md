Traditional RAG Pipeline using LangChain + Groq LLM

Project Overview
This project implements a Traditional Retrieval-Augmented Generation (RAG) Pipeline using LangChain, Groq LLM, and Hugging Face Embeddings for answering company-related policy questions from internal documents.
The system retrieves accurate answers from multiple PDF documents containing HR policies, company policies, IT security policies, workplace conduct policies, training and development policies, and general organizational policies.
This project is designed to simulate an internal company policy assistant that helps employees quickly retrieve correct information from policy documents using Natural Language Processing and LLM-powered retrieval.
________________________________________
Install Dependencies
pip install -r requirements.txt
________________________________________
Environment Variables
Create a .env file:
GROQ_API_KEY=your_groq_api_key_here
________________________________________
Run the Project
pdf_loader.ipynb
________________________________________
Features
•	Multi-PDF document ingestion 
•	Recursive PDF loading from directory 
•	Metadata-aware document processing 
•	Smart text chunking using RecursiveCharacterTextSplitter 
•	Embedding generation using Hugging Face (all-MiniLM-L6-v2) 
•	Persistent vector storage using ChromaDB 
•	Similarity-based retrieval using semantic search 
•	Groq LLM powered answer generation 
•	Reduced hallucination using context-grounded RAG 
•	Handles HR, IT, Security, and Company Policy questions

________________________________________

How It Works

Step 1: Load PDF Documents
The system recursively loads all PDF files using PyPDFLoader.
Step 2: Text Splitting
Documents are divided into smaller chunks using RecursiveCharacterTextSplitter for better semantic retrieval.
Step 3: Generate Embeddings
Each text chunk is converted into vector embeddings using Hugging Face Sentence Transformers.
Step 4: Store in Vector Database
Embeddings are stored inside:
•	ChromaDB (for persistent vector storage) 
Step 5: Retrieval + Generation
When the user asks a question:
1.	Similar chunks are retrieved from the vector database .
2.	Retrieved context is passed to Groq LLM .
3.	Final answer is generated only from the retrieved context .
This improves factual accuracy and reduces hallucination.
________________________________________
Use Cases
This project can answer questions like:
HR Policies
•	What is the annual leave policy?
•	What is the probation period for new employees?
•	What is the resignation notice period?
IT and Security Policies
•	What are the password requirements?
•	What is the VPN usage policy?
•	What are the rules for confidential data sharing?
Workplace Conduct
•	What is the anti-harassment policy?
•	What is the grievance handling process?
Training and Development
•	What is the certification support policy?
•	What onboarding training is mandatory?
General Company Policies
•	What is the visitor management policy?
•	What is the clean desk policy?
•	What is the emergency evacuation procedure?
________________________________________

Future Improvements
•	Conversational RAG with memory
•	FastAPI production deployment
•	Role-based policy assistant
________________________________________
Learning Outcomes
This project demonstrates:
•	End-to-end Traditional RAG implementation
•	Multi-PDF ingestion pipeline
•	Text chunking strategies
•	Embedding generation using Hugging Face
•	Persistent vector DB creation using ChromaDB
•	Groq LLM integration with LangChain
•	Prompt engineering for grounded answers
•	Enterprise document intelligence system design



