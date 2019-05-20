from django.shortcuts import render
from django.views import View
import subprocess
import pandas as pd


def index(request):
    return render(request, 'tt/index.html')

def about(request):
    return render(request, 'tt/about.html')

class Inputform(View):

    def get(self, request):
        return render(request, 'tt/input.html', {})

    def post(self, request):

        group = request.POST.get("group")
        Knowledge = request.POST.get("Knowledge")
        Skill = request.POST.get("Skill")
        Social = request.POST.get("Social")
        Loyality = request.POST.get("Loyality")
        Total = request.POST.get("Total")
        monday = request.POST.get("monday")
        tuesday = request.POST.get("tuesday")
        wednesday = request.POST.get("wednesday")
        thursday = request.POST.get("thursday")
        friday = request.POST.get("friday")
        saturday = request.POST.get("saturday")
        windows = request.POST.get("windows")
        time_t = request.POST.get("time")
        start = request.POST.get("start")
        monday_start = request.POST.get("monday_start")
        tuesday_start = request.POST.get("tuesday_start")
        wednesday_start = request.POST.get("wednesday_start")
        thursday_start = request.POST.get("thursday_start")
        friday_start = request.POST.get("friday_start")
        saturday_start = request.POST.get("saturday_start")
        end = request.POST.get("end")
        monday_end = request.POST.get("monday_end")
        tuesday_end = request.POST.get("tuesday_end")
        wednesday_end = request.POST.get("wednesday_end")
        thursday_end = request.POST.get("thursday_end")
        friday_end = request.POST.get("friday_end")
        saturday_end = request.POST.get("saturday_end")

        import time
        filename = str(int(time.time() * 10**6))
        filename_path = "tt/static/files/" + filename + ".csv"
        print("filename = ", filename)

        days_1 = [monday, tuesday, wednesday, thursday, friday, saturday]
        days = ''
        for day in days_1:
            if day is not None:
                days += str(day)
            if len(str(days)) == 0:
                days = "0"

        days_2 = [monday_start, tuesday_start, wednesday_start, thursday_start, friday_start, saturday_start]

        days_start = ''
        for day in days_2:
            if day is not None:
                days_start += str(day)
            if len(str(days_start)) == 0:
                days_start = "0"

        days_3 = [monday_end, tuesday_end, wednesday_end, thursday_end, friday_end, saturday_end]
        days_end = ''
        for day in days_3:
            if day is not None:
                days_end += str(day)
            if len(str(days_end)) == 0:
                days_end = "0"

        subprocess.check_call([r"tt/static/exe/main_doubled", filename_path, group, windows, Knowledge, Skill, Social, Loyality, Total, days, start, end, days_start, days_end, time_t])

        columns = ['Предмет', 'Преподаватель', 'Ауд.', 'Время']
        df = pd.read_csv(
            filename_path, sep=";",
            header=None, names=columns)

        filename_html = "tt/templates/tt/" + filename + ".html"
        f = open(filename_html, 'w')
        a = df.to_html()
        f.write(a)
        f.close()

        context = {
            "filename" : filename_path,
            "group" : group,
            "windows": windows,
            "Knowledge" : Knowledge,
            "Skill" : Skill,
            "Social" : Social,
            "Loyality": Loyality,
            "Total" : Total,
            "days" : days,
            "start": start,
            "end": end,
            "days_start" : days_start,
            "days_end" : days_end,
            "time" : time_t
            }

        print(context)

        filename_html_1 = "tt/" + filename + ".html"



        return render(request, filename_html_1)


