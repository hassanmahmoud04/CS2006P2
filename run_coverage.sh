#!/bin/bash

# Step 1: Install coverage
echo "Installing coverage..."
pip install coverage

# Step 2: Run pytest with coverage on the testing.py file
echo "Running tests with coverage..."
coverage run -m pytest all_pytests.py

# Step 3: Generate the coverage report with missing lines
echo "Generating coverage report..."
coverage report -m
