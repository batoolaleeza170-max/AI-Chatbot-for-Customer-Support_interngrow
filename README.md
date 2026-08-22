🤖 AI Customer Support Chatbot

An intelligent AI-powered customer support chatbot built with Python
and Streamlit. The chatbot can understand customer queries, identify
their intent, search an FAQ knowledge base, maintain conversation
history, calculate confidence scores, and provide context-aware
responses.

📌 Project Overview

This project was developed as Task 2 -- AI Chatbot for Customer
Support (Week 2).

The chatbot is designed to handle common customer support questions
related to:

Orders and order tracking

Refunds

Payments

Delivery

Order cancellation

Damaged products

Delivery address changes

International delivery

Customer support contact information

✨ Features

🧠 Natural Language Understanding

The chatbot processes user questions and matches them with relevant FAQ
information using text similarity.

💬 Context-Aware Responses

The chatbot uses previous conversation messages to provide more relevant
responses.

📚 FAQ Knowledge Base

Frequently asked questions and answers are stored in a JSON knowledge
base.

🎯 Intent Recognition

The chatbot identifies common customer intents such as:

Greeting

Order status

Refund

Payment

Delivery

Cancellation

Complaint

📊 Confidence Score

Each FAQ match produces a confidence score and a confidence level:

🟢 High

🟡 Medium

🔴 Low

💾 Conversation History

Conversation messages are stored using Streamlit session state so the
chatbot can maintain the current conversation.

🎤 Voice Input

Users can speak their questions using a microphone. Speech is converted
into text using the SpeechRecognition library.

🌐 Multi-language Support

The chatbot supports:

English

Urdu

🔢 Tracking Number Detection

The chatbot can detect tracking numbers in customer messages and provide
a tracking-related response.

🧹 Clear Conversation

Users can clear the current conversation from the sidebar.

🛠️ Technologies Used

Python

Streamlit

Scikit-learn

TF-IDF Vectorization

Cosine Similarity

SpeechRecognition

PyAudio

JSON

Regular Expressions

📁 Project Structure

AI Chatbot for Customer Support/
│
├── data/
│   └── faq.json
│
├── modules/
│   ├── chatbot.py
│   ├── confidence.py
│   ├── intent.py
│   └── knowledge_base.py
│   └── speech.py
│
├── app.py
├── .env.example
├── .gitignore
└── README.md

⚙️ How It Works

User Question
      │
      ▼
Text / Voice Input
      │
      ▼
Intent Recognition
      │
      ▼
FAQ Knowledge Base
      │
      ▼
TF-IDF + Cosine Similarity
      │
      ▼
Context-Aware Response
      │
      ▼
Confidence Score
      │
      ▼
Final Chatbot Response

🔍 FAQ Matching

The chatbot uses TF-IDF Vectorization to convert FAQ questions and
the user's question into numerical vectors.

It then uses Cosine Similarity to find the FAQ question most similar
to the user's query.

A similarity threshold is used to avoid returning unreliable FAQ
answers.

🎯 Intent Recognition

The intent recognition module uses predefined keywords to identify the
user's intent.

Example:

"Where is my order?"
        ↓
order_status

"I want my money back"
        ↓
refund

"How can I pay?"
        ↓
payment

🎤 Voice Input

The voice feature uses:

SpeechRecognition
        +
PyAudio
        +
Microphone

The spoken question is converted into text and then processed by the
same chatbot pipeline.

🌐 Multi-language Support

Users can select their preferred language from the sidebar.

Supported languages:

Language   Support

English    ✅
Urdu       ✅

🚀 Installation

1. Clone the repository

git clone YOUR_GITHUB_REPOSITORY_URL
cd "AI Chatbot for Customer Support"

2. Create a virtual environment

python -m venv venv

3. Activate the virtual environment

Windows PowerShell:

venv\Scripts\activate

4. Install dependencies

pip install streamlit scikit-learn SpeechRecognition PyAudio

5. Run the application

streamlit run app.py

The application will open in your browser.

🧪 Example Questions

Try questions such as:

What are your business hours?

How can I track my order?

What is your refund policy?

How can I cancel my order?

What payment methods do you accept?

How long does delivery take?

My order arrived damaged. What should I do?

Can I change my delivery address?

📊 Example Response

You can request a refund within 7 days of receiving your
order, subject to our refund conditions.

Intent: refund

Confidence Score: 86% 🟢 High

🔐 Security

Do not upload or commit API keys, passwords, or other secrets to GitHub.

Use .gitignore to exclude sensitive files such as:

.env
venv/
__pycache__/

🎓 Learning Outcomes

This project demonstrates practical experience with:

NLP fundamentals

Text similarity

TF-IDF

Cosine similarity

Intent classification

Chatbot development

Context handling

Streamlit application development

Speech-to-text

Multi-language response handling

Python modular programming

👩‍💻 Project

AI Chatbot for Customer Support

Task: Task 2 -- Week 2
Domain: AI / NLP / Chatbot Development
Interface: Streamlit

📄 License

This project is created for educational and internship/project
demonstration purposes.
