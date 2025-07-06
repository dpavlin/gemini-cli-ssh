
from flask import Flask, request, jsonify
from ssh_executor import execute_ssh_command

app = Flask(__name__)

@app.route('/mcp/execute', methods=['POST'])
def mcp_execute():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    hostname = data.get('hostname')
    username = data.get('username')
    password = data.get('password')
    command = data.get('command')

    if not all([hostname, username, password, command]):
        return jsonify({"error": "Missing required parameters"}), 400

    result = execute_ssh_command(hostname, username, password, command)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
