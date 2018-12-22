from django.db import models


class Img(models.Model):
    name = models.CharField(max_length=150)

    @property
    def url(self):
        return self.value.url

    def __str__(self):
        return self.name


class ProductImage(Img):
    value = models.ImageField(
        upload_to='products/',
        verbose_name='Image',
        unique=True
    )


class Avatar(Img):
    value = models.ImageField(
        upload_to='avatars/',
        verbose_name='Avatar',
        unique=True
    )
