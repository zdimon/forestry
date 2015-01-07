# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'DecisionTable.crowning_square'
        db.delete_column(u'clasterization_decisiontable', 'crowning_square')

        # Deleting field 'DecisionTable.unforest_square'
        db.delete_column(u'clasterization_decisiontable', 'unforest_square')

        # Deleting field 'DecisionTable.id'
        db.delete_column(u'clasterization_decisiontable', u'id')

        # Deleting field 'DecisionTable.exting_time'
        db.delete_column(u'clasterization_decisiontable', 'exting_time')

        # Deleting field 'DecisionTable.fire'
        db.delete_column(u'clasterization_decisiontable', 'fire_id')

        # Deleting field 'DecisionTable.ground_square'
        db.delete_column(u'clasterization_decisiontable', 'ground_square')

        # Adding field 'DecisionTable.fires_ptr'
        db.add_column(u'clasterization_decisiontable', u'fires_ptr',
                      self.gf('django.db.models.fields.related.OneToOneField')(default=1, to=orm['fires.Fires'], unique=True, primary_key=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'DecisionTable.crowning_square'
        db.add_column(u'clasterization_decisiontable', 'crowning_square',
                      self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=2),
                      keep_default=False)

        # Adding field 'DecisionTable.unforest_square'
        db.add_column(u'clasterization_decisiontable', 'unforest_square',
                      self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=2, blank=True),
                      keep_default=False)

        # Adding field 'DecisionTable.id'
        db.add_column(u'clasterization_decisiontable', u'id',
                      self.gf('django.db.models.fields.AutoField')(default=1, primary_key=True),
                      keep_default=False)

        # Adding field 'DecisionTable.exting_time'
        db.add_column(u'clasterization_decisiontable', 'exting_time',
                      self.gf('django.db.models.fields.DateTimeField')(default=False, null=True, blank=True),
                      keep_default=False)

        # Adding field 'DecisionTable.fire'
        db.add_column(u'clasterization_decisiontable', 'fire',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['fires.Fires']),
                      keep_default=False)

        # Adding field 'DecisionTable.ground_square'
        db.add_column(u'clasterization_decisiontable', 'ground_square',
                      self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=2, blank=True),
                      keep_default=False)

        # Deleting field 'DecisionTable.fires_ptr'
        db.delete_column(u'clasterization_decisiontable', u'fires_ptr_id')


    models = {
        u'clasterization.decisiontable': {
            'Meta': {'ordering': "['date_begin']", 'object_name': 'DecisionTable', '_ormbases': [u'fires.Fires']},
            'another_another': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '8', 'decimal_places': '4'}),
            'another_fire_eng': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '8', 'decimal_places': '4'}),
            'another_man_days': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '8', 'decimal_places': '4'}),
            'assessment': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'emergency_another': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '8', 'decimal_places': '4'}),
            'emergency_fire_eng': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '8', 'decimal_places': '4'}),
            'emergency_man_days': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '8', 'decimal_places': '4'}),
            u'fires_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['fires.Fires']", 'unique': 'True', 'primary_key': 'True'}),
            'forestry_another': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '8', 'decimal_places': '4'}),
            'forestry_fire_eng': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '8', 'decimal_places': '4'}),
            'forestry_man_days': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '8', 'decimal_places': '4'}),
            'pjc': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '5', 'decimal_places': '2'}),
            'pr': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '5', 'decimal_places': '2'}),
            'total_another': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '8', 'decimal_places': '4'}),
            'total_fire_eng': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '8', 'decimal_places': '4'}),
            'type_polygon': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'wood_volume_per_ha': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '12', 'decimal_places': '2'})
        },
        u'fires.firecause': {
            'Meta': {'object_name': 'FireCause'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': 'False', 'max_length': '250'}),
            'name_en': ('django.db.models.fields.CharField', [], {'default': 'False', 'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'name_ru': ('django.db.models.fields.CharField', [], {'default': 'False', 'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'name_uk': ('django.db.models.fields.CharField', [], {'default': 'False', 'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'old_id': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'})
        },
        u'fires.firedetection': {
            'Meta': {'object_name': 'FireDetection'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'name_ru': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'name_uk': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'old_id': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'})
        },
        u'fires.fires': {
            'Meta': {'ordering': "['date_begin']", 'object_name': 'Fires'},
            'crowning_square': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            'date_begin': ('django.db.models.fields.DateTimeField', [], {'default': 'False', 'null': 'True', 'blank': 'True'}),
            'date_end': ('django.db.models.fields.DateTimeField', [], {'default': 'False', 'null': 'True', 'blank': 'True'}),
            'date_month': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'exting_begin': ('django.db.models.fields.DateTimeField', [], {'default': 'False', 'null': 'True', 'blank': 'True'}),
            'exting_end': ('django.db.models.fields.DateTimeField', [], {'default': 'False', 'null': 'True', 'blank': 'True'}),
            'fire_cause': ('django.db.models.fields.related.ForeignKey', [], {'default': 'False', 'to': u"orm['fires.FireCause']", 'null': 'True', 'blank': 'True'}),
            'fire_detection': ('django.db.models.fields.related.ForeignKey', [], {'default': 'False', 'to': u"orm['fires.FireDetection']", 'null': 'True', 'blank': 'True'}),
            'forestry': ('django.db.models.fields.related.ForeignKey', [], {'default': 'False', 'to': u"orm['forestry.Forestry']", 'null': 'True', 'db_column': "'forestry_id'", 'blank': 'True'}),
            'forestry_group': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['forestry.ForestryGroup']", 'db_column': "'forestry_group_id'"}),
            'ground_square': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'old_id': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'}),
            'square': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            'unforest_square': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'})
        },
        u'forestry.forestry': {
            'Meta': {'object_name': 'Forestry'},
            'forestry_group': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['forestry.ForestryGroup']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'name_ru': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'name_uk': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'old_id': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'})
        },
        u'forestry.forestrygroup': {
            'Meta': {'object_name': 'ForestryGroup'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_ru': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_uk': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'old_id': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'})
        }
    }

    complete_apps = ['clasterization']