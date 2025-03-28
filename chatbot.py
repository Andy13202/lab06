import requests
import json

def query_gemini(api_key, text):
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}'
    }
    payload = {
        "contents": [
            {
                "parts": [{"text": text}]
            }
        ]
    }
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    return response.json()

# 你的 API 密钥
api_key = 'AIzaSyCeZRz0ALQPUuaxzOpLDvZJ-sqigNhX_vI'
# 你想要提问的问题
question = "Explain how AI works"

# 发送请求并打印响应
result = query_gemini(api_key, question)
print(json.dumps(result, indent=4))
