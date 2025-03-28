from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json['message']
    response = query_gemini(user_input)
    return jsonify(response)

def query_gemini(text):
    api_key = "AIzaSyBwowF8XlcnHbIAdRa8yATN9XhRVrCJ35o"  # 使用正确的 API 密钥
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "contents": [
            {
                "parts": [
                    {"text": text}
                ]
            }
        ]
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200 and 'application/json' in response.headers['Content-Type']:
        return response.json()  # 返回 JSON 响应
    else:
        return {'error': 'API call failed or returned non-JSON data', 'status_code': response.status_code}



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
