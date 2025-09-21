from google import genai

# Initialize the GenAI client
client = genai.Client(api_key="Your_Api_Key_Here")
model = "gemini-2.5-flash"

def create_chat():
    history = []
    def chat(user_input):
        history.append(f"role: user, content: {user_input}")
        response = client.models.generate_content(
            model=model,
            contents=history
        )
        assistant_reply = response.text
        history.append(f"role: assistant, content: {assistant_reply}")
        return assistant_reply
    return chat

# Usage:

if __name__ == "__main__":
    # Example interaction
    chat = create_chat()
    while True:
        user_input = input("Me: ")
        print("Gemini says:", chat(user_input))
