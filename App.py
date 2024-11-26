import socket
from flask import Flask, request, jsonify

# 修改 getfqdn 以避免使用系统主机名解析问题
def patched_getfqdn(name=''):
    return 'localhost'

socket.getfqdn = patched_getfqdn

# 创建 Flask 应用
app = Flask(__name__)

# 首页路由
@app.route('/')
def home():
    return "Welcome to the ChatBot Service!"

# 聊天接口路由
@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("message")
    response = generate_response(user_input)
    return jsonify({"response": response})

# 生成简单的 ChatBot 响应
def generate_response(user_input):
    if user_input.lower() == "hello":
        return "Hi there!"
    else:
        return "I'm a simple chatbot, and I don't understand that yet."

# 启动应用
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, use_reloader=False, debug=True)





