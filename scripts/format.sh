#usr/bin/bash
app_dir="games_tracker_app"
if ! command -v python3 &>/dev/null; then
    echo "Python3 is not installed. Please install it and try again."
    exit 1
fi
source venv/bin/activate
black $app_dir
djhtml $app_dir
