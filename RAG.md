Resume RAG System
A Retrieval-Augmented Generation (RAG) system that allows users to ask questions about a resume PDF using semantic search and Google's Gemini Large Language Model. The system extracts resume content, stores embeddings in ChromaDB, retrieves relevant information, and generates accurate answers based solely on the resume content.

Features
PDF resume text extraction
Intelligent text chunking with overlap
Semantic embeddings using Sentence Transformers
Vector storage with ChromaDB
Similarity-based retrieval
Gemini-powered answer generation
Context-aware responses
Reduced hallucinations through RAG
CPU-only execution (GPU not required)
Architecture
Resume PDF
    │
    ▼
PDF Text Extraction
(pdfplumber)
    │
    ▼
Text Chunking
    │
    ▼
Embedding Generation
(Sentence Transformers)
    │
    ▼
ChromaDB Vector Store
    │
    ▼
User Query
    │
    ▼
Semantic Similarity Search
    │
    ▼
Relevant Context Retrieval
    │
    ▼
Google Gemini
    │
    ▼
Generated Answer
Tech Stack
Component	Technology
Language	Python
LLM	Google Gemini
Vector Database	ChromaDB
Embedding Model	Sentence Transformers
PDF Processing	pdfplumber
Deep Learning Framework	PyTorch
Project Structure
resume-rag/
│
├── rag.py
├── resume.pdf
├── README.md
├── requirements.txt
│
└── chroma_db/
Installation
1. Clone the Repository
git clone https://github.com/yourusername/resume-rag.git

cd resume-rag
2. Install Dependencies
pip install pdfplumber chromadb sentence-transformers google-generativeai torch
Alternatively:

pip install -r requirements.txt
Configuration
Configure Gemini API Key
Locate:

genai.configure(api_key="")
Replace with:

genai.configure(api_key="YOUR_GEMINI_API_KEY")
Add Resume PDF
Place your resume PDF inside the project folder.

Example:

pdf_path = "resume.pdf"
Running the Application
Run the following command:

python rag.py
Expected startup output:

Extracting text from resume...
Chunking text into smaller segments...
Generating embeddings and storing in ChromaDB...

RAG System Ready!
Type 'exit' to stop.
Example Queries
What skills does the candidate have?

What projects has the candidate completed?

What programming languages are mentioned?

What certifications are listed?

What is the candidate's educational background?
Sample Response
Query
What skills does the candidate have?
Response
The candidate has experience in:

- Python
- Machine Learning
- Deep Learning
- Data Structures and Algorithms
- Natural Language Processing
If the information does not exist in the resume:

Not mentioned in the resume.
How It Works
Step 1: Resume Parsing
The PDF resume is processed using pdfplumber to extract text content.

Step 2: Text Chunking
The extracted text is divided into overlapping chunks to preserve context.

Step 3: Embedding Generation
Sentence Transformers convert each chunk into vector embeddings.

Step 4: Vector Storage
Embeddings are stored inside ChromaDB for efficient retrieval.

Step 5: Query Processing
User questions are converted into embeddings and matched against stored vectors.

Step 6: Context Retrieval
The most relevant chunks are retrieved based on semantic similarity.

Step 7: Answer Generation
Retrieved context is passed to Gemini, which generates answers strictly from resume content.

Applications
AI Resume Assistant
Recruitment Automation
Candidate Evaluation
Resume Search Engine
HR Analytics
Career Guidance Platforms
Intelligent Applicant Tracking Systems
Advantages
Fast semantic search
Accurate context retrieval
Reduced hallucinations
Efficient vector search
Lightweight CPU execution
Easy deployment
Scalable architecture
Future Enhancements
Multi-resume support
Resume ranking system
Streamlit web application
Chat history memory
Persistent ChromaDB storage
Hybrid search (keyword + semantic)
Recruiter dashboard
Voice-based interaction
Multi-user support
Learning Outcomes
This project helps in understanding:

Retrieval-Augmented Generation (RAG)
Vector Databases
Embedding Models
Semantic Search
Large Language Models
ChromaDB Integration
Gemini API Usage
End-to-End AI Application Development
