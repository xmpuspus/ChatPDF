#!/bin/bash

# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install the requirements
pip install -r requirements.txt

echo "Installation complete. To activate the virtual environment, run 'source venv/bin/activate'."

source venv/bin/activate