import tempfile
from pathlib import Path
from uuid import uuid4

import openpyxl
import random

from core.models import Orphanage, Employee, Employment, ChildAdmission, ChildReturned, ChildCare, ChildAdopted, \
    ChildRepatriation, InternationalAdoption, TransferToTreatment, TransferByCertainAge, ChildDeath
from orphanage.settings import BASE_DIR


def build_report_2120(start, end):
    # исходный файл с незаполненной таблицей
    source = BASE_DIR / 'core' / 'templates' / 'reports' / 'report_2120.xlsx'

    # файл назначения
    destination = Path(tempfile.mkdtemp()) / str(uuid4().hex)

    # вывод в консоль
    print(f'Report 2120 to "{destination}" from "{start}" to "{end}"')

    # открытие файла
    workbook = openpyxl.load_workbook(source)

    # получение листа
    spreadsheet = workbook.active

    # заполнение данных в таблицу
    for i in range(5, 8):
        for j in range(3, 12):
            cell = spreadsheet.cell(row=i, column=j)
            cell.value = random.randint(-2000, 2000) / 1000

    # сохранение файла во временный файл
    workbook.save(destination)
    workbook.close()
    return destination


def build_report_summary(start, end):
    # исходный файл с незаполненной таблицей
    source = BASE_DIR / 'core' / 'templates' / 'reports' / 'report_summary.xlsx'

    # файл назначения
    destination = Path(tempfile.mkdtemp()) / str(uuid4().hex)

    # вывод в консоль
    print(f'Report 2120 to "{destination}" from "{start}" to "{end}"')

    # открытие файла
    workbook = openpyxl.load_workbook(source)

    # получение листа
    spreadsheet = workbook.active

    # заполнение таблицы данными 1 Дом ребёнка
    spreadsheet["A6"].value = 1
    orphanage = Orphanage.objects.first()
    spreadsheet["B6"].value = 1
    spreadsheet["D6"].value = orphanage.count_of_seats

    # заполнение таблицы данными 2 Штаты организации, человек
    employees = Employee.objects.all()
    spreadsheet["C16"].value = Employment.objects.filter(end_date_of_employment__isnull=True).count()

    spreadsheet["D16"].value = Employment.objects.filter(
        report_category=Employment.PositionCategory.DOCTOR,
        end_date_of_employment__isnull=True).count()

    spreadsheet["E16"].value = Employment.objects.filter(
        report_category=Employment.PositionCategory.NON_MEDICAL_STAFF,
        end_date_of_employment__isnull=True).count()

    spreadsheet["F16"].value = Employment.objects.filter(
        report_category=Employment.PositionCategory.PHARMACIST,
        end_date_of_employment__isnull=True).count()

    spreadsheet["G16"].value = Employment.objects.filter(
        report_category=Employment.PositionCategory.LINEAR_MEDICAL_STAFF,
        end_date_of_employment__isnull=True).count()

    # заполнение таблицы данными 3 Контингенты дома ребенка, человек
    spreadsheet["C29"].value = ChildAdmission.objects.count()

    spreadsheet["C30"].value = ChildAdmission.objects.filter(
        admission_type=ChildAdmission.AdmissionType.WITHOUT_CARE).count()

    spreadsheet["C31"].value = ChildAdmission.objects.filter(
        admission_type=ChildAdmission.AdmissionType.ORPHAN).count()

    returned_child = ChildReturned.objects.count()
    child_care = ChildCare.objects.count()
    child_adoption = ChildAdopted.objects.count()
    repatriation = ChildRepatriation.objects.count()
    internation_adoption = InternationalAdoption.objects.count()
    transfer_to_treatment = TransferByCertainAge.objects.count()
    transfer_by_age = TransferByCertainAge.objects.count()
    summa = returned_child + child_care + child_adoption + repatriation + internation_adoption + transfer_to_treatment + transfer_by_age

    spreadsheet["D29"].value = summa

    orphan_child_ids = ChildAdmission.objects.filter(
        admission_type=ChildAdmission.AdmissionType.ORPHAN
    ).values_list('child_id', flat=True)

    discharged_orphans_count = (
            ChildReturned.objects.filter(child_id__in=orphan_child_ids).count() +
            ChildCare.objects.filter(child_id__in=orphan_child_ids).count() +
            ChildAdopted.objects.filter(child_id__in=orphan_child_ids).count() +
            ChildRepatriation.objects.filter(child_id__in=orphan_child_ids).count() +
            InternationalAdoption.objects.filter(child_id__in=orphan_child_ids).count() +
            TransferToTreatment.objects.filter(child_id__in=orphan_child_ids).count() +
            TransferByCertainAge.objects.filter(child_id__in=orphan_child_ids).count()
    )

    spreadsheet["D30"].value = discharged_orphans_count

    without_care_child_ids = ChildAdmission.objects.filter(
        admission_type=ChildAdmission.AdmissionType.WITHOUT_CARE
    ).values_list('child_id', flat=True)

    discharged_orphans_count = (
            ChildReturned.objects.filter(child_id__in=without_care_child_ids).count() +
            ChildCare.objects.filter(child_id__in=without_care_child_ids).count() +
            ChildAdopted.objects.filter(child_id__in=without_care_child_ids).count() +
            ChildRepatriation.objects.filter(child_id__in=without_care_child_ids).count() +
            InternationalAdoption.objects.filter(child_id__in=without_care_child_ids).count() +
            TransferToTreatment.objects.filter(child_id__in=without_care_child_ids).count() +
            TransferByCertainAge.objects.filter(child_id__in=without_care_child_ids).count()
    )

    spreadsheet["D31"].value = discharged_orphans_count

    spreadsheet["F29"].value = ChildDeath.objects.count()

    # сохранение файла во временный файл
    workbook.save(destination)
    workbook.close()
    return destination


if __name__ == '__main__':
    build_report_2120(1, 2)
