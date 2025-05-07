import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY")

def chat_with_gemini(prompt):
    model = genai.GenerativeModel('gemini-2.5-pro-exp-03-25')
    response = model.generate_content(prompt)
    return response.text

print("Hello, I am a Chatbox! Ask anything!")

while True:
    prompt = input("You:")
    if prompt.lower() == "exit":
        break
    reply = chat_with_gemini(prompt)
    print("Gemini: ", reply, "\n")




