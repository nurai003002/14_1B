from django.db import models

class Gallery(models.Model):
    image = models.ImageField(
        upload_to='gallery_image/',
        verbose_name='Фотография'
    )

    class Meta:
        verbose_name = 'Галерея'
        verbose_name_plural = 'Галерея'
        