# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Noticia'
        db.create_table(u'core_noticia', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=200, null=True, blank=True)),
            ('texto', self.gf('django.db.models.fields.TextField')()),
            ('dt_publicacao', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 4, 4, 0, 0))),
            ('imagem', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('link_externo', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('status', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal(u'core', ['Noticia'])


    def backwards(self, orm):
        # Deleting model 'Noticia'
        db.delete_table(u'core_noticia')


    models = {
        u'core.noticia': {
            'Meta': {'object_name': 'Noticia'},
            'dt_publicacao': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 4, 4, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagem': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'link_externo': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.BooleanField', [], {}),
            'texto': ('django.db.models.fields.TextField', [], {}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['core']