from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json['message']
    response = query_gemini(user_input)
    return jsonify(response)

def query_gemini(text):
    api_key = "YOUR_API_KEY_HERE"  # 确保这里填写了正确的 API 密钥
    url = "https://api.google.com/gemini/v1beta/chat"  # 确保这里是正确的 API URL
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {"input": text}
    response = requests.post(url, headers=headers, json=data)
    # 检查响应状态码和内容类型
    if response.status_code == 200 and 'application/json' in response.headers['Content-Type']:
        return response.json()  # 返回 JSON 响应
    else:
        # 如果响应不是 JSON 或请求失败，返回错误信息
        return {'error': 'API call failed or returned non-JSON data', 'status_code': response.status_code}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
