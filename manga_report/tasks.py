from celery import shared_task
from openpyxl import load_workbook
from .models import ReportManga


@shared_task
def add(x, y):
    print("Начался расчёт")
    print("Завершился расчёт")
    return x + y


# takes excel file and makes report into, then returns changed file
@shared_task
def make_report(report_object_id):
    print('hello world')
    report_object = ReportManga.objects.get(id=report_object_id)
    input_file = report_object.input_file
    excel_file = load_workbook(input_file.path)
    page = excel_file["Лист1"]

    lst = page["A"]
    res = {}
    for cell in lst:  # A2
        row_number = cell.row  # 2

        if row_number == 1:
            continue

        name = cell.value
        if name not in res:
            res[name] = {}

        date_cell = page[f"B{row_number}"].value  # 01.01.2022

        if date_cell not in res[name]:
            res[name][date_cell] = 1
        else:
            res[name][date_cell] += 1

    # header
    row_number = 1
    page[f"E{row_number}"] = "seller name"
    letters = "FGHIJKLMNOPQR"  # ...
    i = 0
    for date_value in res[name]:
        # print(date_value)
        page[f"{letters[i]}{row_number}"] = date_value
        i += 1

    # cells
    for name, date_qty_dict in res.items():
        row_number += 1

        page[f"E{row_number}"] = name

        i = 0
        for date_value, qty in date_qty_dict.items():
            page[f"{letters[i]}{row_number}"] = qty
            i += 1

    output_file_path = input_file.path.replace(".xlsx", "_ready.xlsx")
    excel_file.save(output_file_path)
    output_file_name = report_object.input_file.name.replace(".xlsx", "_ready.xlsx")
    report_object.output_file.name = output_file_name
    report_object.save()
    return 'all done!'
