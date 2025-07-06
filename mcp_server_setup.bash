#!/usr/bin/env bash
# Deployment script for MCP Server on Linux/macOS/WSL
# Ensure this script is run as root (sudo) for installing system-wide services.

# 1. Create a Python virtual environment in the current directory
if ! command -v python3 &>/dev/null; then
  echo "Error: Python3 is not installed." >&2
  exit 1
fi
python3 -m venv .venv || { echo "Error: Failed to create virtual environment." >&2; exit 1; }

# Activate the virtual environment
# (macOS/Linux/WSL use the same activation script path)
source .venv/bin/activate

# 2. Install Python dependencies from requirements.txt
if [ ! -f "requirements.txt" ]; then
  echo "Error: requirements.txt not found in $(pwd)." >&2
  deactivate
  exit 1
fi
pip install -r requirements.txt || { 
  echo "Error: Failed to install dependencies from requirements.txt." >&2; 
  deactivate; exit 1; 
}

# Deactivate the virtual environment after installing dependencies
deactivate

# 3. Copy or create configuration file into place
CONFIG_DIR="/etc/mcp"
CONFIG_FILE="$CONFIG_DIR/config.json"  # example config file path
mkdir -p "$CONFIG_DIR" || { echo "Error: Cannot create config directory $CONFIG_DIR." >&2; exit 1; }

if [ -f "config.example.json" ]; then
  # If an example config exists in the project, copy it to the system location
  cp -f "config.example.json" "$CONFIG_FILE" || { echo "Error: Failed to copy configuration file." >&2; exit 1; }
else
  # Otherwise, generate a basic default config
  echo "{ \"setting1\": \"value1\", \"setting2\": \"value2\" }" > "$CONFIG_FILE" || {
    echo "Error: Failed to write default configuration." >&2; exit 1;
  }
fi
echo "Configuration file placed at $CONFIG_FILE"

# 4. Register the MCP server as a systemd service (for background startup)
SERVICE_NAME="mcpserver"
SERVICE_FILE="/etc/systemd/system/${SERVICE_NAME}.service"

# Write a systemd unit file for the MCP server
cat > "$SERVICE_FILE" <<EOL
[Unit]
Description=MCP Server Service
After=network.target

[Service]
Type=simple
User=${SUDO_USER:-$USER}
WorkingDirectory=$(pwd)
ExecStart=$(pwd)/.venv/bin/python $(pwd)/server.py
Restart=on-failure

[Install]
WantedBy=multi-user.target
EOL

# Refresh systemd and enable the new service
systemctl daemon-reload || { echo "Error: Failed to reload systemd daemon." >&2; exit 1; }
systemctl enable "${SERVICE_NAME}.service" || { echo "Error: Failed to enable ${SERVICE_NAME} service." >&2; exit 1; }

# Start the service now (if on WSL without systemd, this step may be skipped)
if systemctl start "${SERVICE_NAME}.service" 2>/dev/null; then
  echo "MCP server service '${SERVICE_NAME}' started."
else
  echo "Service installed. You may need to start it manually (or it will start on reboot)."
fi

echo "Deployment script completed successfully."
