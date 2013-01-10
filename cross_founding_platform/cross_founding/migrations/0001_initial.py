# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Project'
        db.create_table('cross_founding_project', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal('cross_founding', ['Project'])

        # Adding model 'Backer'
        db.create_table('cross_founding_backer', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('cross_founding', ['Backer'])

        # Adding model 'User'
        db.create_table('cross_founding_user', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('full_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('e_mail', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('date_of_birth', self.gf('django.db.models.fields.DateField')()),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('project_owner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cross_founding.Project'])),
            ('backer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cross_founding.Backer'])),
        ))
        db.send_create_signal('cross_founding', ['User'])


    def backwards(self, orm):
        # Deleting model 'Project'
        db.delete_table('cross_founding_project')

        # Deleting model 'Backer'
        db.delete_table('cross_founding_backer')

        # Deleting model 'User'
        db.delete_table('cross_founding_user')


    models = {
        'cross_founding.backer': {
            'Meta': {'object_name': 'Backer'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'cross_founding.project': {
            'Meta': {'object_name': 'Project'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'cross_founding.user': {
            'Meta': {'object_name': 'User'},
            'backer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cross_founding.Backer']"}),
            'date_of_birth': ('django.db.models.fields.DateField', [], {}),
            'e_mail': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'full_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'project_owner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cross_founding.Project']"}),
            'user_name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['cross_founding']