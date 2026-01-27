#!/bin/bash
# Web E2E Test Environment Setup Script
# Web CAM E2E Automation Test Framework

set -e

echo "=========================================="
echo "Web E2E Test Environment Setup"
echo "=========================================="

# Check Python version
echo ""
echo "[1/4] Checking Python version..."
python3 --version || { echo "Error: Python 3 is required"; exit 1; }

# Create virtual environment if not exists
echo ""
echo "[2/4] Setting up virtual environment..."
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo "Virtual environment created."
else
    echo "Virtual environment already exists."
fi

# Activate virtual environment
source venv/bin/activate

# Install dependencies
echo ""
echo "[3/4] Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Install Playwright browsers
echo ""
echo "[4/4] Installing Playwright browsers..."
playwright install chromium
playwright install firefox

echo ""
echo "=========================================="
echo "Setup completed successfully!"
echo "=========================================="
echo ""
echo "To activate the environment:"
echo "  source venv/bin/activate"
echo ""
echo "To run tests:"
echo "  pytest Web/tests/ -v"
echo ""
echo "To run specific test file:"
echo "  pytest Web/tests/test_sample.py -v"
echo ""
echo "To run with HTML report:"
echo "  pytest Web/tests/ -v --html=report.html"
echo ""
