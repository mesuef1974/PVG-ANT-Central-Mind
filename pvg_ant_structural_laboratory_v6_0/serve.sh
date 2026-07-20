#!/usr/bin/env sh
set -eu
cd "$(dirname "$0")"
echo 'PVG–ANT Structural Laboratory v6.0: http://localhost:8000'
python -m http.server 8000
