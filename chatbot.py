import requests

def ask_chatgpt(prompt):
    headers = {
        'Authorization': 'Bearer YOUR_API_KEY',
        'Content-Type': 'application/json',
    }
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": prompt}]
    }
    response = requests.post('https://api.openai.com/v1/chat/completions', headers=headers, json=data)
    return response.json()

# 示例调用
response = ask_chatgpt("Hello, how are you?")
print(response)
