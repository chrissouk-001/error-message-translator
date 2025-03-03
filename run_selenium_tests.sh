#!/bin/bash

# Selenium test runner script for Error Message Translator

# Define colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Print header
echo -e "${BLUE}=======================================${NC}"
echo -e "${BLUE}   Error Message Translator           ${NC}"
echo -e "${BLUE}   Selenium Frontend Tests            ${NC}"
echo -e "${BLUE}=======================================${NC}"

# Parse command line options
VERBOSE=0
SPECIFIC_TEST=""

for arg in "$@"
do
    case $arg in
        --verbose|-v)
        VERBOSE=1
        shift
        ;;
        --theme-only)
        SPECIFIC_TEST="tests/integration/test_theme_toggle.py"
        shift
        ;;
        --searches-only)
        SPECIFIC_TEST="tests/integration/test_recent_searches.py"
        shift
        ;;
        --help|-h)
        echo -e "Usage: ./run_selenium_tests.sh [options]"
        echo -e "Options:"
        echo -e "  --verbose, -v    : Show verbose output"
        echo -e "  --theme-only     : Run only theme toggle tests"
        echo -e "  --searches-only  : Run only recent searches tests"
        echo -e "  --help, -h       : Show this help message"
        exit 0
        ;;
    esac
done

# Check for dependencies and install if needed
if ! pip list | grep -q "pytest-selenium"; then
    echo -e "${YELLOW}Installing test dependencies...${NC}"
    echo -e "${YELLOW}This includes all required packages for running tests.${NC}"
    pip install -r requirements-test.txt
fi

# Set pytest verbosity
PYTEST_ARGS=""
if [ $VERBOSE -eq 1 ]; then
    PYTEST_ARGS="-v"
fi

# Execute the tests
echo -e "${YELLOW}Running Selenium tests...${NC}"

if [ -z "$SPECIFIC_TEST" ]; then
    # Run all Selenium tests
    python -m pytest tests/integration/test_recent_searches.py tests/integration/test_theme_toggle.py $PYTEST_ARGS
else
    # Run specific test file
    python -m pytest $SPECIFIC_TEST $PYTEST_ARGS
fi

# Check if tests were successful
if [ $? -eq 0 ]; then
    echo -e "${GREEN}All Selenium tests passed successfully!${NC}"
else
    echo -e "${RED}Some Selenium tests failed. See above for details.${NC}"
    echo -e "${YELLOW}Tip: Try running with --verbose for more information.${NC}"
    exit 1
fi 