import itertools
import random
from datetime import datetime, timedelta

from django.core.management import BaseCommand

from core.models import Child, ChildAdmission, ChildDeath, Employee, Employment, ChildReturned, ChildCare, ChildAdopted, \
    ChildRepatriation, InternationalAdoption, TransferToTreatment, TransferByCertainAge, Orphanage, ChildSickness, \
    Checkup
from orphanage.settings import DEBUG


class Command(BaseCommand):
    help = "Заполнение случайными данными."

    def handle(self, *args, **options):
        if DEBUG:
            clear()
            create_children()
            create_employees()


def clear():
    Child.objects.all().delete()
    ChildAdmission.objects.all().delete()
    ChildDeath.objects.all().delete()
    ChildReturned.objects.all().delete()
    ChildCare.objects.all().delete()
    ChildAdopted.objects.all().delete()
    ChildRepatriation.objects.all().delete()
    InternationalAdoption.objects.all().delete()
    Employee.objects.all().delete()
    Employment.objects.all().delete()
    Orphanage.objects.all().delete()


def create_children():
    male_count = random.randint(50, 55)
    female_count = random.randint(50, 55)
    children_names = get_random_names(male_count, female_count)
    today = datetime.today()

    # дом ребёнка
    Orphanage.objects.create(location_type="X", count_of_seats=(male_count+female_count)//2)

    for full_name in children_names:
        # Ребёнок
        child = Child(first_name=full_name[0],
                      patronymic=full_name[1],
                      last_name=full_name[2],
                      date_of_birth=get_random_child_birthday(),
                      disability_category=random.randint(0, 3))
        child.save()
        # Поступление
        admission = ChildAdmission(child=child,
                                   date_of_admission=child.date_of_birth + timedelta(days=random.randint(0, 70)),
                                   admission_type=str(random.randint(1, 2)))
        admission.save()

        # Взаимоисключающие записи:
        # Смертность
        if random.randint(0, 99) <= 5:  # 5%
            ChildDeath.objects.create(child=child,
                                      date_of_death=get_random_date_between(admission.date_of_admission,
                                                                            today))
        # Взятие родителями
        elif random.randint(0, 99) <= 5:  # 5% оставшихся
            ChildReturned.objects.create(child=child,
                                         date_of_adoption=get_random_date_between(admission.date_of_admission,
                                                                                  today))
        # Взятие родителями
        elif random.randint(0, 99) <= 5:  # 5% оставшихся
            ChildReturned.objects.create(child=child,
                                         date_of_adoption=get_random_date_between(admission.date_of_admission,
                                                                                  today))
        # Опека или приемная семья
        elif random.randint(0, 99) <= 7:  # 7% оставшихся
            ChildCare.objects.create(child=child,
                                     care_type=str(random.randint(1, 2)),
                                     date_of_adoption=get_random_date_between(admission.date_of_admission,
                                                                              today))
        # Усыновленные дети
        elif random.randint(0, 99) <= 7:  # 7% оставшихся
            ChildAdopted.objects.create(child=child,
                                        date_of_adoption=get_random_date_between(admission.date_of_admission,
                                                                                 today))
        # Репатриация
        elif random.randint(0, 99) <= 10:  # 10% оставшихся
            ChildRepatriation.objects.create(child=child,
                                             date_of_repatriation=get_random_date_between(admission.date_of_admission,
                                                                                          today),
                                             country="X")
        # международное усыновление
        elif random.randint(0, 99) <= 5:  # 5% оставшихся
            InternationalAdoption.objects.create(child=child,
                                                 date_of_adoption=get_random_date_between(admission.date_of_admission,
                                                                                          today))
        # Переведенные в медицинские организации
        elif random.randint(0, 99) <= 5:  # 5% оставшихся
            TransferToTreatment.objects.create(child=child,
                                               date_of_transfer=get_random_date_between(admission.date_of_admission,
                                                                                        today),
                                               organization="X")
        # Переведенные по достижению определённого возраста
        age = today.year - child.date_of_birth.year - ((today.month, today.day) < (child.date_of_birth.month, child.date_of_birth.day))
        if age >= 3:
            TransferByCertainAge.objects.create(child=child,
                                                date_of_transfer=child.date_of_birth + timedelta(days = 364*3),
                                                type=str(random.randint(1, 2)))
        # Заболевания
        if random.randint(0, 99) <= 80: # 80%
            for i in range(0, random.randint(1, 3)):
                ChildSickness.objects.create(child=child,
                                             icd_code=get_random_icd_code(),
                                             date_of_diagnosis=get_random_date_between(admission.date_of_admission, today))

        # Профилактика
        if random.randint(0, 99) <= 80: # 80%
            Checkup.objects.create(child=child,
                                   date_of_checkup=get_random_date_between(admission.date_of_admission, today),
                                   diagnosis=str(random.randint(1, 10)))

def create_employees():
    employees_count = random.randint(100, 110)
    names = get_random_names(employees_count // 2, employees_count // 2)
    today = datetime.today()
    for name in names:
        employee = Employee(first_name=name[0], patronymic=name[1], last_name=name[2])
        employee.save()
        employment_rate = random.choices([0.25, 0.5, 0.75, 1, 1.25, 1.5],
                                         weights=(10, 30, 10, 90, 20, 10),
                                         k=1)[0]
        employment = Employment(employee=employee,
                                rate=employment_rate,
                                report_category=str(random.randint(1, 8)),
                                start_date_of_employment=today - timedelta(
                                    days=random.randint(100, 360 * 3)),
                                end_date_of_employment=None)
        if random.randint(0, 99) <= 55:  # 55%
            employment.end_date_of_employment = get_random_date_between(employment.start_date_of_employment,
                                                                        today)
        employment.save()


MALE_FIRST_NAMES = {"Иван", "Петр", "Андрей", "Василий", "Семён", "Антон", "Владимир", "Геннадий", "Николай", "Роман"}
MALE_MIDDLE_NAMES = {"Иванович", "Петрович", "Андреевич", "Василиевич", "Семёнович", "Антонович", "Владимирович",
                     "Геннадиевич", "Николаевич", "Романович"}
MALE_LAST_NAMES = {"Иванов", "Петров", "Андреев", "Васильев", "Семёнов", "Антонов", "Владимиров", "Геннадьев",
                   "Николаев", "Романов"}
MALE_NAMES = sorted(itertools.product(MALE_FIRST_NAMES, MALE_MIDDLE_NAMES, MALE_LAST_NAMES))

FEMALE_FIRST_NAME = {"Елена", "Анна", "Ольга", "Екатерина", "Вера", "Надежда", "Любовь", "Ксения", "Светлана",
                     "Татьяна"}
FEMALE_MIDDLE_NAMES = {"Ивановна", "Петровна", "Андреевна", "Василиевна", "Семёновна", "Антоновна", "Владимировна",
                       "Геннадиевна", "Николаевна", "Романовна"}
FEMALE_LAST_NAMES = {"Иванова", "Петрова", "Андреева", "Васильева", "Семёнова", "Антонова", "Владимирова", "Геннадьева",
                     "Николаева", "Романова"}
FEMALE_NAMES = sorted(itertools.product(FEMALE_FIRST_NAME, FEMALE_MIDDLE_NAMES, FEMALE_LAST_NAMES))


def get_random_icd_code():
    letter = random.choice('ABCDEFGHIJKLMNOPQRSTU')
    code = random.randint(0, 100)
    return f'{letter:03}{code}'

def get_random_names(males, females):
    return random.sample(MALE_NAMES, males) + random.sample(FEMALE_NAMES, females)


def get_random_date_between(date_start, date_end):
    delta_seconds = (date_end - date_start).total_seconds()
    return date_start + timedelta(seconds=random.uniform(0, delta_seconds))


def get_random_child_birthday():
    now = datetime.now()
    delta_days = random.randint(100, 360 * 4)
    return now - timedelta(days=delta_days)
