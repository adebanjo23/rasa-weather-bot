from flask import Flask, render_template, request, jsonify
import requests  # Add this import

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('chat.html')

@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    response = get_chat_response(msg)
    return jsonify({"text": response})  # Return response as JSON

def get_chat_response(text):
    endpoint = "http://c9c2-197-210-53-174.ngrok-free.app/webhooks/rest/webhook"
    data = {
        "sender": "mayowa",
        "message": text
    }

    response = requests.post(endpoint, json=data)

    if response.status_code == 200:
        messages = response.json()
        print(messages)
        if messages:
            return messages[0]["text"]

    return "Sorry, I couldn't get a response."

if __name__ == '__main__':
    app.run()
