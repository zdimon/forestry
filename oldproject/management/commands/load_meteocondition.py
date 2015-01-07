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
        from django.utils import timezone
        from oldproject.models import Meteocondition as Oldmeteocondition
        #from oldproject.models import FireDetectionTranslation as Oldfiredetectiontranslation
        from fires.models import Meteocondition
        logger.info("Start transfering.....")
        logger.info("Clear table.....")
        Meteocondition.objects.all().delete()
        for fg in Oldmeteocondition.objects.all():
           # try:
                #cd = timezone.make_aware(fg.curdate, timezone.get_current_timezone())




                o = Meteocondition()
                #o.old_id = fg.id
                o.curdate = fg.curdate
                if fg.t:
                    o.t = fg.t
                else:
                    o.t = 0
                if fg.p0:
                    o.p0 = fg.p0
                else:
                    o.p0 = 0
                if fg.p:
                    o.p = fg.p
                else:
                    o.p = 0
                if fg.pa:
                    o.pa = fg.pa
                else:
                    o.pa = 0
                if fg.u:
                    o.u = fg.u
                else:
                    o.u = 0
                if fg.dd:
                    o.dd = fg.dd
                else:
                    o.dd = 0
                if fg.ff:
                    o.ff = fg.ff
                else:
                    o.ff = 0
                if fg.ff10:
                    o.ff10 = fg.ff10
                else:
                    o.ff10 = 0
                if fg.ff3:
                    o.ff3 = fg.ff3
                else:
                    o.ff3 = 0

                if fg.n:
                    o.n = fg.n
                else:
                    o.n = 0
                if fg.ww:
                    o.ww = fg.ww
                else:
                    o.ww = 0
                if fg.w1:
                    o.w1 = fg.w1
                else:
                    o.w1 = 0
                if fg.w2:
                    o.w2 = fg.w2
                else:
                    o.w2 = 0
                if fg.tn:
                    o.tn = fg.tn
                else:
                    o.tn = 0
                if fg.tx:
                    o.tx = fg.tx
                else:
                    o.tx = 0
                if fg.cl:
                    o.cl = fg.cl
                else:
                    o.cl = 0
                if fg.nh:
                    o.nh = fg.nh
                else:
                    o.nh = 0
                if fg.h:
                    o.h = fg.h
                else:
                    o.h = 0
                if fg.cm:
                    o.cm = fg.cm
                else:
                    o.cm = 0
                if fg.ch:
                    o.ch = fg.ch
                else:
                    o.ch = 0
                if fg.w:
                    o.w = fg.w
                else:
                    o.w = 0
                if fg.r:
                    o.r = fg.r
                else:
                    o.r = 0
                if fg.rrr:
                    o.rrr = fg.rrr
                else:
                    o.rrr = 0
                if fg.tr:
                    o.tr = fg.tr
                else:
                    o.tr = 0
                if fg.e:
                    o.e = fg.e
                else:
                    o.e = 0
                if fg.tg:
                    o.tg = fg.tg
                else:
                    o.tg = 0
                if fg.es:
                    o.es = fg.es
                else:
                    o.es = 0
                if fg.sss:
                    o.sss = fg.sss
                else:
                    o.sss = 0
                if fg.rain:
                    o.rain = fg.rain
                else:
                    o.rain = 0
                if fg.kmp:
                    o.kmp = fg.kmp
                else:
                    o.kmp = 0
                if fg.pjc:
                    o.pjc = fg.pjc
                else:
                    o.pjc = 0
                if fg.ap:
                    o.ap = fg.ap
                else:
                    o.ap = 0
                if fg.pm:
                    o.pm = fg.pm
                else:
                    o.pm = 0
                if fg.pr:
                    o.pr = fg.pr
                else:
                    o.pr = 0
                #o.pa=1
                #o.u =1
                #o.ff = 1
                #o.ff10 = 1
                #o.tn = 1
                #o.tx = 1
                #o.w = 1
                #o.tr =1
                #o.tg = 1
                #o.sss = 1
                #o.rain = 1
                #o.kmp = 1
                #o.pjc = 1
                #o.ap = 1
                #o.pm = 1
                #o.pr = 1
                o.save()
                print o.id
            #except Exception, err:
             #S   print Exception, err
            #logger.info("Finish transfering.....")
