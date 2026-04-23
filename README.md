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
mock_lead_capture(name, email, platform)
