import requests
# pip intsall sseclient-py
import sseclient


# SSE API 的 URL
url = 'http://127.0.0.1:8000/stream_chat?prompt=helloworld'
# print(url)

# 使用 requests 发送 GET 请求并保持连接
response = requests.post(url, stream=True)

print(f"Response Status Code: {response.status_code}")
if response.status_code != 200:
    print("Failed to connect to the SSE API")

# 使用 sseclient 处理 SSE 数据流
client = sseclient.SSEClient(response)
# 逐条读取事件并处理
for event in client.events():
    print(event.data)
