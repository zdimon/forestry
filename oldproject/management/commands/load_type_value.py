# -*- coding: utf-8 -*-

import logging
logging.basicConfig()
from optparse import make_option

from django.core.management.base import BaseCommand
from django.utils.importlib import import_module
from django.utils.translation import ugettext_lazy as _


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class Command(BaseCommand):


    def handle(self, *args, **options):
        from oldproject.models import TypeValue as Oldtype
        from forestry.models import TypeValue
        logger.info("Start transfering.....")
        logger.info("Clear table.....")
        TypeValue.objects.all().delete()
        for fg in Oldtype.objects.all():
            o = TypeValue()
            o.name = fg.name
            o.save()
        logger.info("Finish transfering.....")
