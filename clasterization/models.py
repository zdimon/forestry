from django.contrib.gis.db import models
from paintstore.fields import ColorPickerField
from django.utils.html import mark_safe


from datetime import timedelta

from django.utils import timezone
from django.db import models

from durationfield.db.models.fields.duration import DurationField

from datetime import timedelta
#import timedelta

from django.utils.translation import ugettext as _
from django.db.models.signals import post_save, pre_save
from django.utils.timezone import datetime
from config import settings
from django.contrib.gis.db import models
from paintstore.fields import ColorPickerField
from django.utils.html import mark_safe
from fires.models import Fires

# Create your models here.

class DecisionTable(Fires):

#CONDITION ATTRIBUTES

  #  crowning = models.DecimalField(verbose_name=_(u'Square of crowning fire'), max_digits=12, decimal_places=2, null=True)
   # ground = models.DecimalField(verbose_name=_(u'Squre of ground fire'), max_digits=12, decimal_places=2, blank = True, null=True)
   # unforest = models.DecimalField(verbose_name=_(u'Squire which is not belong to forest'), max_digits=12, decimal_places=2, blank = True, null=True)



    type_polygon = models.IntegerField(verbose_name=_(u'Region type'), default=1)
    wood_volume_per_ha = models.DecimalField(verbose_name=_(u'Wood store per 1 ha'), max_digits=12, decimal_places=2, default=0)
#Mateocondition table
    pjc = models.DecimalField(verbose_name=_(u'Meteocondition probability'), max_digits=5, decimal_places=2, default=0)
    pr = models.DecimalField(verbose_name=_(u'Total probability of forest fire beginning'), max_digits=5, decimal_places=2, default=0)

#DECISION ATTRIBUTES
    forestry_man_days = models.DecimalField(verbose_name=_(u'Forestry, man-days'), max_digits=8, decimal_places=4, default=0)
    emergency_man_days = models.DecimalField(verbose_name=_(u'Emergency, man-days'), max_digits=8, decimal_places=4, default=0)
    another_man_days = models.DecimalField(verbose_name=_(u'Other services, man-days'), max_digits=8, decimal_places=4, default=0)
    forestry_fire_eng = models.DecimalField(verbose_name=_(u'Forestry, fire engine, car-shifts'), max_digits=8, decimal_places=4, default=0)

    forestry_another = models.DecimalField(verbose_name=_(u'Forestry, other engines, car-shifts'), max_digits=8, decimal_places=4, default=0)

    emergency_fire_eng = models.DecimalField(verbose_name=_(u'Emergency, fire engines, car-shifts'), max_digits=8, decimal_places=4, default=0)

    emergency_another = models.DecimalField(verbose_name=_(u'Emergency, other engines, car-shifts'), max_digits=8, decimal_places=4, default=0)

    another_fire_eng = models.DecimalField(verbose_name=_(u'Other services, fire engines, car-shifts'), max_digits=8, decimal_places=4, default=0)
    another_another = models.DecimalField(verbose_name=_(u'Other services, other engines car-shifts'), max_digits=8, decimal_places=4, default=0)
    total_fire_eng = models.DecimalField(verbose_name=_(u'Total, fire engines, car-shifts'), max_digits=8, decimal_places=4, default=0)
    total_another = models.DecimalField(verbose_name=_(u'Total, other engines, car-shifts'), max_digits=8, decimal_places=4, default=0)
#Assesment of the situation
    assessment = models.IntegerField(verbose_name=_(u'Assessment of the situation'), default=1)


#GENERALIZED ATTRIBUTES
    ground_square_gen = models.CharField(verbose_name=_(u''), max_length=10, default="zero")
    crowning_square_gen = models.CharField(verbose_name=_(u''), max_length=10, default="zero")
    unforest_square_gen = models.CharField(verbose_name=_(u''), max_length=10, default="zero")
    wood_volume_per_ha_gen = models.CharField(verbose_name=_(u''), max_length=10, default="zero")
    pjc_gen = models.CharField(verbose_name=_(u''), max_length=10, default="zero")
    pr_gen = models.CharField(verbose_name=_(u''), max_length=10, default="zero")
    assessment_gen = models.CharField(verbose_name=_(u''), max_length=10, default="zero")


    def __unicode__(self):
       return str(self.number)

    @property
    def exting_time(self):
        t = self.fires.exting_end - self.fires.exting_degin
        return t






class Contradiction(models.Model):


#GENERALIZED ATTRIBUTES
    #date_begin = models.DateTimeField(verbose_name=_(u'Data and time of fire beginning'), default=False, blank=True, null=True)
    ground_square_gen = models.CharField(verbose_name=_(u''), max_length=10, default="zero")
    crowning_square_gen = models.CharField(verbose_name=_(u''), max_length=10, default="zero")
    unforest_square_gen = models.CharField(verbose_name=_(u''), max_length=10, default="zero")
    wood_volume_per_ha_gen = models.CharField(verbose_name=_(u''), max_length=10, default="zero")
    pjc_gen = models.CharField(verbose_name=_(u''), max_length=10, default="zero")
    pr_gen = models.CharField(verbose_name=_(u''), max_length=10, default="zero")
    assessment_gen = models.CharField(verbose_name=_(u''), max_length=10, default="zero")


    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name=_(u'Contradiction')
        verbose_name_plural=_(u'Contradictions')




