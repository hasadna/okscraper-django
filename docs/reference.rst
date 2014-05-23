Reference
=========

okscraper_django.management.commands.okscrape
---------------------------------------------

.. py:module:: okscraper_django.management.commands.okscrape

.. py:class:: Command

    okscrape management command - runs a scrpaer
    
    Usage::

        python manage.py okscrape MODULE_NAME [CLASS_NAME] [--dblog] [ARGS]..
        
        MODULE_NAME is a module name inside your django project.
        
        CLASS_NAME is a name of the scraper class inside the module you wish to run. If it is not provided, will look for a MainScraper class to run.
        
        --dblog option should be passed when running from cron - when it is passed the logs will be written to database instead of standard output.
        
        ARGS are extra arguments that will be passed to the scraper
    

okscraper_django.models
-----------------------

.. py:module:: okscraper_django.models

.. py:class:: ScraperRun
    
    Django model for storing scraper runs, each object stores the scraper label, start time and end time.

.. py:class:: ScraperRunLog

    Django model for storing each log line, each line is related to a ScraperRun object.
