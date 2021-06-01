#!/bin/sh
set -e
#SQLALCHEMY_DATABASE_URI: postgresql+psycopg2://purple:purple@db/purple python3 -m flask db upgrade
#APP_SETTINGS=production python3 -m flask db upgrade
python3 -m flask db upgrade
#python3 run.py
