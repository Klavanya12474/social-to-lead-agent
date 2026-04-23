# Social-to-Lead Agentic Workflow 🚀

This project is a Conversational AI Agent built as part of the Machine Learning Intern Assignment for ServiceHive's product **Inflx**.

The agent simulates a real-world SaaS sales assistant for a fictional company called **AutoStream**, an automated video editing platform for content creators.

---

## Features ✨

### 1. Intent Detection
The agent identifies user intent into:
- Casual Greeting
- Product / Pricing Inquiry
- High-Intent Lead

---

### 2. Knowledge Retrieval (RAG-like)
The agent answers questions from a local knowledge base stored in JSON.

### Pricing Plans

#### Basic Plan
- $29/month
- 10 videos/month
- 720p resolution

#### Pro Plan
- $79/month
- Unlimited videos
- 4K resolution
- AI Captions
- 24/7 Support

---

### 3. Lead Capture Tool Execution
When the user shows high intent, the agent collects:

- Name
- Email
- Creator Platform

Then executes a mock tool:

```python

social-to-lead-agent/
│
├── app.py
├── utils.py
├── knowledge_base.json
├── requirements.txt
└── README.md

pip install -r requirements.txt

python app.py

You: Hi
Agent: Hello! Welcome to AutoStream. How can I help you?

You: Tell me pricing
Agent: Here are our plans...

You: I want pro plan
Agent: Please provide your name.

You: Lavanya
Agent: Please provide your email.

You: lavanya@gmail.com
Agent: Which creator platform do you use?

You: YouTube
Lead captured successfully: Lavanya, lavanya@gmail.com, YouTube

