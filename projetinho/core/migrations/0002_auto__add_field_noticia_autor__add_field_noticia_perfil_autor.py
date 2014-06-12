# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Noticia.autor'
        db.add_column(u'core_noticia', 'autor',
                      self.gf('django.db.models.fields.CharField')(default='N\xc3\xa3o informado', max_length=50),
                      keep_default=False)

        # Adding field 'Noticia.perfil_autor'
        db.add_column(u'core_noticia', 'perfil_autor',
                      self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Noticia.autor'
        db.delete_column(u'core_noticia', 'autor')

        # Deleting field 'Noticia.perfil_autor'
        db.delete_column(u'core_noticia', 'perfil_autor')


    models = {
        u'core.noticia': {
            'Meta': {'object_name': 'Noticia'},
            'autor': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'dt_publicacao': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 4, 7, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagem': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'link_externo': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'perfil_autor': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.BooleanField', [], {}),
            'texto': ('django.db.models.fields.TextField', [], {}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['core']