!pip install langchain==0.0.189
!pip install huggingface_hub
!pip install sentence_transformers
!pip install openai
!pip install tiktoken
!pip install nest_asyncio

import nest_asyncio
nest_asyncio.apply()

from langchain.document_loaders.sitemap import SitemapLoader

loader = SitemapLoader(
    "https://giki.edu.pk/sitemap_index.xml", #Insert your own link here
    filter_urls=["https://giki.edu.pk/admissions/admissions-undergraduates/"]
)
documents = loader.load()

!pip install google-generativeai
!pip install faiss-cpu

import google.generativeai as genai
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
import textwrap

# Configure Gemini
genai.configure(api_key='input your gemini api')
model = genai.GenerativeModel('gemini-pro')

# Process the documents with smaller chunks and more overlap
def split_documents(documents):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100,
        length_function=len,
        separators=["\n\n", "\n", " ", ""]
    )
    chunks = text_splitter.split_documents(documents)
    print(f"Created {len(chunks)} document chunks")
    return chunks

# Create vector store
def create_vector_store(chunks):
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vector_store = FAISS.from_documents(chunks, embeddings)
    return vector_store

# Initialize the QA system - Adding the missing function
def initialize_qa_system(documents):
    chunks = split_documents(documents)
    vector_store = create_vector_store(chunks)
    return vector_store

# Improved function to get relevant chunks
def get_relevant_chunks(vector_store, query, k=4):
    docs = vector_store.similarity_search(query, k=k)
    context = "\n\n".join([doc.page_content for doc in docs])
    return context

# Improved prompt template for Gemini
def generate_response(query, context):
    prompt = f"""You are a helpful assistant for GIKI (Ghulam Ishaq Khan Institute) admissions. 
    Use the following context to answer the question. 
    Be direct and concise in your response.
    If you're not completely sure about something, say so.
    
    Context:
    {context}
    
    Question: {query}
    
    Answer:"""
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error generating response: {str(e)}"

# Debug function to show retrieved context
def debug_context(context):
    print("\nDebug - Retrieved Context:")
    print("-" * 50)
    print(context)
    print("-" * 50)

# Main chat interface with debugging
def chat_interface(vector_store):
    print("Welcome to the GIKI Admissions QA Bot! (Type 'quit' to exit)")
    print("Type 'debug' to see the retrieved context for your last question")
    print("-" * 50)
    
    last_context = None
    
    while True:
        query = input("\nYour question: ").strip()
        
        if query.lower() == 'quit':
            print("Thank you for using the QA Bot!")
            break
            
        if query.lower() == 'debug':
            if last_context:
                debug_context(last_context)
            continue
            
        if query:
            # Get relevant document chunks
            context = get_relevant_chunks(vector_store, query)
            last_context = context
            
            # Generate response
            response = generate_response(query, context)
            
            # Print response with nice formatting
            print("\nAnswer:", textwrap.fill(response, width=80))
            print("-" * 50)

# Print document content before processing
print("Initial document content preview:")
for i, doc in enumerate(documents):
    print(f"\nDocument {i + 1} preview (first 200 characters):")
    print(doc.page_content[:200])
    print("-" * 50)

# Initialize and start the chatbot
vector_store = initialize_qa_system(documents)
chat_interface(vector_store)
