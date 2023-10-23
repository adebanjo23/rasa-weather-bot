from flask import Flask, render_template, request, jsonify
import requests  # Add this import

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('chat.html')

@app.route("/get", methods=["GET", "POST"])
def chat():
    print("Here")
    msg = request.form["msg"]
    response = get_chat_response(msg)
    return jsonify({"text": response})  # Return response as JSON

def get_chat_response(text):
    print("Here2")
    endpoint = "http://d40d-197-210-52-75.ngrok-free.app/webhooks/rest/webhook"
    data = {
        "sender": "mayowa",
        "message": text
    }

    response = requests.post(endpoint, json=data)
    print("got_here")


    messages = response.json()
    print(messages)
    if messages:
        return messages[0]["text"]

    return "Sorry, I couldn't get a response."

if __name__ == '__main__':
    app.run()
