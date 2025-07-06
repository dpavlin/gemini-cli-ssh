
import argparse
import paramiko

def execute_ssh_command(hostname, username, password, command):
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname, username=username, password=password)

        stdin, stdout, stderr = client.exec_command(command)
        output = stdout.read().decode()
        errors = stderr.read().decode()

        return {"output": output, "errors": errors}

    except Exception as e:
        return {"error": str(e)}

    finally:
        if 'client' in locals() and client.get_transport() and client.get_transport().is_active():
            client.close()

def main():
    parser = argparse.ArgumentParser(description='SSH Command Executor')
    parser.add_argument('hostname', help='Remote host')
    parser.add_argument('username', help='Username')
    parser.add_argument('password', help='Password')
    parser.add_argument('command', help='Command to execute')
    args = parser.parse_args()

    result = execute_ssh_command(args.hostname, args.username, args.password, args.command)

    if "error" in result:
        print(f"An error occurred: {result['error']}")
    else:
        print(f"Output from {args.hostname}:\n{result['output']}")
        print(f"Errors from {args.hostname}:\n{result['errors']}")

if __name__ == '__main__':
    main()
