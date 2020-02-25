from django.db import models


# Create your models here.

class Promotion(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Nombre')
    link = models.URLField(default=" ", verbose_name='URL')
    slug = models.SlugField(max_length=100, db_index=True)
    description = models.TextField(blank=True, verbose_name='Descripción')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='promotions/%Y/%m/%d', blank=True, verbose_name='Imagen')

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
        verbose_name = 'promocion'
        verbose_name_plural = 'promociones'

    def __str__(self):
        return self.name
