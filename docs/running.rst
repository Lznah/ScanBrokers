***********
How to run?
***********

Open file ``./run.sh`` and set environment variables there. 


Environment variables
---------------------

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