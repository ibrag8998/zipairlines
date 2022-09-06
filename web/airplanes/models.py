from django.db import models
from django.utils.translation import gettext_lazy as _


class Airplane(models.Model):
    id: int = models.PositiveIntegerField(_("id"), primary_key=True)
    passengers: int = models.PositiveIntegerField(_("passengers amount"))

    class Meta:
        verbose_name = _("airplane")
        verbose_name_plural = _("airplanes")
