from django.db import models
from django.utils.translation import ugettext_lazy as _


class AbstractModel(models.Model):
    """
    Абстрактная модель содержащая одинаковые поля для всех моделей,
    которые будут наследоваться от этой модели
    """
    id = models.AutoField(_("ID"), primary_key=True, editable=False)
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)

    class Meta:
        abstract = True