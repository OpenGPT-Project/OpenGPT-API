from opengpt import OpenGPT

# Create an instance of OpenAIWrapper
OpenGPT = OpenGPT()

user_input = input("Enter your message: ")
assistant_reply = OpenGPT.openai_default(user_input)

if assistant_reply:
    print(f"Assistant's reply: {assistant_reply}")
