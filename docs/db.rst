Dabatabase
---------------------

This project uses an in-memory database object to store data, that are later served in requests to Flask server.

This database is basically an aggregation of JSON objects, that are stored in a folder in filesystem defined by ``WEBSERVER_DATAPATH`` environment variable. These JSON files are loaded into this database object and later used in a series of preprocessing algorithms. 

This preprocessing here is meant as preprocessing of queries lately requested in Flask routes. I decided for this query preprocessing, because the server updates data only once in a day and this can be done during night. Because of that, the response of webserver to a query is super fast.

Database is reloaded by CRON task every day at hour defined by ``HOUR_DATABASE_RELOAD`` environment variable.

.. automodule:: scanbrokers.db
   :members:
   :undoc-members:
   :show-inheritance:
