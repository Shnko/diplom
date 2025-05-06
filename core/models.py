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
    date_of_admission = models.DateField(null=False, verbose_name="дата поступления")

    class Meta:
        verbose_name = _("child admission")
        verbose_name_plural = _("child admissions")

class ChildDeath(models.Model):
    """
    Смерти детей
    """
    child = models.OneToOneField(Child, primary_key = True, on_delete=models.CASCADE)
    date_of_death = models.DateField(null=False, verbose_name="дата смерти")

    class Meta:
        verbose_name = _("child death")

class Employee(models.Model):
    """
    Сотрудники
    """
    last_name = models.CharField(null=False, blank=False, max_length=100, verbose_name=_("last name"))
    first_name = models.CharField(null=False, blank=False, max_length=100, verbose_name=_("first name"))
    patronymic = models.CharField(null=False, blank=False, max_length=100, verbose_name=_("patronymic"))

    class Meta:
        verbose_name = _("employee")

    def __str__(self):
        return f"{self.id} - {self.last_name} {self.first_name} {self.patronymic}"


class Employment(models.Model):
    """
    Трудоустройства
    """
    class PositionCategory(models.TextChoices):
        DOCTOR = "1", "Врач"
        LINEAR_MEDICAL_STAFF = "2", "Средний медицинский персонал"
        JUNIOR_MEDICAL_STAFF = "3", "Младший медицинский персонал"
        PHARMACIST = "4", "Провизор"
        APOTHECARY = "5", "Фармацевт"
        TEACHER = "6", "Педагогический персонал"
        NON_MEDICAL_STAFF = "7", "Специалисты с высшим не медицинским образованием"
        OTHERS = "8", "Прочий персонал"

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    rate = models.DecimalField(null=False, blank=False, max_digits=4, decimal_places=2, verbose_name=_("working rate"))
    position_name = models.CharField(null=False, blank=False, max_length=100, verbose_name="Должности")
    report_category = models.CharField(choices=PositionCategory)
    start_date_of_employment = models.DateField(null=False, verbose_name=_("start date of employment"))
    end_date_of_employment = models.DateField(null=True, blank=True, verbose_name=_("end date of employment"))

    class Meta:
        verbose_name = "трудоустройство"


class ChildReturned(models.Model):
    """
    Дети, взятые родителями
    """
    child = models.ForeignKey(Child, on_delete=models.CASCADE)
    date_of_adoption = models.DateField(null=False, verbose_name="Дата взятия родителями")
    class Meta:
        verbose_name = "ребёнок, взятый родителями"

class ChildParent(models.Model):
    """
    Родители детей
    """
    returned = models.ForeignKey(ChildReturned, on_delete=models.CASCADE)
    last_name = models.CharField(null=False, blank=False, max_length=100, verbose_name=_("last name"))
    first_name = models.CharField(null=False, blank=False, max_length=100, verbose_name=_("first name"))
    patronymic = models.CharField(null=False, blank=False, max_length=100, verbose_name=_("patronymic"))

    class Meta:
        verbose_name = "родители"

    def __str__(self):
        return f"{self.id} - {self.last_name} {self.first_name} {self.patronymic}"


class ChildCare(models.Model):
    """
    Дети, которые были отданы под опеку или в приемную семью
    """

    class CareType(models.TextChoices):
        WARDERED = "1", "Взято под опеку"
        FOSTER_FAMILY = "2", "Взято приемной семьей"

    child = models.ForeignKey(Child, on_delete=models.CASCADE)
    date_of_adoption = models.DateField(null=False, verbose_name="Дата взятия в приемную семью или под опекунство")
    care_type = models.CharField(choices=CareType, verbose_name="Тип попечительства")

    class Meta:
        verbose_name = "попечительство"


class ChildAdopted(models.Model):
    """
    Усыновленные дети
    """
    child = models.ForeignKey(Child, on_delete=models.CASCADE)
    date_of_adoption = models.DateField(null=False, verbose_name="Дата усыновления")


class AdoptionParent(models.Model):
    """
    Приемные родители детей
    """
    adoption = models.ForeignKey(ChildAdopted, on_delete=models.CASCADE)
    last_name = models.CharField(null=False, blank=False, max_length=100, verbose_name=_("last name"))
    first_name = models.CharField(null=False, blank=False, max_length=100, verbose_name=_("first name"))
    patronymic = models.CharField(null=False, blank=False, max_length=100, verbose_name=_("patronymic"))

    class Meta:
        verbose_name = "приемные родители"
