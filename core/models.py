from django.db import models
from django.utils.translation import gettext_lazy as _

class Child(models.Model):
    """
    Модель ребёнка
    """
    first_name = models.CharField(null=False, blank=False, max_length=100, verbose_name="имя")
    last_name = models.CharField(null=False, blank=False, max_length=100, verbose_name="фамилия")
    patronymic = models.CharField(null=False, blank=False, max_length=100, verbose_name="отчество")
    date_of_birth = models.DateField(null=False, verbose_name="дата рождения")
    disability_category = models.IntegerField(null=False, blank=False, default=0, verbose_name="категория инвалидности")
    class Meta:
        verbose_name = "ребёнка"
        verbose_name_plural = "дети"
    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.patronymic} [{self.date_of_birth}]"

class ChildAdmission(models.Model):
    """
    Поступление
    """
    class AdmissionType(models.TextChoices):
        ORPHAN = "1", "Сирота"
        WITHOUT_CARE = "2", "Оставшийся без попечения родителей"

    child = models.ForeignKey(Child, on_delete=models.CASCADE, verbose_name="ребёнок")
    date_of_admission = models.DateField(null=False, verbose_name="дата поступления")
    admission_type = models.CharField(choices=AdmissionType, default="1", verbose_name="причина поступления")

    class Meta:
        verbose_name = "поступление ребёнка"
        verbose_name_plural = "поступление детей"

class ChildDeath(models.Model):
    """
    Смерти детей
    """
    child = models.OneToOneField(Child, primary_key = True, on_delete=models.CASCADE, verbose_name="ребёнок")
    date_of_death = models.DateField(null=False, verbose_name="дата смерти")

    class Meta:
        verbose_name = "смертность"
        verbose_name_plural = "смертность"

    def __str__(self):
        return f" "

class Employee(models.Model):
    """
    Сотрудники
    """
    last_name = models.CharField(null=False, blank=False, max_length=100, verbose_name="фамилия")
    first_name = models.CharField(null=False, blank=False, max_length=100, verbose_name="имя")
    patronymic = models.CharField(null=False, blank=False, max_length=100, verbose_name="отчество")

    class Meta:
        verbose_name = "сотрудника"
        verbose_name_plural = "сотрудники"

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.patronymic}"


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

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name="сотрудник")
    rate = models.DecimalField(null=False, blank=False, max_digits=4, decimal_places=2, verbose_name="ставка")
    report_category = models.CharField(choices=PositionCategory, verbose_name="категория")
    start_date_of_employment = models.DateField(null=False, verbose_name="дата трудоустройства")
    end_date_of_employment = models.DateField(null=True, blank=True, verbose_name="дата увольнения")

    class Meta:
        verbose_name = "трудоустройство"
        verbose_name_plural = "трудоустройства"


class ChildReturned(models.Model):
    """
    Дети, взятые родителями
    """
    child = models.ForeignKey(Child, on_delete=models.CASCADE, verbose_name="ребёнок")
    date_of_adoption = models.DateField(null=False, verbose_name="дата взятия родителями")
    class Meta:
        verbose_name = "ребёнка, взятого родителями"
        verbose_name_plural = "дети, взятые родителями"

class ChildParent(models.Model):
    """
    Родители детей
    """
    returned = models.ForeignKey(ChildReturned, on_delete=models.CASCADE, verbose_name="ребёнок")
    last_name = models.CharField(null=False, blank=False, max_length=100, verbose_name="фамилия")
    first_name = models.CharField(null=False, blank=False, max_length=100, verbose_name="имя")
    patronymic = models.CharField(null=False, blank=False, max_length=100, verbose_name="отчество")

    class Meta:
        verbose_name = "родителя"
        verbose_name_plural = "родители"

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.patronymic}"


class ChildCare(models.Model):
    """
    Дети, которые были отданы под опеку или в приемную семью
    """

    class CareType(models.TextChoices):
        WARDERED = "1", "Взято под опеку"
        FOSTER_FAMILY = "2", "Взято приемной семьей"

    child = models.ForeignKey(Child, on_delete=models.CASCADE, verbose_name="ребёнок")
    date_of_adoption = models.DateField(null=False, verbose_name="дата взятия в приемную семью или под опекунство")
    care_type = models.CharField(choices=CareType, verbose_name="тип попечительства")

    class Meta:
        verbose_name = "попечительство"
        verbose_name_plural = "попечительства"


class ChildAdopted(models.Model):
    """
    Усыновленные дети
    """
    child = models.ForeignKey(Child, on_delete=models.CASCADE, verbose_name="ребёнок")
    date_of_adoption = models.DateField(null=False, verbose_name="дата усыновления")

    class Meta:
        verbose_name = "усыновленного ребёнка"
        verbose_name_plural = "усыновленные дети"

class AdoptionParent(models.Model):
    """
    Приемные родители детей
    """
    adoption = models.ForeignKey(ChildAdopted, on_delete=models.CASCADE, verbose_name="ребёнок")
    last_name = models.CharField(null=False, blank=False, max_length=100, verbose_name="фамилия")
    first_name = models.CharField(null=False, blank=False, max_length=100, verbose_name="имя")
    patronymic = models.CharField(null=False, blank=False, max_length=100, verbose_name="отчество")

    class Meta:
        verbose_name = "приемного родителя"
        verbose_name_plural = "приемные родители"

class ChildRepatriation(models.Model):
    """
    Репатриация
    """
    child = models.ForeignKey(Child, on_delete=models.CASCADE, verbose_name="ребёнок")
    date_of_repatriation = models.DateField(null=False, verbose_name="дата репатриации")

    class Meta:
        verbose_name = "репатриацию"
        verbose_name_plural = "репатриации"


class InternationalAdoption(models.Model):
    """
    Дети, отданные на международное усыновление
    """
    child = models.ForeignKey(Child, on_delete=models.CASCADE, verbose_name="ребёнок")
    date_of_adoption = models.DateField(null=False, verbose_name="дата усыновления")

    class Meta:
        verbose_name = "международное усыновление"
        verbose_name_plural = "международные усыновления"


class TransferToTreatment(models.Model):
    """
    Переведенные в медицинские организации
    """
    child = models.ForeignKey(Child, on_delete=models.CASCADE, verbose_name="ребёнок")
    date_of_transfer = models.DateField(null=False, verbose_name="дата перевода")
    organization = models.CharField(null=False, blank=False, max_length=100, verbose_name="название организации")
    class Meta:
        verbose_name = "перевод в медицинские организации"
        verbose_name_plural = "перевод в медицинские организации"


class TransferByCertainAge(models.Model):
    """
    Перевод в учреждения по достижению определенного возраста
    """
    class InstitutionType(models.TextChoices):
        EDUCATION_INST = "1", "Образовательная организация"
        SOCIAL_SAFE_INST = "2", "Организация социальной защиты населения"

    child = models.ForeignKey(Child, on_delete=models.CASCADE, verbose_name="ребёнок")
    date_of_transfer = models.DateField(null=False, verbose_name="дата перевода в учреждение")
    type = models.CharField(choices=InstitutionType)

    class Meta:
        verbose_name = "перевод в учреждения по достижению определенного возраста"
        verbose_name_plural = "переводы в учреждения по достижению определенного возраста"



class ChildSickness(models.Model):
    """
    Заболеваемость детей
    """
    child = models.ForeignKey(Child, on_delete=models.CASCADE, verbose_name="ребёнок")
    icd_code = models.CharField(null=False, blank=False, max_length=100, verbose_name="код диагноза по МКБ")
    date_of_diagnosis = models.DateField(null=False, verbose_name="дата постановления диагноза")
    class Meta:
        verbose_name = "заболеваемость"
        verbose_name_plural = "заболеваемости"



class Checkup(models.Model):
    """
    Профилактические осмотры
    """
    child = models.ForeignKey(Child, on_delete=models.CASCADE, verbose_name="ребёнок")
    date_of_checkup = models.DateField(null=False, verbose_name="дата профилактического осмотра")
    diagnosis = models.CharField(null=False, blank=False, max_length=100, verbose_name="диагноз")

    class Meta:
        verbose_name = "профилактические осмотры"
        verbose_name_plural = "профилактические осмотры"



class Orphanage(models.Model):
    """
    Информация о доме ребенка
    """
    location_type = models.CharField(null=False, blank=False, max_length=100, verbose_name="местоположение")
    count_of_seats = models.IntegerField(null=False, blank=False, default=0, verbose_name="количество мест")

    class Meta:
        verbose_name = "информация о доме ребенка"
        verbose_name_plural = "информация о доме ребенка"

