#!/bin/sh
set -e
python3 -m flask db upgrade
python3 run.py
