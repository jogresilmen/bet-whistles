# -*- coding: utf-8
"""
Modelo de datos de la app main
"""
# Django Libraries
from django.db import models
from django.utils.translation import gettext_lazy as _


class Sex(models.Model):
    name = models.CharField(max_length=10, verbose_name=_("Name"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Sex")
