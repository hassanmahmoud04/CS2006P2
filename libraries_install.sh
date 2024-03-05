#!/bin/bash

# Define external libraries to install
libraries=("pytest" "numpy")

# Loop through the libraries and install them using pip
for lib in "${libraries[@]}"; do
    echo "Installing $lib..."
    pip install "$lib"
done

echo "All specified libraries have been installed."
