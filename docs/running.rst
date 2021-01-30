***********
How to run?
***********

Open file ``./run.sh`` and set environment variables there. 


Environment variables
---------------------

This is a list of environment variables, that you need to editor in ``./run.sh`` file before running.
# path to flask app
export FLASK_APP='scanbrokers/server.py'
# path to json data folder
export WEBSERVER_DATAPATH='./data/'
# run in debug mode? Yes - 1; No - 0
export FLASK_DEBUG=1

+--------------+--------------------------------------------------------------------------------------------+
| ``FLASK_APP`` | An absolute or relative path to flask application, where is create_app factory defined    |
+--------------+--------------------------------------------------------------------------------------------+
| ``WEBSERVER_DATAPATH`` | A path to folder, where you have JSON data from over WebScraper stored.          |
+--------------+--------------------------------------------------------------------------------------------+
| ``FLASK_DEBUG`` | Do you want to run application in debug mode? If yes, set it to 1. If not, set it to 0. |
+--------------+--------------------------------------------------------------------------------------------+

Now run this to start the server:

.. code-block:: console

    flash run