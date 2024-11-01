#!/bin/bash

# Ensure Python and psutil are installed
echo "Checking for Python installation..."
if ! command -v python3 &> /dev/null; then
    echo "Python3 is not installed. Please install it using: sudo dnf install python3"
    exit 1
fi

echo "Checking for psutil library..."
if ! python3 -c "import psutil" &> /dev/null; then
    echo "psutil not found. Installing it..."
    pip3 install psutil
fi

# Run the Python dashboard script
echo "Starting the System Resource Usage Dashboard..."
python3 dashboard.py
