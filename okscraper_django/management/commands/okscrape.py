# encoding: utf-8

from django.core.management.base import BaseCommand
from okscraper.cli.runner import Runner as OkscraperCliRunner
import logging
from optparse import make_option
from okscraper_django.models import ScraperRun, ScraperRunLog
from datetime import datetime
import traceback

class DblogHandler(logging.Handler):

    def __init__(self, scraperrun, *args, **kwargs):
        self._scraperrun = scraperrun
        super(DblogHandler, self).__init__(*args, **kwargs)

    def emit(self, record):
        runlog = ScraperRunLog(text=record.getMessage(), status=record.levelname)
        runlog.save()
        self._scraperrun.logs.add(runlog)
        self._scraperrun.save()

class Command(BaseCommand):

    args = 'module [class] [arg]..'

    option_list = BaseCommand.option_list + (
        make_option(
            '--dblog', action='store_true', dest="dblog", default=False,
            help='log run details to db for monitoring of scraper jobs'
        ),
    )

    def _define_logger(self, verbosity, dblog, scraperrun):
        logger = logging.getLogger()
        ch = logging.StreamHandler()
        if verbosity == '1':
            level = logging.WARN
        elif verbosity == '2':
            level = logging.INFO
        elif verbosity == '3':
            level = logging.DEBUG
        else:
            level = logging.ERROR
        ch.setLevel(level)
        logger.addHandler(ch)
        if dblog:
            handler = DblogHandler(scraperrun)
            handler.setLevel(logging.INFO)
            logger.addHandler(handler)

    def handle(self, *args, **options):
        dblog = options.get('dblog', False)
        scraperrun = None
        if dblog:
            scraper_label = args[0]
            if len(args)>1 and args[1] is not None: scraper_label=scraper_label+'.'+args[1]
            scraperrun = ScraperRun(scraper_label=scraper_label)
            scraperrun.save()
        self._define_logger(
            options.get('verbosity', '1'), dblog,
            scraperrun
        )
        runner = OkscraperCliRunner(
            args[0],
            args[1] if len(args)>1 else None,
            *args[2:] if len(args)>2 else []
        )
        if dblog:
            try:
                runner.run()
            except:
                print traceback.format_exc()
                runlog = ScraperRunLog(text=traceback.format_exc(), status='EXCEPTION')
                runlog.save()
                scraperrun.logs.add(runlog)
            scraperrun.end_time = datetime.now()
            scraperrun.save()
        else:
            runner.run()
