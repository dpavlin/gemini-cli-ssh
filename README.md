# Gemini CLI SSH Integration

This project demonstrates how to integrate SSH command execution with the Gemini CLI using the Model Context Protocol (MCP).

## Setup Instructions

**Note:** If you are interacting with this repository through a model-managed environment (e.g., Gemini CLI), the model will handle the setup instructions for you, and you do not need to perform venv steps manually.

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

## Model Prompt Instructions

To instruct the Gemini CLI model to manage the MCP server, you can use the following prompts:

*   **Start the MCP server:** `Model, please start the MCP server.`
*   **Restart the MCP server:** `Model, please restart the MCP server.`

When prompted with these commands, the model will:

*   **Start the MCP server:** Check if the `mcp_server.py` process is already running. If it's not, it will activate the virtual environment and run `python3 mcp_server.py` in the background.
*   **Restart the MCP server:** Attempt to stop any running `mcp_server.py` process. Then, it will activate the virtual environment and start a new `python3 mcp_server.py` process in the background.
