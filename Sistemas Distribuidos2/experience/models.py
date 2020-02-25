from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User


# Create your models here.

class Experience(models.Model):
    user = models.ForeignKey(User, related_name='experience', on_delete=models.CASCADE)
    title = models.CharField(verbose_name="Título", max_length=200)
    content = RichTextField(verbose_name="Contenido")
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    image = models.ImageField(upload_to='experience/%Y/%m/%d', blank=True, verbose_name='Imagen')

    class Meta:
        verbose_name = "experienca"
        verbose_name_plural = "experiencias"
        ordering = ['-created']

    def __str__(self):
        return self.title

    def total_likes(self):
        return self.likes.count()
