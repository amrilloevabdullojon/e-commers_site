from datetime import datetime

from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _
import pytz
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

UserModel = get_user_model()


class CategoryModel(models.Model):
    title = models.CharField(max_length=20, verbose_name=_('title'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')


class BrandModel(models.Model):
    title = models.CharField(max_length=20, verbose_name=_('title'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('brand')
        verbose_name_plural = _('brands')


class ColorModel(models.Model):
    title = models.CharField(max_length=25, verbose_name=_('title'),null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('color')
        verbose_name_plural = _('colors')


class ProductModel(models.Model):
    title = models.CharField(max_length=50, verbose_name=_('title'))
    image = models.ImageField(upload_to='products', verbose_name=_('image'))
    price = models.FloatField(verbose_name=_('price'))
    discount = models.PositiveIntegerField(default=0, verbose_name=_('discount'))
    real_price = models.FloatField(verbose_name=_('real price'), default=0)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))
    short_description = models.TextField(verbose_name=_('short_description'))
    long_description = RichTextUploadingField(verbose_name=_('long_description'))
    color = models.ManyToManyField(ColorModel, related_name='products', verbose_name=_('color'))
    category = models.ForeignKey(
        CategoryModel,
        on_delete=models.PROTECT,
        related_name='products',
        verbose_name=_('category')
    )
    brand = models.ForeignKey(
        BrandModel,
        on_delete=models.PROTECT,
        related_name='products',
        verbose_name=_('brand')
    )

    wishlist = models.ManyToManyField(UserModel,
                                      related_name='wishlist',
                                      verbose_name=_('wishlist')
                                      )

    def is_discount(self):
        return self.discount != 0

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('product')
        verbose_name_plural = _('products')


class ProductImageModel(models.Model):
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name='images',
                                verbose_name=_('product'))
    image = models.ImageField(upload_to='products', verbose_name=_('image'))

    class Meta:
        verbose_name = _('product image')
        verbose_name_plural = _('product images')
