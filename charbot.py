from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json['message']
    response = query_gemini(user_input)
    return jsonify(response)

def query_gemini(text):
    api_key = "YOUR_API_KEY_HERE"
    url = "https://api.google.com/gemini/v1beta/chat"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {"input": text}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
