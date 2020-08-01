#!/bin/bash

EXPORT FLASK_APP=app.py
EXPORT FLASK_ENV=development

source venv/bin/activate

python -m flask run
