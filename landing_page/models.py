# -*- coding: utf-8 -*-
from django.db import models
# from stroykapremont.settings import MEDIA_URL

from tinymce.models import HTMLField
from adminsortable.models import SortableMixin

from filer.fields.image import FilerImageField

# IMAGE_STR = 'изображение'
# IMAGE_HEIGHT_LIST = 120
# IMAGE_HEIGHT_DETAIL = 250
#
#
# def helper_get_image_html(url, height, alt):
#     alt = str(alt)
#     height = str(height)
#     if not str(url):
#         return '<span style="color:red">%s еще не загружено</span>' % IMAGE_STR
#     s_height = ' height="%s"' % height if height else ''
#     s_alt = ' alt="%s"' % alt if alt else ''
#     full_url = '%s%s' % (MEDIA_URL, url)
#     result = '<a href="%s"><img src="%s" %s %s/></a>' % (full_url, full_url, s_height, s_alt)
#     return result


class Projects(SortableMixin):
    order = models.PositiveIntegerField(default=0, editable=False, db_index=True)
    title = models.CharField(max_length=30, unique=True, verbose_name='уникальное название')
    slug = models.SlugField(unique=True)    # need for js frontend
    # desc = HTMLField(verbose_name='описание')

    # image = FilerFileField(upload_to='project_cats/', blank=True, verbose_name=IMAGE_STR)
    # image = FilerImageField(null=True, blank=True, related_name="category")

    class Meta(object):
        verbose_name = 'Категория проекта'
        verbose_name_plural = 'Категории проектов'
        ordering = ['order', ]

    # def admin_list_image(self):
    #     return helper_get_image_html(self.image, IMAGE_HEIGHT_LIST, self.title)
    #
    # admin_list_image.allow_tags = True
    # admin_list_image.short_description = IMAGE_STR
    #
    # def admin_detail_image(self):
    #     return helper_get_image_html(self.image, IMAGE_HEIGHT_DETAIL, self.title)
    #
    # admin_detail_image.allow_tags = True
    # admin_detail_image.short_description = IMAGE_STR

    def __str__(self):
        return self.title


class Project_Images(SortableMixin):
    order = models.PositiveIntegerField(default=0, editable=False, db_index=True)
    category = models.ForeignKey(Projects, on_delete=models.CASCADE, default=0, verbose_name='категория')
    title = models.CharField(max_length=30, verbose_name='название', default='')
    # image = FilerFileField(upload_to='project_details/', blank=True, verbose_name=IMAGE_STR)
    image = FilerImageField(null=True, blank=True, related_name="project")

    class Meta(object):
        verbose_name = 'Детализация проекта'
        verbose_name_plural = 'Детализация проектов'
        # ordering = ['category', 'order']
        ordering = ['order', ]

    # def admin_list_image(self):
    #     return helper_get_image_html(self.image, IMAGE_HEIGHT_LIST, '')
    #
    # admin_list_image.allow_tags = True
    # admin_list_image.short_description = IMAGE_STR
    #
    # def admin_detail_image(self):
    #     return helper_get_image_html(self.image, IMAGE_HEIGHT_DETAIL, '')
    #
    # admin_detail_image.allow_tags = True
    # admin_detail_image.short_description = IMAGE_STR

    # def __str__(self):
    #     return ''


class SiteSettings(models.Model):
    site_name = models.TextField(max_length=50)
    site_description = models.TextField(max_length=100)

    contact_streetAddress = models.TextField(max_length=200)
    contact_addressLocality = models.TextField(max_length=200)
    contact_addressRegion = models.TextField(max_length=200)

    contact_telephone = models.TextField(max_length=30)

    contact_hours = HTMLField()



