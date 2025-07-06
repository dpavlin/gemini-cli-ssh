
import argparse
import requests
import json

def main():
    parser = argparse.ArgumentParser(description='MCP SSH Client')
    parser.add_argument('hostname', help='Remote host')
    parser.add_argument('username', help='Username')
    parser.add_argument('password', help='Password')
    parser.add_argument('command', help='Command to execute')
    args = parser.parse_args()

    url = 'http://127.0.0.1:5001/mcp/execute'
    payload = {
        'hostname': args.hostname,
        'username': args.username,
        'password': args.password,
        'command': args.command
    }
    headers = {'Content-Type': 'application/json'}

    try:
        response = requests.post(url, data=json.dumps(payload), headers=headers)
        response.raise_for_status()  # Raise an exception for bad status codes
        print(json.dumps(response.json(), indent=4))

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
    except json.JSONDecodeError:
        print(f"Failed to decode JSON response: {response.text}")


if __name__ == '__main__':
    main()
