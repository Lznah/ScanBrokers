************
Installation
************

Eager to get started? This page gives information how to install ScanBrokers.

Python Version
==============

We recommend using the Python version 3.9.0 for ScanBrokers

You can download ScanBrokers webserver from Github.

.. code-block:: console

    git clone https://github.com/Lznah/ScanBrokers

Dependencies
============

These distribution will be installed, when installing ScanBrokers.

* Flask_: A well-known Python framework to create websites.
* Unidecode_: A library for removing accents from text.

.. _Flask: https://flask.palletsprojects.com
.. _Unidecode: https://pypi.python.org/pypi/Unidecode

Extra Dependencies
==================

They do not install unless you want to run tests or generate documentation.

* PyTest_: A framework to test Python code.
* Sphinx_: An automatical tool for generation documentation.

.. _PyTest: https://www.sphinx-doc.org/en/master/
.. _Sphinx: https://www.sphinx-doc.org/en/master/


Obtaining data webscraper
=========================

Also, you might need a webscraper, that is not a part of this repository and it is in separate repository. You have to decide where to have it in your filesystem. 

You can download our Selenium Scraper here:

.. code-block:: console

    git clone https://github.com/Lznah/SrealityAdresarScraper


Or if you want to just try webserver without installing webscraper, you can just download files below. Do not forget to set appropriate ``WEBSERVER_DATAPATH`` environment variable that navigates to folder, where you store this file. The folder should not contain any other JSON file.
