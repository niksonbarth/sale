from django.db import models
from django.core.urlresolvers import reverse
from decimal import Decimal
from django.core.validators import MinValueValidator


class Category(models.Model):

    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Identificador', max_length=100)
    image = models.ImageField(upload_to='catalog/category/images', verbose_name='Imagem', null=True, blank=True)

    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('catalog:category', kwargs={'slug': self.slug})

class Product(models.Model):

    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Identificador', max_length=100)
    category = models.ForeignKey('catalog.Category', verbose_name='Categoria')
    description = models.TextField('Descrição', blank=True)
    barcode = models.BigIntegerField('Código de barras', blank=False)

    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('catalog:product', kwargs={'slug': self.slug})

class SuperMarket(models.Model):

    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Identificador', max_length=100)
    city = models.CharField('Cidade', max_length=255)
    image = models.ImageField(upload_to='catalog/supermarket/images', verbose_name='Imagem', null=True, blank=True)

    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    class Meta:
        verbose_name = 'Super Mercado'
        verbose_name_plural = 'Super Mercados'
        ordering = ['name']

    def __str__(self):
        return self.name

class Ad(models.Model):

    product = models.ForeignKey('catalog.Product', verbose_name='Produto')
    superMarket = models.ForeignKey('catalog.SuperMarket', verbose_name='Super Mercado')
    price = models.DecimalField('Preço', decimal_places=2, max_digits=8, validators=[MinValueValidator(Decimal('0.01'))])
    unit = models.ForeignKey('core.Unit', verbose_name='Unidade', null=False, blank=False)

    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    class Meta:
        verbose_name = 'Anúncio'
        verbose_name_plural = 'Anúncios'

    def __str__(self):
        return self.product.name