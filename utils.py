def detect_intent(user_input):
    user_input = user_input.lower()

    if any(word in user_input for word in ["buy", "sign up", "try", "purchase", "i want", "pro plan"]):
        return "high_intent"

    elif any(word in user_input for word in ["hi", "hello", "hey"]):
        return "greeting"

    elif any(word in user_input for word in ["price", "pricing", "cost", "plan", "feature"]):
        return "inquiry"

    return "unknown"


def mock_lead_capture(name, email, platform):
    print(f"Lead captured successfully: {name}, {email}, {platform}")