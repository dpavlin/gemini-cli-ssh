# Gemini CLI SSH Integration

This project demonstrates how to integrate SSH command execution with the Gemini CLI using the Model Context Protocol (MCP).

## Setup Instructions

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/dpavlin/gemini-cli-ssh.git
    cd gemini-cli-ssh
    ```

2.  **Create and activate a virtual environment:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Start the MCP Server:**

    The MCP server needs to be running in the background. This server exposes the SSH execution functionality.

    ```bash
    source venv/bin/activate && python3 mcp_server.py &
    ```

5.  **Use the MCP Client:**

    You can now use the `mcp_client.py` script to execute commands on remote machines via the MCP server. The client takes the hostname, username, password, and the command as arguments.

    ```bash
    python3 mcp_client.py <hostname> <username> <password> '<command>'
    ```

    **Example:**

    ```bash
    python3 mcp_client.py klin dpavlin your_password 'uname -a'
    ```

    **Note:** For security, it is highly recommended to use SSH keys for authentication instead of providing passwords directly in the command line, especially in production environments. You can configure your SSH client (`~/.ssh/config`) to use keys.
