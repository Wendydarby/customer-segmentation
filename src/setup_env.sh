#!/bin/bash

# Step 1: Create a virtual environment
echo "Creating virtual environment..."
python3 -m venv venv

# Step 2: Activate the virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Step 3: Install required packages
echo "Installing required packages..."
pip install --upgrade pip
pip install pandas numpy matplotlib scikit-learn

# Step 4: Confirm installation
echo "Installed packages:"
pip list

echo "Environment setup is complete. To activate the environment, run: source venv/bin/activate"