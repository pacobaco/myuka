#!/usr/bin/env bash
set -e
source .env
pkill -f 'python3 app.py' || true
python3 app.py &
sleep 2
ADDR=$(python3 rotate_onion.py)
echo "🔗 Site available at $ADDR"