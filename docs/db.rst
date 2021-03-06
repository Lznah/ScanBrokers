**********
Dabatabase
**********
This project uses an in-memory database object to store data, that are later served in requests to Flask server.

This database is basically an aggregation of JSON objects, that are stored in a folder in filesystem defined by ``WEBSERVER_DATAPATH`` environment variable. These JSON files are loaded into this database object and later used in a series of preprocessing algorithms. 

This preprocessing here is meant as preprocessing of queries lately requested in Flask routes. I decided for this query preprocessing, because the server updates data only once in a day and this can be done during night. Because of that, the response of webserver to a query is super fast.

Unfortunately, I have discoved, that this does not work as I expected. The application context works a bit different and there is a new context with each request, not with the start of the application. Because of that, there is currently no need to set up cron task for restarting the server.

Database Object Structure
-------------------------

This is just a simple example of the database object structure.

.. code-block:: javascript

   {
      'json_files': [
         '12345.json': JSON object,
         '67890.json': JSON object,
         // ...
      ],
      'agents': JSON data object
      'another preprocess data': JSON data object
      // ...

   }


Database is supposted to be reloaded by CRON task every day at hour defined by ``HOUR_DATABASE_RELOAD`` environment variable. However, I was not able to implement a custom script command for already running Flask application. Therefore, reloading of the database is now done by a simple restart of the server in user defined CRON job.

.. automodule:: scanbrokers.db
   :members:
   :undoc-members:
