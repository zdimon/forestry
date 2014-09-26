# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.contrib.gis.db import models

class Forestelement(models.Model):
    type_polygon = models.ForeignKey('TypePolygon')
    rothermel = models.ForeignKey('Rothermel')
    code = models.CharField(max_length=5)
    class Meta:
        managed = False
        db_table = 'forest_element'

class Forestelementtranslation(models.Model):
    forest_element = models.ForeignKey(Forestelement) # Field name made lowercase.
    name = models.CharField(max_length=250)
    lang = models.CharField(max_length=250)
    class Meta:
        managed = False
        db_table = 'forest_element_translation'

class Rothermel(models.Model):
    
    reserve = models.DecimalField(max_digits=8, decimal_places=2)
    unit_area = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    depth = models.DecimalField(max_digits=5, decimal_places=2)
    h = models.DecimalField(max_digits=15, decimal_places=2)
    ro = models.DecimalField(max_digits=8, decimal_places=2)
    mf = models.DecimalField(max_digits=8, decimal_places=2)
    st = models.DecimalField(max_digits=8, decimal_places=2)
    se = models.DecimalField(max_digits=8, decimal_places=2)
    u = models.DecimalField(max_digits=8, decimal_places=2)
    tg = models.DecimalField(max_digits=8, decimal_places=2)
    mx = models.DecimalField(max_digits=8, decimal_places=2)
    class Meta:
        managed = False
        db_table = 'Rothermel'

class Article(models.Model):
    
    user_id = models.IntegerField(blank=True, null=True)
    folder = models.ForeignKey('FolderArticle', blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'article'

class Article2Folder(models.Model):
    folder_id = models.IntegerField()
    article = models.ForeignKey(Article)
    class Meta:
        managed = False
        db_table = 'article2_folder'

class ArticleTranslation(models.Model):

    content = models.TextField(blank=True)
    ititle = models.CharField(max_length=100, blank=True)
    seo_keyword = models.CharField(max_length=1000, blank=True)
    seo_description = models.CharField(max_length=1000, blank=True)
    lang = models.CharField(max_length=2)
    class Meta:
        managed = False
        db_table = 'article_translation'

class AuthGroup(models.Model):

    name = models.CharField(unique=True, max_length=80)
    class Meta:
        managed = False
        db_table = 'auth_group'

class AuthGroupPermissions(models.Model):

    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')
    class Meta:
        managed = False
        db_table = 'auth_group_permissions'

class AuthPermission(models.Model):

    name = models.CharField(max_length=50)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)
    class Meta:
        managed = False
        db_table = 'auth_permission'

class AuthUser(models.Model):

    password = models.CharField(max_length=128)
    last_login = models.DateTimeField()
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'auth_user'

class AuthUserGroups(models.Model):

    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)
    class Meta:
        managed = False
        db_table = 'auth_user_groups'

class AuthUserUserPermissions(models.Model):

    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)
    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'

class Contact(models.Model):

    email = models.CharField(max_length=100, blank=True)
    author = models.CharField(max_length=100, blank=True)
    content = models.CharField(max_length=1000, blank=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'contact'

class DjangoAdminLog(models.Model):

    action_time = models.DateTimeField()
    user = models.ForeignKey(AuthUser)
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    object_id = models.TextField(blank=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    class Meta:
        managed = False
        db_table = 'django_admin_log'

class DjangoContentType(models.Model):

    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    class Meta:
        managed = False
        db_table = 'django_content_type'

class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'django_session'

class DjangoSite(models.Model):

    domain = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    class Meta:
        managed = False
        db_table = 'django_site'

class ExtingCosts(models.Model):

    class Meta:
        managed = False
        db_table = 'exting_costs'

class ExtingCostsTranslation(models.Model):
    exting_costs = models.ForeignKey(ExtingCosts)
    name = models.CharField(max_length=250, blank=True)
    lang = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'exting_costs_translation'

class FireCause(models.Model):

    class Meta:
        managed = False
        db_table = 'fire_cause'

class FireCauseTranslation(models.Model):
    fire_cause = models.ForeignKey(FireCause)
    name = models.CharField(max_length=250, blank=True)
    lang = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'fire_cause_translation'

class FireDamage(models.Model):

    class Meta:
        managed = False
        db_table = 'fire_damage'

class FireDamageTranslation(models.Model):
    name = models.CharField(max_length=250, blank=True)
    lang = models.CharField(max_length=2)
    class Meta:
        managed = False
        db_table = 'fire_damage_translation'

class FireDetection(models.Model):
    pass
    class Meta:
        managed = False
        db_table = 'fire_detection'

class FireDetectionTranslation(models.Model):
    fire_detection = models.ForeignKey(FireDetection)
    name = models.CharField(max_length=250, blank=True)
    lang = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'fire_detection_translation'

class FireLocation(models.Model):

    fire = models.ForeignKey('Fires', blank=True, null=True)
    geo_polygon = models.ForeignKey('GeoPolygon', blank=True, null=True)
    kvartal = models.IntegerField(blank=True, null=True)
    vydel = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'fire_location'

class FireWorked(models.Model):
    pass
    class Meta:
        managed = False
        db_table = 'fire_worked'

class FireWorkedTranslation(models.Model):
    fire_worked_id = models.IntegerField()
    name = models.CharField(max_length=250, blank=True)
    lang = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'fire_worked_translation'

class Fires(models.Model):

    date_begin = models.DateTimeField(blank=True, null=True)
    date_end = models.DateTimeField(blank=True, null=True)
    fire_detection = models.ForeignKey(FireDetection, blank=True, null=True)
    exting_begin = models.DateTimeField(blank=True, null=True)
    exting_end = models.DateTimeField(blank=True, null=True)
    forestry = models.ForeignKey('Forestry', blank=True, null=True)
    square = models.FloatField(blank=True, null=True)
    crowning_square = models.FloatField(blank=True, null=True)
    ground_square = models.FloatField(blank=True, null=True)
    unforest_square = models.FloatField(blank=True, null=True)
    fire_cause = models.ForeignKey(FireCause, blank=True, null=True)
    date_month = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'fires'

class Fires2ExtingCosts(models.Model):
    fire = models.ForeignKey(Fires)
    exting_costs = models.ForeignKey(ExtingCosts)
    sum = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fires2_exting_costs'

class Fires2FireDamage(models.Model):

    fire_id = models.IntegerField(blank=True, null=True)
    fire_damage_id = models.IntegerField(blank=True, null=True)
    sum = models.FloatField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'fires2_fire_damage'

class Fires2FireWorked(models.Model):

    fire_id = models.IntegerField(blank=True, null=True)
    fire_worked_id = models.IntegerField(blank=True, null=True)
    num = models.FloatField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'fires2_fire_worked'

class Fires2GeoPolygon(models.Model):

    fire_id = models.IntegerField(blank=True, null=True)
    geo_polygon_id = models.IntegerField(blank=True, null=True)
    kvartal = models.IntegerField(blank=True, null=True)
    vydel = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'fires2_geo_polygon'

class FolderArticle(models.Model):

    name = models.TextField(blank=True)
    item = models.ForeignKey('self', blank=True, null=True)
    parent_id = models.IntegerField(blank=True, null=True)
    counter = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    lft = models.IntegerField(blank=True, null=True)
    rgt = models.IntegerField(blank=True, null=True)
    level = models.SmallIntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'folder_article'

class ForestElement(models.Model):

    code = models.CharField(max_length=5, blank=True)
    type_polygon = models.ForeignKey('TypePolygon', blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'forest_element'

class ForestElement2GeoPolygon(models.Model):

    geo_polygon = models.ForeignKey('GeoPolygon', blank=True, null=True)
    forest_element = models.ForeignKey(ForestElement, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    height = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    diameter = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    wood_store = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    percent = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'forest_element2_geo_polygon'

class ForestElementTranslation(models.Model):
    forest_element_id = models.IntegerField()
    name = models.CharField(max_length=250, blank=True)
    lang = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'forest_element_translation'

class Forestry(models.Model):

    forestry_group = models.ForeignKey('ForestryGroup', blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'forestry'

class ForestryGroup(models.Model):
    pass
    class Meta:
        managed = False
        db_table = 'forestry_group'

class ForestryGroupTranslation(models.Model):
    forestry_group_id = models.IntegerField()
    name = models.CharField(max_length=250, blank=True)
    lang = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'forestry_group_translation'

class ForestryTranslation(models.Model):
    forestry_id = models.IntegerField()
    name = models.CharField(max_length=250, blank=True)
    lang = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'forestry_translation'

class GeoKvartal(models.Model):

    oid = models.IntegerField(blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)
    forestry = models.ForeignKey(Forestry, blank=True, null=True)
    area = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    area_count = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    perimetr = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    center_zoom = models.BigIntegerField(blank=True, null=True)
    center_lon = models.DecimalField(max_digits=18, decimal_places=7, blank=True, null=True)
    center_lat = models.DecimalField(max_digits=18, decimal_places=7, blank=True, null=True)
    geom = models.MultiPolygonField(srid=900913, blank=True, null=True)
    objects = models.GeoManager()
    class Meta:
        managed = False
        db_table = 'geo_kvartal'

class GeoLine(models.Model):

    ooid = models.IntegerField(blank=True, null=True)
    type = models.ForeignKey('TypeLine', blank=True, null=True)
    name = models.CharField(max_length=1000, blank=True)
    class Meta:
        managed = False
        db_table = 'geo_line'

class GeoPoint(models.Model):

    ooid = models.IntegerField(blank=True, null=True)
    type = models.ForeignKey('TypePoint', blank=True, null=True)
    name = models.CharField(max_length=1000, blank=True)
    perimetr = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'geo_point'

class GeoPolygon(models.Model):

    oid = models.IntegerField(blank=True, null=True)
    type = models.ForeignKey('TypePolygon', blank=True, null=True)
    name = models.CharField(max_length=1000, blank=True)
    area = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    perimetr = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    full_date = models.NullBooleanField()
    is_geom = models.NullBooleanField()
    geom = models.MultiPolygonField(srid=900913, blank=True, null=True)
    vydel = models.IntegerField(blank=True, null=True)
    kvartal = models.IntegerField(blank=True, null=True)
    center_zoom = models.SmallIntegerField(blank=True, null=True)
    center_lon = models.DecimalField(max_digits=18, decimal_places=7, blank=True, null=True)
    center_lat = models.DecimalField(max_digits=18, decimal_places=7, blank=True, null=True)
    kvartal_0 = models.ForeignKey(GeoKvartal, db_column='kvartal_id', blank=True, null=True) # Field renamed because of name conflict.
    fire_able = models.SmallIntegerField(blank=True, null=True)
    forestry = models.ForeignKey(Forestry, blank=True, null=True)
    firedanger = models.DecimalField(max_digits=16, decimal_places=5, blank=True, null=True)
    influence_probability = models.TextField(blank=True) # This field type is a guess.
    firerisk = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    wood_volume_per_ha = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    influence_probabiliti = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    class_damage = models.IntegerField(blank=True, null=True)
    class_risk = models.IntegerField(blank=True, null=True)
    class_risk1 = models.IntegerField(blank=True, null=True)
    class_risk2 = models.IntegerField(blank=True, null=True)
    objects = models.GeoManager()
    class Meta:
        managed = False
        db_table = 'geo_polygon'

class Kvartal(models.Model):
    kvartal = models.CharField(max_length=10, blank=True)
    the_geom = models.MultiPolygonField(blank=True, null=True)
    objects = models.GeoManager()
    class Meta:
        managed = False
        db_table = 'kvartal'

class MapAttributes(models.Model):

    name = models.CharField(max_length=50)
    bound1 = models.DecimalField(max_digits=8, decimal_places=4)
    bound2 = models.DecimalField(max_digits=8, decimal_places=4)
    bound3 = models.DecimalField(max_digits=8, decimal_places=4)
    bound4 = models.DecimalField(max_digits=8, decimal_places=4)
    bound5 = models.DecimalField(max_digits=8, decimal_places=4, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'map_attributes'

class MapDecisionfinal(models.Model):

    fire = models.ForeignKey(Fires)
    crowning_square = models.IntegerField()
    ground_square = models.IntegerField()
    unforest_square = models.IntegerField()
    type_polygon = models.IntegerField()
    wood_volume_per_ha = models.IntegerField()
    pjc = models.IntegerField()
    pr = models.IntegerField()
    forestry_man_days = models.IntegerField()
    emergency_man_days = models.IntegerField()
    another_man_days = models.IntegerField()
    forestry_fire_eng = models.IntegerField()
    forestry_another = models.IntegerField()
    emergency_fire_eng = models.IntegerField()
    emergency_another = models.IntegerField()
    another_fire_eng = models.IntegerField()
    another_another = models.IntegerField()
    total_fire_eng = models.IntegerField()
    total_another = models.IntegerField()
    sit_danger = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'map_decisionfinal'

class MapDecisiontable(models.Model):

    fire = models.ForeignKey(Fires)
    crowning_square = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    ground_square = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    unforest_square = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    type_polygon = models.IntegerField()
    wood_volume_per_ha = models.DecimalField(max_digits=12, decimal_places=2)
    pjc = models.DecimalField(max_digits=5, decimal_places=2)
    pr = models.DecimalField(max_digits=5, decimal_places=2)
    forestry_man_days = models.DecimalField(max_digits=8, decimal_places=4)
    emergency_man_days = models.DecimalField(max_digits=8, decimal_places=4)
    another_man_days = models.DecimalField(max_digits=8, decimal_places=4)
    forestry_fire_eng = models.DecimalField(max_digits=8, decimal_places=4)
    forestry_another = models.DecimalField(max_digits=8, decimal_places=4)
    emergency_fire_eng = models.DecimalField(max_digits=8, decimal_places=4)
    emergency_another = models.DecimalField(max_digits=8, decimal_places=4)
    another_fire_eng = models.DecimalField(max_digits=8, decimal_places=4)
    another_another = models.DecimalField(max_digits=8, decimal_places=4)
    total_fire_eng = models.DecimalField(max_digits=8, decimal_places=4)
    total_another = models.DecimalField(max_digits=8, decimal_places=4)
    assessment = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'map_decisiontable'

class MapExtingcosts(models.Model):

    name = models.CharField(max_length=250)
    class Meta:
        managed = False
        db_table = 'map_extingcosts'

class MapFirecause(models.Model):

    name = models.CharField(max_length=250)
    class Meta:
        managed = False
        db_table = 'map_firecause'

class MapFiredamage(models.Model):

    name = models.CharField(max_length=250)
    class Meta:
        managed = False
        db_table = 'map_firedamage'

class MapFiredetection(models.Model):

    name = models.CharField(max_length=250)
    class Meta:
        managed = False
        db_table = 'map_firedetection'

class MapFirelocation(models.Model):

    fire = models.ForeignKey('MapFires')
    geo_polygon = models.ForeignKey(GeoPolygon)
    kvartal = models.IntegerField()
    vydel = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'map_firelocation'

class MapFires(models.Model):

    fire_detection = models.ForeignKey(MapFiredetection)
    forestry_id = models.ForeignKey(Forestry)
    fire_cause = models.ForeignKey(MapFirecause)
    date_begin = models.DateTimeField()
    date_end = models.DateTimeField()
    exting_begin = models.DateTimeField()
    exting_end = models.DateTimeField()
    square = models.DecimalField(max_digits=5, decimal_places=2)
    crowning_square = models.DecimalField(max_digits=5, decimal_places=2)
    ground_square = models.DecimalField(max_digits=5, decimal_places=2)
    unforest_square = models.DecimalField(max_digits=5, decimal_places=2)
    date_month = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'map_fires'

class MapFires2Extingcosts(models.Model):

    fire = models.ForeignKey(MapFires)
    exting_costs = models.ForeignKey(MapExtingcosts)
    sum = models.DecimalField(max_digits=5, decimal_places=2)
    class Meta:
        managed = False
        db_table = 'map_fires2extingcosts'

class MapFires2Firedamage(models.Model):

    fire = models.ForeignKey(MapFires)
    fire_damage = models.ForeignKey(MapFiredamage)
    sum = models.DecimalField(max_digits=5, decimal_places=2)
    class Meta:
        managed = False
        db_table = 'map_fires2firedamage'

class MapFires2Fireworked(models.Model):

    fire = models.ForeignKey(MapFires)
    fire_worked = models.ForeignKey('MapFireworked')
    num = models.DecimalField(max_digits=5, decimal_places=2)
    class Meta:
        managed = False
        db_table = 'map_fires2fireworked'

class MapFires2Geopolygon(models.Model):

    fire = models.ForeignKey(MapFires)
    geo_polygon = models.ForeignKey(GeoPolygon)
    kvartal = models.IntegerField()
    vydel = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'map_fires2geopolygon'

class MapFiresnumber(models.Model):

    date_month = models.IntegerField()
    number = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'map_firesnumber'

class MapFireworked(models.Model):

    name = models.CharField(max_length=250)
    class Meta:
        managed = False
        db_table = 'map_fireworked'

class MapMeteocondition(models.Model):

    t = models.DecimalField(max_digits=5, decimal_places=2)
    p0 = models.DecimalField(max_digits=5, decimal_places=2)
    p = models.DecimalField(max_digits=5, decimal_places=2)
    pa = models.DecimalField(max_digits=5, decimal_places=2)
    u = models.IntegerField()
    dd = models.CharField(max_length=50)
    ff = models.IntegerField()
    ff10 = models.IntegerField()
    ff3 = models.IntegerField()
    n = models.CharField(max_length=50)
    ww = models.CharField(max_length=100)
    ww1 = models.CharField(max_length=100)
    ww2 = models.CharField(max_length=100)
    tn = models.DecimalField(max_digits=5, decimal_places=2)
    tx = models.DecimalField(max_digits=5, decimal_places=2)
    cl = models.CharField(max_length=100)
    nh = models.CharField(max_length=30)
    h = models.CharField(max_length=20)
    cm = models.CharField(max_length=100)
    ch = models.CharField(max_length=100)
    w = models.DecimalField(max_digits=5, decimal_places=2)
    r = models.DecimalField(max_digits=5, decimal_places=2)
    rrr = models.DecimalField(max_digits=5, decimal_places=2)
    tr = models.IntegerField()
    e = models.CharField(max_length=100)
    tg = models.DecimalField(max_digits=5, decimal_places=2)
    es = models.CharField(max_length=100)
    sss = models.IntegerField()
    rain = models.BooleanField()
    kmp = models.DecimalField(max_digits=5, decimal_places=2)
    pjc = models.DecimalField(max_digits=5, decimal_places=2)
    ap = models.DecimalField(max_digits=5, decimal_places=2)
    pm = models.DecimalField(max_digits=5, decimal_places=2)
    pr = models.DecimalField(max_digits=5, decimal_places=2)
    class Meta:
        managed = False
        db_table = 'map_meteocondition'

class MapParamvalueselect(models.Model):

    param = models.ForeignKey('MapTypeparampolygon')
    name = models.CharField(max_length=250)
    class Meta:
        managed = False
        db_table = 'map_paramvalueselect'

class MapPost(models.Model):

    title = models.CharField(max_length=255)
    datetime = models.DateTimeField()
    content = models.TextField()
    class Meta:
        managed = False
        db_table = 'map_post'

class MapTypeparampolygon(models.Model):

    type_reg = models.ForeignKey('TypePolygon')
    type_value = models.ForeignKey('MapTypevalue')
    name = models.CharField(max_length=250)
    value = models.CharField(max_length=100)
    class Meta:
        managed = False
        db_table = 'map_typeparampolygon'

class MapTypevalue(models.Model):

    name = models.CharField(max_length=250)
    class Meta:
        managed = False
        db_table = 'map_typevalue'

class MapValueparampolygon(models.Model):

    type_reg = models.ForeignKey('TypePolygon')
    region = models.ForeignKey(GeoPolygon)
    type_param = models.ForeignKey(MapTypeparampolygon)
    value = models.CharField(max_length=100)
    class Meta:
        managed = False
        db_table = 'map_valueparampolygon'

class Meteocondition(models.Model):

    curdate = models.DateField(blank=True, null=True)
    t = models.FloatField(blank=True, null=True)
    p0 = models.FloatField(blank=True, null=True)
    p = models.FloatField(blank=True, null=True)
    pa = models.FloatField(blank=True, null=True)
    u = models.SmallIntegerField(blank=True, null=True)
    dd = models.CharField(max_length=50, blank=True)
    ff = models.SmallIntegerField(blank=True, null=True)
    ff10 = models.SmallIntegerField(blank=True, null=True)
    ff3 = models.SmallIntegerField(blank=True, null=True)
    n = models.CharField(max_length=50, blank=True)
    ww = models.CharField(max_length=100, blank=True)
    w1 = models.CharField(max_length=100, blank=True)
    w2 = models.CharField(max_length=100, blank=True)
    tn = models.FloatField(blank=True, null=True)
    tx = models.FloatField(blank=True, null=True)
    cl = models.CharField(max_length=100, blank=True)
    nh = models.CharField(max_length=30, blank=True)
    h = models.CharField(max_length=20, blank=True)
    cm = models.CharField(max_length=100, blank=True)
    ch = models.CharField(max_length=100, blank=True)
    w = models.FloatField(blank=True, null=True)
    r = models.FloatField(blank=True, null=True)
    rrr = models.FloatField(blank=True, null=True)
    tr = models.SmallIntegerField(blank=True, null=True)
    e = models.CharField(max_length=100, blank=True)
    tg = models.FloatField(blank=True, null=True)
    es = models.CharField(max_length=100, blank=True)
    sss = models.SmallIntegerField(blank=True, null=True)
    rain = models.NullBooleanField()
    kmp = models.FloatField(blank=True, null=True)
    pjc = models.FloatField(blank=True, null=True)
    ap = models.FloatField(blank=True, null=True)
    pm = models.FloatField(blank=True, null=True)
    pr = models.FloatField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'meteocondition'

class Page(models.Model):

    alias = models.CharField(max_length=100)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'page'

class PageTranslation(models.Model):

    content = models.TextField(blank=True)
    seo_title = models.CharField(max_length=100)
    seo_keyword = models.CharField(max_length=1000)
    seo_description = models.CharField(max_length=1000)
    lang = models.CharField(max_length=2)
    class Meta:
        managed = False
        db_table = 'page_translation'

class ParamValueSelect(models.Model):

    param = models.ForeignKey('TypeParamPolygon', blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'param_value_select'

class ParamValueSelectTranslation(models.Model):

    name = models.CharField(max_length=250, blank=True)
    lang = models.CharField(max_length=2)
    class Meta:
        managed = False
        db_table = 'param_value_select_translation'

class Profile(models.Model):

    user = models.ForeignKey('SfGuardUser', blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    country = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=100, blank=True)
    icq = models.CharField(max_length=100, blank=True)
    skype = models.CharField(max_length=100, blank=True)
    avatar = models.CharField(max_length=100, blank=True)
    is_developer = models.NullBooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'profile'

class ProfileTranslation(models.Model):

    about_me = models.TextField(blank=True)
    profession = models.CharField(max_length=1000, blank=True)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    lang = models.CharField(max_length=2)
    class Meta:
        managed = False
        db_table = 'profile_translation'

class Projects(models.Model):

    name = models.CharField(max_length=100, blank=True)
    item = models.ForeignKey('self', blank=True, null=True)
    parent_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    lft = models.IntegerField(blank=True, null=True)
    rgt = models.IntegerField(blank=True, null=True)
    level = models.SmallIntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'projects'

class ProjectsTranslation(models.Model):

    seo_title = models.CharField(max_length=100, blank=True)
    seo_keyword = models.CharField(max_length=1000, blank=True)
    seo_description = models.CharField(max_length=1000, blank=True)
    content = models.TextField(blank=True)
    lang = models.CharField(max_length=2)
    class Meta:
        managed = False
        db_table = 'projects_translation'

class RothermelTranslation(models.Model):
    veget_type = models.CharField(max_length=250)
    lang = models.CharField(max_length=2)
    rothermel_id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'rothermel_translation'

class SfGuardGroup(models.Model):

    name = models.CharField(unique=True, max_length=255, blank=True)
    description = models.CharField(max_length=1000, blank=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'sf_guard_group'

class SfGuardGroupPermission(models.Model):
    group = models.ForeignKey(SfGuardGroup)
    permission = models.ForeignKey('SfGuardPermission')
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'sf_guard_group_permission'

class SfGuardPermission(models.Model):

    name = models.CharField(unique=True, max_length=255, blank=True)
    description = models.CharField(max_length=1000, blank=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'sf_guard_permission'

class SfGuardRememberKey(models.Model):

    user = models.ForeignKey('SfGuardUser', blank=True, null=True)
    remember_key = models.CharField(max_length=32, blank=True)
    ip_address = models.CharField(max_length=50)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'sf_guard_remember_key'

class SfGuardUser(models.Model):

    username = models.CharField(unique=True, max_length=128)
    algorithm = models.CharField(max_length=128)
    salt = models.CharField(max_length=128, blank=True)
    password = models.CharField(max_length=128, blank=True)
    is_active = models.NullBooleanField()
    is_super_admin = models.NullBooleanField()
    money = models.IntegerField(blank=True, null=True)
    can_upload = models.IntegerField(blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'sf_guard_user'

class SfGuardUserGroup(models.Model):
    user = models.ForeignKey(SfGuardUser)
    group = models.ForeignKey(SfGuardGroup)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'sf_guard_user_group'

class SfGuardUserPermission(models.Model):
    user = models.ForeignKey(SfGuardUser)
    permission = models.ForeignKey(SfGuardPermission)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'sf_guard_user_permission'

class SouthMigrationhistory(models.Model):

    app_name = models.CharField(max_length=255)
    migration = models.CharField(max_length=255)
    applied = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'south_migrationhistory'

class Translate(models.Model):

    target = models.CharField(max_length=1000)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'translate'

class TranslateTranslation(models.Model):

    source = models.CharField(max_length=1000, blank=True)
    lang = models.CharField(max_length=2)
    class Meta:
        managed = False
        db_table = 'translate_translation'

class TypeLine(models.Model):

    name = models.CharField(max_length=250, blank=True)
    class Meta:
        managed = False
        db_table = 'type_line'

class TypeParamLine(models.Model):

    name = models.CharField(max_length=1000, blank=True)
    type_reg = models.ForeignKey(TypeLine, blank=True, null=True)
    type_param = models.CharField(max_length=50, blank=True)
    class Meta:
        managed = False
        db_table = 'type_param_line'

class TypeParamPoint(models.Model):

    name = models.CharField(max_length=250, blank=True)
    type_reg = models.ForeignKey('TypePoint', blank=True, null=True)
    value = models.CharField(max_length=100, blank=True)
    type_param = models.CharField(max_length=50, blank=True)
    class Meta:
        managed = False
        db_table = 'type_param_point'

class TypeParamPolygon(models.Model):

    type_reg = models.ForeignKey('TypePolygon', blank=True, null=True)
    value = models.CharField(max_length=100, blank=True)
    type_value = models.ForeignKey('TypeValue', blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'type_param_polygon'

class TypeParamPolygonTranslation(models.Model):
    type_param_polygon = models.ForeignKey(TypeParamPolygon)
    name = models.CharField(max_length=250, blank=True)
    lang = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'type_param_polygon_translation'

class TypePoint(models.Model):
    
    name = models.CharField(max_length=250, blank=True)
    class Meta:
        managed = False
        db_table = 'type_point'

class TypePolygon(models.Model):
    
    is_pub = models.NullBooleanField()
    fill_color = models.CharField(max_length=7, blank=True)
    border_color = models.CharField(max_length=7, blank=True)
    class Meta:
        managed = False
        db_table = 'type_polygon'

class TypePolygonTranslation(models.Model):
    type_polygon = models.ForeignKey(TypePolygon)
    name = models.CharField(max_length=250, blank=True)
    lang = models.CharField(max_length=2)
    
    class Meta:
        managed = False
        db_table = 'type_polygon_translation'

class TypeValue(models.Model):
    
    name = models.CharField(max_length=250, blank=True)
    class Meta:
        managed = False
        db_table = 'type_value'

class UserSetting(models.Model):
    
    user = models.ForeignKey(SfGuardUser, blank=True, null=True)
    folder_photo = models.IntegerField(blank=True, null=True)
    folder_video = models.IntegerField(blank=True, null=True)
    folder_article = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'user_setting'

class ValueParamLine(models.Model):
    
    value = models.CharField(max_length=100, blank=True)
    type_reg = models.ForeignKey(TypeLine, blank=True, null=True)
    region = models.ForeignKey(GeoLine, blank=True, null=True)
    type_param = models.ForeignKey(TypeParamLine, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'value_param_line'

class ValueParamPoint(models.Model):
    
    value = models.CharField(max_length=100, blank=True)
    type_reg = models.ForeignKey(TypePoint, blank=True, null=True)
    region = models.ForeignKey(GeoPoint, blank=True, null=True)
    type_param = models.ForeignKey(TypeParamPoint, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'value_param_point'

class ValueParamPolygon(models.Model):
    
    value = models.CharField(max_length=250, blank=True)
    type_reg = models.ForeignKey(TypePolygon, blank=True, null=True)
    region = models.ForeignKey(GeoPolygon, blank=True, null=True)
    type_param = models.ForeignKey(TypeParamPolygon, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'value_param_polygon'

class ValueParamPolygonTranslation(models.Model):

    lang = models.CharField(max_length=2)
    class Meta:
        managed = False
        db_table = 'value_param_polygon_translation'

