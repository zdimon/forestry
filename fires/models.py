# -*- coding: utf-8 -*-
from datetime import timedelta
from django.utils import timezone
from django.db import models
from django.utils.translation import ugettext as _
from django.db.models.signals import post_save, pre_save
from django.utils.timezone import datetime
from config import settings
from django.contrib.gis.db import models
from paintstore.fields import ColorPickerField
from django.utils.html import mark_safe



class Rothermel(models.Model):
    old_id = models.IntegerField(verbose_name=_(u'Old id'), default=0, db_index=True)
    veget_type_id = models.IntegerField(verbose_name=_(u'Vegetation type id'), default=0)
    veget_type = models.CharField(verbose_name=_(u'Vegetation name'), max_length=250,default=False)
    reserve = models.DecimalField(verbose_name=_(u'The reserve of forest fuel, kg/m2'), max_digits=8, decimal_places=2, default=0)
    unit_area = models.DecimalField(verbose_name=_(u'Unit area, m-1'), max_digits=5, decimal_places=2, default=0)
    depth = models.DecimalField(verbose_name=_(u'Layer depth, m'), max_digits=5, decimal_places=2, default=0)
    h = models.DecimalField(verbose_name=_(u'Heating value of dry fuel, Joul/kg'), max_digits=8, decimal_places=2, default=0)
    ro = models.DecimalField(verbose_name=_(u'Density of dry fuel, kg/m3'), max_digits=8, decimal_places=2, default=0)
    mf = models.DecimalField(verbose_name=_(u'Moisture content'), max_digits=8, decimal_places=2, default=0)
    st = models.DecimalField(verbose_name=_(u'The mass part of minerals in forest fuel'), max_digits=8, decimal_places=2, default=0)
    se = models.DecimalField(verbose_name=_(u'Diameter'), max_digits=8, decimal_places=2, default=0)
    u = models.DecimalField(verbose_name=_(u'Wind speed, m/sec'), max_digits=8, decimal_places=2, default=0)
    tg = models.DecimalField(verbose_name=_(u'The slope of the terrain (tangent)'), max_digits=8, decimal_places=2, default=0)
    mx = models.DecimalField(verbose_name=_(u'Critical moisture content'), max_digits=8, decimal_places=2, default=0)
    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name=_(u'Parameters of Rothermel model')
        verbose_name_plural=_(u'Parameters of Rothermel model')


class FireDetection(models.Model):
    old_id = models.IntegerField(verbose_name=_(u'Old id'), default=0, db_index=True)
    name = models.CharField(verbose_name=_(u'Who detected fire'), max_length=250)
    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name =_(u'Who detected fire')
        verbose_name_plural =_(u'Who detected fire')


class FireCause(models.Model):
    old_id = models.IntegerField(verbose_name=_(u'Old id'), default=0, db_index=True)
    name = models.CharField(verbose_name=_(u'Fire cause'), max_length=250,default=False)
    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name=_(u'Fire cause')
        verbose_name_plural=_(u'Fire causes')


class ExtingCosts(models.Model):
    old_id = models.IntegerField(verbose_name=_(u'Old id'), default=0, db_index=True)
    name = models.CharField(verbose_name=_(u'Type of extinguishing costs'), max_length=250,default=False)
    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name=_(u'Types of extinguishing costs')
        verbose_name_plural=_(u'Types of extinguishing costs')


class FireDamage(models.Model):
    old_id = models.IntegerField(verbose_name=_(u'Old id'), default=0, db_index=True)
    name = models.CharField(verbose_name=_(u'Fire damage'), max_length=250,default=False)
    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name=_(u'Fire damage')
        verbose_name_plural=_(u'Fire damage')


class FireWorked(models.Model):
    old_id = models.IntegerField(verbose_name=_(u'Old id'), default=0, db_index=True)
    name = models.CharField(verbose_name=_(u'Worked on fire'), max_length=250,default=False)
    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name=_(u'Worked on fire')
        verbose_name_plural=_(u'Worked on fire')


class Fires(models.Model):
    old_id = models.IntegerField(verbose_name=_(u'Old id'), default=0, db_index=True)
    from forestry.models import Forestry, ForestryGroup
    fire_detection = models.ForeignKey(FireDetection, verbose_name=_(u'Who detected'), default=False, blank=True, null=True)
    forestry_group = models.ForeignKey(ForestryGroup, verbose_name=_(u'Forestry group'), db_column='forestry_group_id', default=1)
    forestry = models.ForeignKey(Forestry, verbose_name=_(u'Forestry'), db_column='forestry_id', default=False, blank=True, null=True)
    fire_cause = models.ForeignKey(FireCause, verbose_name=_(u'Firecause'), default=False, blank=True, null=True)
    date_begin = models.DateTimeField(verbose_name=_(u'Data and time of fire beginning'), default=False, blank=True, null=True)
    date_end = models.DateTimeField(verbose_name=_(u'Date and time of fire ending'), default=False, blank=True, null=True)
    exting_begin = models.DateTimeField(verbose_name=_(u'Date and time of beginning of extinguishing'), default=False, blank=True, null=True)
    exting_end = models.DateTimeField(verbose_name=_(u'Date and time of the ending of extinguishing'), default=False, blank=True, null=True)
    square = models.DecimalField(verbose_name=_(u'Total burnt area'), max_digits=5, decimal_places=2, default=0, blank=True, null=True)
    crowning_square = models.DecimalField(verbose_name=_(u'The area of crown fire'), max_digits=5, decimal_places=2, default=0, blank=True, null=True)
    ground_square = models.DecimalField(verbose_name=_(u'The area of ground fire'), max_digits=5, decimal_places=2, default=0, blank=True, null=True)
    unforest_square = models.DecimalField(verbose_name=_(u'Non forest area'), max_digits=5, decimal_places=2, default=0, blank=True, null=True)
    date_month = models.IntegerField(verbose_name=_(u'The day of month'), default=0, blank=True, null=True)
    def __unicode__(self):
        return unicode(self.date_begin) + u'  ' + unicode(self.forestry_id) or u''
    class Meta:
        verbose_name=_(u'Fire')
        verbose_name_plural=_(u'Fires')
        ordering = ['date_begin']


class Fires2ExtingCosts(models.Model):
    old_id = models.IntegerField(verbose_name=_(u'Old id'), default=0, db_index=True)
    fire = models.ForeignKey('Fires', verbose_name=_(u'Fire'), default=False, blank=True, null=True)
    exting_costs = models.ForeignKey('ExtingCosts', verbose_name=_(u'Extinguishing costs'), default=False, blank=True, null=True)
    sum = models.DecimalField(verbose_name=_(u'The amount of costs'), max_digits=10, decimal_places=2, default=0, blank=True, null=True)
    def __unicode__(self):
        return unicode(self.fire) + u':  ' + unicode(self.exting_costs) + u' - ' + unicode(self.sum) or u''



class Fires2FireDamage(models.Model):
    old_id = models.IntegerField(verbose_name=_(u'Old id'), default=0, db_index=True)
    fire = models.ForeignKey('Fires', verbose_name=_(u'Fire'), default=False)
    fire_damage = models.ForeignKey('FireDamage', verbose_name=_(u'Fire damage'), default=False)
    sum = models.DecimalField(verbose_name=_(u'The amount of damage'), max_digits=10, decimal_places=2, default=0)
    def __unicode__(self):
        return unicode(self.fire) + u':  ' + unicode(self.fire_damage) + u' - ' + unicode(self.sum) or u''



class Fires2FireWorked(models.Model):
    old_id = models.IntegerField(verbose_name=_(u'Old id'), default=0, db_index=True)
    fire = models.ForeignKey('Fires', verbose_name=_(u'Fire'), default=False)
    fire_worked = models.ForeignKey('FireWorked', verbose_name=_(u'Worked on fire'), default=False)
    num = models.DecimalField(verbose_name=_(u'The amount'), max_digits=5, decimal_places=2, default=0)
    def __unicode__(self):
        return unicode(self.fire) + u':  ' + unicode(self.fire_worked) + u' - ' + unicode(self.num) or u''



class Fires2GeoPolygon(models.Model):
    old_id = models.IntegerField(verbose_name=_(u'Old id'), default=0, db_index=True)
    from forestry.models import GeoPolygon
    fire = models.ForeignKey('Fires', default=False)
    geo_polygon = models.ForeignKey(GeoPolygon, default=False)
    kvartal = models.IntegerField(verbose_name=_(u'The number of block'), default=0)
    vydel = models.IntegerField(verbose_name=_(u'The number of region'), default=0)
    def __unicode__(self):
     #   return unicode(self.fire) + u':  ' + unicode(self.geo_polygon) + u' - ' + unicode(self.kvartal) or u''
        return unicode(self.fire) or u''



class Meteocondition(models.Model):
    old_id = models.IntegerField(verbose_name=_(u'Old id'), default=0, db_index=True)
    curdate = models.DateField(verbose_name=_(u'Date'))
    t = models.DecimalField(verbose_name=_(u'Temperature'), max_digits=5, decimal_places=2, default=0)
    p0 = models.DecimalField(verbose_name=_(u'Atmospheric pressure at the level of station (mm))'), max_digits=5, decimal_places=2, default=0, blank = True)
    p = models.DecimalField(verbose_name=_(u''), max_digits=5, decimal_places=2, blank = True)
    pa = models.DecimalField(verbose_name=_(u''), max_digits=5, decimal_places=2,blank = True)
    u = models.IntegerField(verbose_name=_(u''), blank = True)
    dd = models.CharField(verbose_name=_(u''), max_length=150, blank = True)
    ff = models.IntegerField(verbose_name=_(u''), blank = True)
    ff10 = models.IntegerField(verbose_name=_(u''), blank = True)
    ff3 = models.IntegerField(verbose_name=_(u''),blank = True, null = True)
    n = models.CharField(verbose_name=_(u''), max_length=150, blank = True)
    ww = models.CharField(verbose_name=_(u''), max_length=100, blank = True)
    w1 = models.CharField(verbose_name=_(u''), max_length=100, blank = True)
    w2 = models.CharField(verbose_name=_(u''), max_length=100, blank = True)
    tn = models.DecimalField(verbose_name=_(u'min temperature during lost period (12 howers))'), max_digits=5, decimal_places=2, blank = True)
    tx = models.DecimalField(verbose_name=_(u'max temperature during lost period (12 howers))'), max_digits=5, decimal_places=2,blank = True)
    cl = models.CharField(max_length=100, blank = True)
    nh = models.CharField(max_length=30, blank = True)
    h = models.CharField(max_length=20, blank = True)
    cm = models.CharField(max_length=100, blank = True)
    ch = models.CharField(max_length=100, blank = True)
    w = models.DecimalField(max_digits=5, decimal_places=2, blank = True)

    r = models.DecimalField(verbose_name=_(u'The due point temperature'), max_digits=5, decimal_places=2, default=0)
    rrr = models.DecimalField(verbose_name=_(u'The amount of precipitation (mm)'), max_digits=5, decimal_places=2, default=0)
    tr = models.IntegerField(verbose_name=_(u'The period of time during which such amount of precipitation is accumulated'), blank = True)
    e = models.CharField(max_length=100, blank = True)
    tg = models.DecimalField(max_digits=5, decimal_places=2, blank = True)
    es = models.CharField(max_length=100, blank = True)
    sss = models.IntegerField(verbose_name=_(u'the height of snow (sm)'), blank = True)
    rain = models.BooleanField(verbose_name=_(u'Rain'), blank = True)
    # Рассчетные показатели
    kmp = models.DecimalField(verbose_name=_(u'Complex meteorological index'), max_digits=20, decimal_places=10, blank = True)
    pjc = models.DecimalField(verbose_name=_(u'Probability because of meteoconditions'), max_digits=20, decimal_places=10, blank = True)
    ap = models.DecimalField(verbose_name=_(u'Probability because of anthropogenic cause'), max_digits=20, decimal_places=10, blank = True)
    pm = models.DecimalField(verbose_name=_(u'Probability because of thunderstorm activity'), max_digits=20, decimal_places=10, blank = True)
    pr = models.DecimalField(verbose_name=_(u'Total probability of forest fire beginning'), max_digits=20, decimal_places=10, blank = True)
    def __unicode__(self):
     #   return unicode(self.fire) + u':  ' + unicode(self.geo_polygon) + u' - ' + unicode(self.kvartal) or u''
        return unicode(self.curdate) or u''
    class Meta:
        verbose_name=_(u'Meteocondition')
        verbose_name_plural=_(u'Meteoconditions')

