from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(
        max_length=100,
    )
    description = models.TextField(
        null=True,
        blank=True,
    )
    modified = models.DateTimeField(
        auto_now=True
    )
    created = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Product name',
        unique=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        null=True,
        blank=True
    )
    image = models.ForeignKey(
        'images.ProductImage',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
    desc = models.CharField(
        max_length=250,
        default='',
        verbose_name='Description')
    exclusive = models.BooleanField(
        verbose_name='Exclusive',
        default=False)
    is_promo = models.BooleanField(
        verbose_name='Promo',
        default=False)
    in_trend = models.BooleanField(
        verbose_name='In trend',
        default=False)
    modified = models.DateTimeField(
        auto_now=True
    )
    created = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return "%s (%s%s) [in trend: %s, promo: %s, exclusive: %s]" % (self.name, self.desc[:50],
                                                                       '...' if len(self.desc) > 50 else '',
                                                                       self.in_trend,
                                                                       self.is_promo,
                                                                       self.exclusive)
