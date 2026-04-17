#!/bin/bash

# Activate the virtual environment
source venv/Scripts/activate

# Run the test suite
pytest test_app.py --webdriver Chrome

# Capture the exit code from pytest
EXIT_CODE=$?

# Return 0 if passed, 1 if failed
if [ $EXIT_CODE -eq 0 ]; then
    echo "All tests passed!"
    exit 0
elses
    echo "Some tests failed!"
    exit 1
fi