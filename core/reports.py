import tempfile
from pathlib import Path
from uuid import uuid4

import openpyxl
import random

from core.models import Orphanage
from orphanage.settings import BASE_DIR

def build_report_2120(start, end):

    # исходный файл с незаполненной таблицей
    source = BASE_DIR / 'core'/ 'templates' / 'reports' / 'report_2120.xlsx'

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
    source = BASE_DIR / 'core'/ 'templates' / 'reports' / 'report_summary.xlsx'

    # файл назначения
    destination = Path(tempfile.mkdtemp()) / str(uuid4().hex)

    # вывод в консоль
    print(f'Report 2120 to "{destination}" from "{start}" to "{end}"')

    # открытие файла
    workbook = openpyxl.load_workbook(source)

    # получение листа
    spreadsheet = workbook.active

    # заполнение данных в таблицу
    spreadsheet["A8"].value=1
    orphanage = Orphanage.objects.first()
    spreadsheet["C8"].value=1
    spreadsheet["D8"].value=orphanage.count_of_seats

    # сохранение файла во временный файл
    workbook.save(destination)
    workbook.close()
    return destination


if __name__ == '__main__':
    build_report_2120(1, 2)