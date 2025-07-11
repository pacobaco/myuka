#!/usr/bin/env bash
set -e
export REGION=$1
pkill -f 'python3 app.py' || true
python3 app.py &  # Serve the region content on 127.0.0.1:8080
sleep 2
python3 publish_region.py