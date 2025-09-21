from google import genai

# Initialize the GenAI client
client = genai.Client(api_key="Your_Api_Key_Here")

# Define the model
model = "gemini-2.5-flash"

# Store conversation history
history = []

# Function to interact with the chatbot
def chat_with_gemini(user_input):
    history.append(f"role: user, content: {user_input}")
    
    response = client.models.generate_content(
        model=model,
        contents=history
    )
    
    assistant_reply = response.text
    history.append(f"role: assistant, content: {assistant_reply}")
    
    return assistant_reply

# Example interaction
while True:
    user_input = input("Me: ")
    print("Gemini says:", chat_with_gemini(user_input))
