from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "AI API Running"

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")

    if "who made you" in user_message.lower():
        reply = "I was created by Ay"

    else:
        reply = "Hello, I am your AI bot"

    return jsonify({"reply": reply})

app.run(host="0.0.0.0", port=10000)
