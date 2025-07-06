#!/usr/bin/env bash
set -euo pipefail

# Paths
ROOT="$(cd "$(dirname "$0")"; pwd)"
VENV="$ROOT/.venv"
ACTIVATE="$VENV/bin/activate"
SERVICE_NAME="ps-pool.service"
SYSTEMD_PATH="/etc/systemd/system/$SERVICE_NAME"

echo "1. Creating Python venv..."
python3 -m venv "$VENV"

echo "2. Activating venv and installing deps..."
source "$ACTIVATE"
pip install --upgrade pip
pip install -r "$ROOT/requirements.txt"

echo "3. Copying config files..."
# Assumes .cursor/mcp.json & settings.json already in place; skip or customize

echo "4. Writing systemd unit to $SYSTEMD_PATH..."
sudo tee "$SYSTEMD_PATH" > /dev/null <<EOF
[Unit]
Description=PowerShell MCP Server
After=network.target

[Service]
Type=simple
User=$USER
WorkingDirectory=$ROOT
ExecStart=$ACTIVATE && python $ROOT/mcp_server/__main__.py
Restart=on-failure

[Install]
WantedBy=multi-user.target
EOF

echo "5. Reloading systemd and enabling service..."
sudo systemctl daemon-reload
sudo systemctl enable --now "$SERVICE_NAME"

echo "Deployment complete. Service status:"
sudo systemctl status "$SERVICE_NAME" --no-pager
