okscraper-django management commands
====================================

okscrape
--------

The main management commands which can be used to run scrapers.

Provides the following services:

* Easy running of scrapers from the command line (e.g. using cron)
* Stores log of runs into a dedicated model (ScraperRun)
* The model is visible in the admin and can be used to track errors
