#!/bin/bash
export FLASK_APP='scanbrokers/server.py'
export WEBSERVER_DATAPATH='./data/'
export FLASK_DEBUG=1
flask run