#!/bin/bash

# Simple test runner script for Error Message Translator

# Define colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Print header
echo -e "${BLUE}=======================================${NC}"
echo -e "${BLUE}   Error Message Translator Tests      ${NC}"
echo -e "${BLUE}=======================================${NC}"

# Parse command line options
COVERAGE=0
UNIT_ONLY=0
INTEGRATION_ONLY=0
VERBOSE=0

for arg in "$@"
do
    case $arg in
        --coverage|-c)
        COVERAGE=1
        shift
        ;;
        --unit|-u)
        UNIT_ONLY=1
        shift
        ;;
        --integration|-i)
        INTEGRATION_ONLY=1
        shift
        ;;
        --verbose|-v)
        VERBOSE=1
        shift
        ;;
        --help|-h)
        echo -e "Usage: ./run_tests.sh [options]"
        echo -e "Options:"
        echo -e "  --coverage, -c   : Run tests with coverage report"
        echo -e "  --unit, -u       : Run only unit tests"
        echo -e "  --integration, -i: Run only integration tests"
        echo -e "  --verbose, -v    : Show verbose output"
        echo -e "  --help, -h       : Show this help message"
        exit 0
        ;;
    esac
done

# Execute the tests
if [ $COVERAGE -eq 1 ]; then
    # Coverage mode
    echo -e "${YELLOW}Running tests with coverage...${NC}"
    
    if [ $UNIT_ONLY -eq 1 ]; then
        pytest --cov=app tests/unit/ --cov-report term-missing
    elif [ $INTEGRATION_ONLY -eq 1 ]; then
        pytest --cov=app tests/integration/ --cov-report term-missing
    else
        pytest --cov=app tests/ --cov-report term-missing
    fi
else
    # Regular mode
    PYTEST_ARGS=""
    
    if [ $VERBOSE -eq 1 ]; then
        PYTEST_ARGS="-v"
    fi
    
    if [ $UNIT_ONLY -eq 1 ]; then
        echo -e "${YELLOW}Running unit tests...${NC}"
        pytest $PYTEST_ARGS tests/unit/
    elif [ $INTEGRATION_ONLY -eq 1 ]; then
        echo -e "${YELLOW}Running integration tests...${NC}"
        pytest $PYTEST_ARGS tests/integration/
    else
        echo -e "${YELLOW}Running all tests...${NC}"
        pytest $PYTEST_ARGS
    fi
fi

# Check if tests were successful
if [ $? -eq 0 ]; then
    echo -e "${GREEN}All tests passed successfully!${NC}"
else
    echo -e "${RED}Some tests failed. See above for details.${NC}"
    exit 1
fi 