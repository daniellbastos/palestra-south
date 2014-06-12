# -*- coding: utf-8 -*-
from django.db import models
from django.template.defaultfilters import slugify
from datetime import datetime

class Autor(models.Model):
    nome = models.CharField(u'Nome', max_length=50)
    perfil = models.URLField(u'Link Perfil do Autor', blank=True, null=True)
        
    def __unicode__(self):
        return self.nome


class Noticia(models.Model):
    autores = models.ManyToManyField(Autor, verbose_name=u'Autor(es)')
    titulo = models.CharField(u'Título', max_length=200)
    slug = models.SlugField(u'Slug', max_length=200, editable=False, blank=True, null=True)
    texto = models.TextField(u'Texto')
    dt_publicacao = models.DateTimeField(u'Data de Publicação', default=datetime.now())
    imagem = models.ImageField(upload_to='noticia', verbose_name=u'Imagem de Capa')
    link_externo = models.URLField(u'Link Externo', blank=True, null=True)
    status = models.BooleanField(u'Habilitado')

    def __unicode__(self):
        return self.titulo

    def save(self):
        self.slug = slugify(self.titulo)
        return super(self.__class__, self).save()


class ImagemAnexo(models.Model):
    noticia = models.ForeignKey(Noticia, on_delete=models.CASCADE, blank=True, null=True)
    arquivo = models.ImageField(upload_to='imagem', verbose_name=u'Imagem')

    def __unicode__(self):
        return self.arquivo