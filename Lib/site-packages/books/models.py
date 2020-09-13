from __future__ import unicode_literals

from django.contrib.sites.managers import CurrentSiteManager
from django.contrib.sites.models import Site
from django.db import models
from django.db.models import Q
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

import datetime


@python_2_unicode_compatible
class Editor(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = _('Editor')
        verbose_name_plural = _('Editors')

    def __str__(self):
        return self.name


def cover_filename(instance, filename):
    return "books/%s.jpg" % instance.slug


class BookManager(models.Manager):
    def published(self):
        now = datetime.datetime.now()
        queryset = self.filter(validated=True)
        queryset = queryset.filter(start_publication_on__lte=now)
        q = (
            Q(end_publication_on__isnull=False)
            & Q(end_publication_on__gt=now)
        ) | Q(end_publication_on__isnull=True)
        queryset = queryset.filter(q)
        return queryset


class SiteBookManager(CurrentSiteManager, BookManager):
    pass


@python_2_unicode_compatible
class Book(models.Model):
    site = models.ForeignKey(Site)

    validated = models.BooleanField(default=False)
    start_publication_on = models.DateTimeField(default=datetime.datetime.now)
    end_publication_on = models.DateTimeField(blank=True, null=True)

    lang = models.CharField(max_length=5)
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, db_index=True)
    authors = models.CharField(max_length=200)
    editor = models.ForeignKey(Editor)
    url = models.URLField(blank=True)
    affiliate_url = models.URLField(blank=True)
    isbn_10 = models.CharField(max_length=10, null=True, blank=True)
    isbn_13 = models.CharField(max_length=13, null=True, blank=True)
    asin = models.CharField(max_length=20, null=True, blank=True)
    description = models.TextField()
    cover = models.ImageField(upload_to=cover_filename, blank=True)

    objects = BookManager()
    on_site = SiteBookManager()

    class Meta:
        verbose_name = _('Book')
        verbose_name_plural = _('Books')

    def __str__(self):
        return self.title
