import json
from utils import detect_intent, mock_lead_capture

# Load knowledge base
with open("knowledge_base.json", "r") as f:
    kb = json.load(f)

lead_data = {
    "name": None,
    "email": None,
    "platform": None
}

high_intent_mode = False

print("AutoStream AI Agent is running... Type 'exit' to stop.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    intent = detect_intent(user_input)

    if high_intent_mode:
        if not lead_data["name"]:
            lead_data["name"] = user_input
            print("Agent: Please provide your email.")
            continue

        elif not lead_data["email"]:
            lead_data["email"] = user_input
            print("Agent: Which creator platform do you use?")
            continue

        elif not lead_data["platform"]:
            lead_data["platform"] = user_input
            mock_lead_capture(
                lead_data["name"],
                lead_data["email"],
                lead_data["platform"]
            )
            print("Agent: Thank you! Our team will contact you soon.")
            high_intent_mode = False
            continue

    if intent == "greeting":
        print("Agent: Hello! Welcome to AutoStream. How can I help you?")

    elif intent == "inquiry":
        print("Agent: Here are our plans:")
        for plan, details in kb["plans"].items():
            print(f"{plan}: {details}")

    elif intent == "high_intent":
        print("Agent: Great! I'd love to help you get started.")
        print("Agent: Please provide your name.")
        high_intent_mode = True

    else:
        print("Agent: Can you please clarify your question?")