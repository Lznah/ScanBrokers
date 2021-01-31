***********
How to run?
***********

Open file ``./run.sh`` and set environment variables there. 


Environment variables
---------------------

+------------------------+-----------------------------------------------------------------------------------------+
| ``FLASK_APP``          | An absolute or relative path to flask application, where is create_app factory defined  |
+------------------------+-----------------------------------------------------------------------------------------+
| ``WEBSERVER_DATAPATH`` | A path to folder, where you have JSON data from over WebScraper stored.                 |
+------------------------+-----------------------------------------------------------------------------------------+
| ``FLASK_DEBUG``        | Do you want to run application in debug mode? If yes, set it to 1. If not, set it to 0. |
+------------------------+-----------------------------------------------------------------------------------------+

Now run this to start the server:

.. code-block:: console

    flash run

Alternatively, you can run the server as a module, but you need to define at least ``WEBSERVER_DATAPATH`` environment variable before running:

.. code-block:: console

    python -m scanbrokers


Run with WSGI
-------------

An example of `.wsgi` that was used on my private server. Also this server hosts domain http://scanbrokers.eu


.. code-block:: python

    #!/usr/bin/env python

    import sys
    import site
    import os

    # connect to virtualenv
    site.addsitedir('/var/www/your_domain/__venv__/lib/your_python_version/site-packages')

    sys.path.insert(0, '/var/www/your_domain/')

    # I know, this is not very nice, but it works
    os.environ['WEBSERVER_DATAPATH'] = 'path_to_your_data'

    from scanbrokers import app as application
