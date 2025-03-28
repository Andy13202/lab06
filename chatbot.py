import requests
import json

def query_gemini(query):
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"
    headers = {
        "Authorization": "Bearer AIzaSyCeZRz0ALQPUuaxzOpLDvZJ-sqigNhX_vI",
        "Content-Type": "application/json"
    }
    payload = {
        "contents": [
            {
                "parts": [{"text": query}]
            }
        ]
    }
    response = requests.post(url, headers=headers, json=payload)
    return response.json()

# 使用例子
result = query_gemini("Explain how AI works")
print(json.dumps(result, indent=4))
