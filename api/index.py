from flask import Flask, request, jsonify
from flask_basicauth import BasicAuth
import ssl

app = Flask(__name__)

# 配置基本认证
app.config['BASIC_AUTH_USERNAME'] = 'admin'
app.config['BASIC_AUTH_PASSWORD'] = 'admin@123'
basic_auth = BasicAuth(app)


@app.route('/uxi_data', methods=['POST'])
@basic_auth.required
def receive_uxi_data():
    if request.is_json:
        data = request.get_json()
        # 这里处理接收到的数据
        print("Received UXI data:", data)
        # 在这里可以添加数据处理、存储或转发的逻辑
        return jsonify({"status": "success", "message": "Data received"}), 200
    else:
        return jsonify({"status": "error", "message": "Invalid data format"}), 400
