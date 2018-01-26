from django.db import models

class Unit(models.Model):

    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Identificador', max_length=100)
    acronym = models.CharField('Sigla', max_length=10)


    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    class Meta:
        verbose_name = 'Unidade'
        verbose_name_plural = 'Unidade'
        ordering = ['name']

    def __str__(self):
        return self.name
