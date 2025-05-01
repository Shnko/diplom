from django.db import models
from django.utils.translation import gettext_lazy as _

# Модель ребёнка
class Child(models.Model):
    first_name = models.CharField(null=False, blank=False, max_length=100, verbose_name="Имя")
    last_name = models.CharField(null=False, blank=False, max_length=100, verbose_name="Фамилия")
    patronymic = models.CharField(null=False, blank=False, max_length=100, verbose_name="Отчество")
    date_of_birth = models.DateField(null=False, blank=False, verbose_name="Дата рождения")
    class Meta:
        verbose_name = _("child")
        verbose_name_plural = _("children")
    def __str__(self):
        return f"{self.id} - {self.first_name} {self.last_name} [{self.date_of_birth}]"