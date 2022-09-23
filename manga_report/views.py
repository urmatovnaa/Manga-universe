from django.shortcuts import render, HttpResponse
from django.views import View
from .models import ReportManga
from threading import Thread
from .tasks import make_report


# Create your views here.
class ReportView(View):
    template_name = "report/report.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        rep = ReportManga()
        excel_file = request.FILES["input_file"]
        rep.input_file = excel_file
        rep.save()
        print("Сейчас вызову celery task add")
        make_report.delay(report_object_id=rep.id)
        print("Таск был вызван строкой выше")

        return HttpResponse("Данные приняты, отчёт готовится...")
