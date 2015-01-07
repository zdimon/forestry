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
        from oldproject.models import ExtingCosts as Oldextingcosts
        from oldproject.models import ExtingCostsTranslation as Oldextingcoststranslation
        from fires.models import ExtingCosts
        logger.info("Start transfering.....")
        logger.info("Clear table.....")
        ExtingCosts.objects.all().delete()
        for fg in Oldextingcosts.objects.all():
            o = ExtingCosts()
            o.old_id = fg.id
            for ot in Oldextingcoststranslation.objects.filter(exting_costs=fg):
                print 'qq1'
                if ot.lang=='ru':
                    o.name=ot.name
                    o.name_ru=ot.name
                if ot.lang=='en':
                    o.name_en = ot.name
                if ot.lang=='uk':
                    o.name_uk = ot.name
            o.save()
        logger.info("Finish transfering.....")
