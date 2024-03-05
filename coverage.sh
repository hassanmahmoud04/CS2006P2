#!/bin/bash

# Install the coverage tool
pip install coverage

# Assuming 'testing.py' is your main test script
test_script="testing.py"

# Run coverage on the test script
echo "Running coverage for $test_script..."
coverage run $test_script

# Generate a coverage report in the terminal
coverage report -m

# Optionally, generate an HTML report for easier viewing
coverage html

echo "Coverage HTML report generated in htmlcov/index.html"
