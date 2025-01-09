# Website-QA-Chatbot-with-Gemini
A smart chatbot that can answer questions about any website's content using Google's Gemini AI and LangChain.
# Website QA Chatbot with Gemini
A smart chatbot that can answer questions about any website's content using Google's Gemini AI and LangChain.

## 🌟 Key Features
- Scrapes and processes website content through sitemaps
- Uses state-of-the-art embeddings for semantic search
- Powered by Google's Gemini AI for natural responses
- Automatic PDF generation for offline access
- Intelligent context chunking for better comprehension

## 🚀 Quick Start
1. Clone the repository
```bash
git clone https://github.com/yourusername/website-qa-chatbot.git
cd website-qa-chatbot
```

2. Install requirements
```bash
pip install -r requirements.txt
```

3. Set up your Gemini API key
```python
# Create a .env file and add your API key
GEMINI_API_KEY=your_api_key_here
```

4. Run the chatbot
```python
python main.py
```

## 📦 Project Structure
```
website-qa-chatbot/
├── main.py               # Main application file
├── utils/
│   ├── document_processor.py  # Document processing utilities
│   ├── embeddings.py         # Embedding functions
│   └── chat_interface.py     # Chat interface functions
├── requirements.txt     # Project dependencies
├── .env.example        # Example environment variables
├── .gitignore          # Git ignore file
└── README.md           # Project documentation
```

## 💻 Usage Example
```python
from chatbot import WebsiteQABot

# Initialize the bot
bot = WebsiteQABot(api_key="your_gemini_api_key")

# Process a website
bot.process_website("https://example.com/sitemap.xml")

# Start chatting
bot.start_chat()
```

## 🔑 Requirements
- Python 3.8+
- Gemini API key
- Internet connection for website scraping

