from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Image name', unique=True)
    image = models.ImageField(upload_to='products/', verbose_name='Image', unique=True)
    desc = models.CharField(max_length=250, default='', verbose_name='Description')
    exclusive = models.BooleanField(verbose_name='Exclusive', default=False)
    is_promo = models.BooleanField(verbose_name='Promo', default=False)
    in_trend = models.BooleanField(verbose_name='In trend', default=False)

    def __str__(self):
        return "%s (%s%s)" % (self.name, self.desc[:50], '...' if len(self.desc) > 50 else '')


