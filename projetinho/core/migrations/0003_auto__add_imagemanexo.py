# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ImagemAnexo'
        db.create_table(u'core_imagemanexo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('noticia', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Noticia'], null=True, blank=True)),
            ('arquivo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'core', ['ImagemAnexo'])


    def backwards(self, orm):
        # Deleting model 'ImagemAnexo'
        db.delete_table(u'core_imagemanexo')


    models = {
        u'core.imagemanexo': {
            'Meta': {'object_name': 'ImagemAnexo'},
            'arquivo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'noticia': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Noticia']", 'null': 'True', 'blank': 'True'})
        },
        u'core.noticia': {
            'Meta': {'object_name': 'Noticia'},
            'autor': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'dt_publicacao': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 4, 8, 0, 0)'}),
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