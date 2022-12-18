import os.path

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Category(models.Model):
    #it has foreignkey to itself (self), when we have category and sub-category (the ones with null=Trus are parent category)
    #this model is onetoone with Foreginkey (Foreginkey=to one specific record an manytomany =to some specific record)
    parent = models.ForeignKey('self', verbose_name=_('parent'), blank=True, null=True, on_delete=models.CASCADE)
    title = models.CharField(_('title'), max_length=50)
    description = models.TextField(_('description'), blank=True)
    avatar = models.ImageField(_('avatar'), blank=True, upload_to='categories/')
    is_enable = models.BooleanField(_('is enable'), default=True)
    created_time = models.DateTimeField(_('created time'), auto_now_add=True)
    updated_time = models.DateTimeField(_('updated time'), auto_now=True)

#oneoone = only one specific record

    class Meta:
        db_table = 'categories'
        verbose_name = _('Category')
        verbose_name_plural = _('categories')



class Product(models.Model):
    title = models.CharField(_('title'), max_length=50)
    description = models.TextField(_('description'), blank=True)
    avatar = models.ImageField(_('avatar'), blank=True, upload_to='products/')
    #save the avatar in this directory: products/
    is_enable = models.BooleanField(_('is enable'), default=True)
    categories = models.ManyToManyField('Category', verbose_name=_('categories'), blank=True)
    # blank=True because there might be no category
    #here we make this model manytomany (one product cab belong more than one category) with category model
    created_time = models.DateTimeField(_('created time'), auto_now_add=True)
    updated_time = models.DateTimeField(_('updated time'), auto_now=True)

    class Meta:
        db_table = 'products'
        verbose_name = _('Product')
        verbose_name_plural = _('products')



# for example each series can have many files, so better to have a separate class for files
#files will be uploaded here and will be connected to Product
class File(models.Model):
    #should be connected to only one product (so it is foreignkey to Product model). one or some files can belong to one product
    #each product could have one or more than one product
    # each file can be connected to each file one by one
    product = models.ForeignKey('Product', verbose_name=_('product'), blank=True, null=True, on_delete=models.CASCADE)
    title = models.CharField(_('title'), max_length=50)
    file = models.FileField(_('file'), upload_to='files/%Y/%m/%d')
    #all the files for the same day will be uploaded to separate sub-directory with specific date
    is_enable = models.BooleanField(_('is enable'), default=True)
    created_time = models.DateTimeField(_('created time'), auto_now_add=True)
    updated_time = models.DateTimeField(_('updated time'), auto_now=True)

    class Meta:
        db_table = 'files'
        verbose_name = _('file')
        verbose_name_plural = _('files')


#all the files will be uploaded to one of these 3 folders (products, categories or files)
#but these folders should also be in a directory ==>
#go to settings.py and do the following:
#1- import os (on top of script)
#2- add this at the end --> #Media Files
# 3- add this at the end to put the files here --> MEDIA_ROOT = os.path.join((BASE_DIR, 'media/'))
# 4- add this at the end to show the files here --> MEDIA_URL = 'media/'
