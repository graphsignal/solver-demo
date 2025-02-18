#!/bin/bash

set -e 

source venv/bin/activate
python solver/main.py
deactivate