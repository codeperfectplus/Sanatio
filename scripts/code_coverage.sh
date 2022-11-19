#!/bin/bash
check_command() {
    if [ ! -x "$(command -v $1)" ]; then
        echo "$1 is not installed"
        pip install $1
        exit 1
    fi
}

check_command coverage
check_command pytest

coverage run -m pytest
coverage report -> coverage.txt



