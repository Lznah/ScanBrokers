#!/bin/bash
export FLASK_APP=server.py
export FLASK_DEBUG=1
export JSON_DATA_FOLDER='./data/'
flask run