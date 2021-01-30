#!/bin/bash
# path to flask app
export FLASK_APP='scanbrokers/server.py'
# path to json data folder
export WEBSERVER_DATAPATH='./data/'
# run in debug mode? Yes - 1; No - 0
export FLASK_DEBUG=1
flask run