# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Autor'
        db.create_table(u'core_autor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('perfil', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal(u'core', ['Autor'])

        # Deleting field 'Noticia.autor'
        db.delete_column(u'core_noticia', 'autor')

        # Deleting field 'Noticia.perfil_autor'
        db.delete_column(u'core_noticia', 'perfil_autor')

        # Adding M2M table for field autores on 'Noticia'
        m2m_table_name = db.shorten_name(u'core_noticia_autores')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('noticia', models.ForeignKey(orm[u'core.noticia'], null=False)),
            ('autor', models.ForeignKey(orm[u'core.autor'], null=False))
        ))
        db.create_unique(m2m_table_name, ['noticia_id', 'autor_id'])


    def backwards(self, orm):
        # Deleting model 'Autor'
        db.delete_table(u'core_autor')

        # Adding field 'Noticia.autor'
        db.add_column(u'core_noticia', 'autor',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50),
                      keep_default=False)

        # Adding field 'Noticia.perfil_autor'
        db.add_column(u'core_noticia', 'perfil_autor',
                      self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Removing M2M table for field autores on 'Noticia'
        db.delete_table(db.shorten_name(u'core_noticia_autores'))


    models = {
        u'core.autor': {
            'Meta': {'object_name': 'Autor'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'perfil': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'core.imagemanexo': {
            'Meta': {'object_name': 'ImagemAnexo'},
            'arquivo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'noticia': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Noticia']", 'null': 'True', 'blank': 'True'})
        },
        u'core.noticia': {
            'Meta': {'object_name': 'Noticia'},
            'autores': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['core.Autor']", 'symmetrical': 'False'}),
            'dt_publicacao': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 4, 10, 0, 0)'}),
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