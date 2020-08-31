from django.utils.translation import ugettext as _
from django.db import models

DOUGH_CHOICES = (
    ('тонкое', 'тонкое'),
    ('традиционное', 'традиционное'),
)

SIZE_CHOICES = (
    ('26 см', '26 см'),
    ('30 см', '30 см'),
    ('40 см', '40 см'),
)


class Catalog(models.Model):
    image = models.ImageField(_('photo'), upload_to='photo', blank=True, null=True)
    name = models.CharField(_('name'), max_length=150, blank=True, null=True)
    dough = models.CharField(_('dough'), choices=DOUGH_CHOICES, default='FREE', max_length=30)
    size = models.CharField(_('size'), choices=SIZE_CHOICES, default='FREE', max_length=30)
    price= models.DecimalField(_('price'), max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Catalog'