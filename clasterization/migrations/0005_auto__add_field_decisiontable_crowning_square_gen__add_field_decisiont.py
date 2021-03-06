# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'DecisionTable.crowning_square_gen'
        db.add_column(u'clasterization_decisiontable', 'crowning_square_gen',
                      self.gf('django.db.models.fields.CharField')(default='zero', max_length=10),
                      keep_default=False)

        # Adding field 'DecisionTable.unforest_square_gen'
        db.add_column(u'clasterization_decisiontable', 'unforest_square_gen',
                      self.gf('django.db.models.fields.CharField')(default='zero', max_length=10),
                      keep_default=False)

        # Adding field 'DecisionTable.wood_volume_per_ha_gen'
        db.add_column(u'clasterization_decisiontable', 'wood_volume_per_ha_gen',
                      self.gf('django.db.models.fields.CharField')(default='zero', max_length=10),
                      keep_default=False)

        # Adding field 'DecisionTable.pjc_gen'
        db.add_column(u'clasterization_decisiontable', 'pjc_gen',
                      self.gf('django.db.models.fields.CharField')(default='zero', max_length=10),
                      keep_default=False)

        # Adding field 'DecisionTable.pr_gen'
        db.add_column(u'clasterization_decisiontable', 'pr_gen',
                      self.gf('django.db.models.fields.CharField')(default='zero', max_length=10),
                      keep_default=False)

        # Adding field 'DecisionTable.assessment_gen'
        db.add_column(u'clasterization_decisiontable', 'assessment_gen',
                      self.gf('django.db.models.fields.CharField')(default='zero', max_length=10),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'DecisionTable.crowning_square_gen'
        db.delete_column(u'clasterization_decisiontable', 'crowning_square_gen')

        # Deleting field 'DecisionTable.unforest_square_gen'
        db.delete_column(u'clasterization_decisiontable', 'unforest_square_gen')

        # Deleting field 'DecisionTable.wood_volume_per_ha_gen'
        db.delete_column(u'clasterization_decisiontable', 'wood_volume_per_ha_gen')

        # Deleting field 'DecisionTable.pjc_gen'
        db.delete_column(u'clasterization_decisiontable', 'pjc_gen')

        # Deleting field 'DecisionTable.pr_gen'
        db.delete_column(u'clasterization_decisiontable', 'pr_gen')

        # Deleting field 'DecisionTable.assessment_gen'
        db.delete_column(u'clasterization_decisiontable', 'assessment_gen')


    models = {
        u'clasterization.decisiontable': {
            'Meta': {'ordering': "['date_begin']", 'object_name': 'DecisionTable', '_ormbases': [u'fires.Fires']},
            'another_another': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '8', 'decimal_places': '4'}),
            'another_fire_eng': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '8', 'decimal_places': '4'}),
            'another_man_days': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '8', 'decimal_places': '4'}),
            'assessment': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'assessment_gen': ('django.db.models.fields.CharField', [], {'default': "'zero'", 'max_length': '10'}),
            'crowning_square_gen': ('django.db.models.fields.CharField', [], {'default': "'zero'", 'max_length': '10'}),
            'emergency_another': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '8', 'decimal_places': '4'}),
            'emergency_fire_eng': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '8', 'decimal_places': '4'}),
            'emergency_man_days': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '8', 'decimal_places': '4'}),
            u'fires_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['fires.Fires']", 'unique': 'True', 'primary_key': 'True'}),
            'forestry_another': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '8', 'decimal_places': '4'}),
            'forestry_fire_eng': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '8', 'decimal_places': '4'}),
            'forestry_man_days': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '8', 'decimal_places': '4'}),
            'ground_square_gen': ('django.db.models.fields.CharField', [], {'default': "'zero'", 'max_length': '10'}),
            'pjc': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '5', 'decimal_places': '2'}),
            'pjc_gen': ('django.db.models.fields.CharField', [], {'default': "'zero'", 'max_length': '10'}),
            'pr': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '5', 'decimal_places': '2'}),
            'pr_gen': ('django.db.models.fields.CharField', [], {'default': "'zero'", 'max_length': '10'}),
            'total_another': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '8', 'decimal_places': '4'}),
            'total_fire_eng': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '8', 'decimal_places': '4'}),
            'type_polygon': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'unforest_square_gen': ('django.db.models.fields.CharField', [], {'default': "'zero'", 'max_length': '10'}),
            'wood_volume_per_ha': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '12', 'decimal_places': '2'}),
            'wood_volume_per_ha_gen': ('django.db.models.fields.CharField', [], {'default': "'zero'", 'max_length': '10'})
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