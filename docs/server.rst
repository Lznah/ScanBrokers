**********
Web Server
**********
Web server is a Flask Application. There are few reasons, why I decided to use Flask. Firstly, Flask was shown at NI-PYT course at FIT CTU. Secondly, Flask Webserver does not require to stick with MVC framework.

Also, there is a database initialized at the start of the webserver.


Database reload
---------------

Unfortunately, database reloading for already running webserver was meant to be done every day by a custom command line script for Flask. This functionality could be implemented later. Database reloading is simply done by restarting server. 

Database is restarted every day at specific hour. This is done by crontask.

.. automodule:: scanbrokers.server
   :members:
   :undoc-members:
   :show-inheritance: