from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    # 从 POST 请求中提取消息
    user_input = request.json['message']
    # 获取 API 响应
    response = query_gemini(user_input)
    # 以 JSON 形式返回 API 响应
    return jsonify(response)

def query_gemini(text):
    # 你的实际 API 密钥
    api_key = "AIzaSyBwowF8XlcnHbIAdRa8yATN9XhRVrCJ35o"
    # API URL
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"
    # 请求头部
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    # 请求数据
    data = {
        "contents": [
            {
                "parts": [{"text": text}]
            }
        ]
    }
    # 发送 API 请求
    response = requests.post(url, headers=headers, json=data)
    # 为调试打印请求和响应信息
    print(f"发送请求到 {url}，头部 {headers} 和数据 {data}")
    print(f"收到响应状态 {response.status_code} 和内容 {response.text}")
    # 检查响应状态码和内容类型
    if response.status_code == 200 and 'application/json' in response.headers['Content-Type']:
        return response.json()
    else:
        # 如果出现问题返回错误信息
        return {'error': 'API 调用失败或返回非 JSON 数据', 'status_code': response.status_code}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
