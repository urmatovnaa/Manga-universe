from celery import shared_task
from openpyxl import load_workbook
from .models import ReportManga


# takes excel file and makes report into, then returns changed file
@shared_task
def make_report(report_object_id):
    report_object = ReportManga.objects.get(id=report_object_id)
    input_file = report_object.input_file
    excel_file = load_workbook(input_file.path)
    page = excel_file["Лист1"]

    lst = page["B"]
    res = {}
    for cell in lst:  # B2
        row_number = cell.row  # 2

        if row_number == 1:
            continue
        type = cell.value

        if type not in res:
            res[type] = 1
        else:
            res[type] += 1

    # header
    row_number = 1
    page[f"E{row_number}"] = "type"
    page[f"F{row_number}"] = "title's count"
    i = 0
    numbers = "23456789"
    for type_value in res.keys():
        page[f"E{numbers[i]}"] = type_value
        page[f"F{numbers[i]}"] = res[type_value]
        i += 1

    output_file_path = input_file.path.replace(".xlsx", "_ready.xlsx")
    excel_file.save(output_file_path)
    output_file_name = report_object.input_file.name.replace(".xlsx", "_ready.xlsx")
    report_object.output_file.name = output_file_name
    report_object.save()
    return 'all done!'
