from django.db import models
from django.utils.translation import gettext_lazy as _

class Child(models.Model):
    """
    Модель ребёнка
    """
    first_name = models.CharField(null=False, blank=False, max_length=100, verbose_name=_("first name"))
    last_name = models.CharField(null=False, blank=False, max_length=100, verbose_name=_("last name"))
    patronymic = models.CharField(null=False, blank=False, max_length=100, verbose_name=_("patronymic"))
    date_of_birth = models.DateField(null=False, verbose_name=_("date of birth"))
    class Meta:
        verbose_name = _("child")
        verbose_name_plural = _("children")
    def __str__(self):
        return f"{self.id} - {self.first_name} {self.last_name} [{self.date_of_birth}]"

class ChildAdmission(models.Model):
    """
    Поступление
    """
    child = models.ForeignKey(Child, on_delete=models.CASCADE)
    date_of_admission = models.DateField(null=False, verbose_name=_("date of admission"))

    class Meta:
        verbose_name = _("child admission")
        verbose_name_plural = _("child admissions")
