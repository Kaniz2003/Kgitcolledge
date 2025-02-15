# ipython-input-1.py
!pip install flask
from flask import Flask, request, jsonify
import google.generativeai as ai

# Configure the API
API_KEY = 'YOUR_API_KEY'  # Replace with your actual API key
ai.configure(api_key=API_KEY)

# Initialize Flask app
app = Flask(__name__)

# Initialize the chatbot model
model = ai.GenerativeModel("gemini-pro")
chat = model.start_chat()

# System message for home remedies focus
SYSTEM_MESSAGE = "You are an expert in home remedies. Only provide natural and home-based solutions for health issues."

@app.route("/chat", methods=["POST"])
def chatbot():
    user_message = request.json.get("message", "")
    if not user_message:
      return jsonify({"response": "Please enter a valid question."})

    # Get response from chatbot
    response = chat.send_message(f"{SYSTEM_MESSAGE}\nUser: {user_message}")

    return jsonify({"response": response.text})

if __name__ == "__main__":
    app.run(debug=True)