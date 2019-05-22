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

        mon = [request.POST.get(str("mon" + str(i))) for i in range(1, 8)]
        tue = [request.POST.get(str("tue" + str(i))) for i in range(1, 8)]
        wed = [request.POST.get(str("wed" + str(i))) for i in range(1, 8)]
        thu = [request.POST.get(str("thu" + str(i))) for i in range(1, 8)]
        fri = [request.POST.get(str("fri" + str(i))) for i in range(1, 8)]
        sat = [request.POST.get(str("sat" + str(i))) for i in range(1, 8)]


        def MakeStrFromPairs(day):
            string = ''
            for pair in day:
                if pair is not None:
                    string += str(pair)
            return string

        mond, tues, wedn, thur, frid, satu = list(map(MakeStrFromPairs, [mon, tue, wed, thu, fri, sat]))

        pairs = mond + tues + wedn + thur + frid + satu

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

        import time
        filename = str(int(time.time() * 10 ** 6))
        filename_path = "tt/static/files/" + filename + ".csv"

        subprocess.check_call([r"tt/static/exe/main", filename_path, group, windows, Knowledge, Skill, Social, Loyality, Total, days, start, end, days_start, days_end, time_t, pairs])
        columns = ['Предмет', 'Преподаватель', 'Ауд.', 'Время']
        df = pd.read_csv(
            filename_path, sep=";",
            header=None, names=columns, index_col=False)
        list_days = ["Понедельник"] + [" "]*6 + ["Вторник"] + [" "] *6 + ["Среда"] + [" "] *6 + ["Четверг"] + [" "] *6 + ["Пятница"] + [" "] *6 + ["Суббота"] + [" "] *6

        df['День'] = list_days

        columns = df.columns.to_list()

        columns = columns[-1:] + columns[:-1]
        columns = columns[-1:] + columns[:-1]
        columns[0], columns[1] = columns[1], columns[0]
        df = df[columns]
        df = df.fillna("-")

        filename_html = "tt/templates/tt/" + filename +".html"
        # filename_html = "tt/templates/tt/" + group + ".html"
        f = open(filename_html, 'w')
        a = df.to_html(justify="center")
        f.write(a)
        f.close()
        f = open(filename_html)
        lines = f.readlines()
        f.close()
        f = open(filename_html, 'w')
        f.writelines([line for line in lines[1:-1]])
        f.close()

        filename_html_1 = "tt/" + filename + ".html"
        filename_html_old = "tt/" + group + ".html"

        context = {
            "filename" : filename_html_1,
            "old" : filename_html_old,
            "group" : group,
            "Knowledge" : Knowledge,
            "Skill" : Skill,
            "Social" : Social,
            "Loyality" : Loyality,
            "Total" : Total,
            "monday" : monday,
            "tuesday" : tuesday,
            "wednesday" : wednesday,
            "thursday" : thursday,
            "friday" : friday,
            "saturday" : saturday,
            "windows" : windows,
            "time_t" : time_t,
            "start" : start,
            "monday_star" : monday_start,
            "tuesday_start" : tuesday_start,
            "wednesday_start" : wednesday_start,
            "thursday_start" : thursday_start,
            "friday_start" : friday_start,
            "saturday_start" : saturday_start,
            "end" : end,
            "monday_end" : monday_end,
            "tuesday_end" : tuesday_end,
            "wednesday_end" : wednesday_end,
            "thursday_end" : thursday_end,
            "friday_end" : friday_end,
            "pairs" : pairs
        }

        print(filename_path, group, windows, Knowledge, Skill, Social, Loyality, Total, days, start, end, days_start, days_end, time_t, pairs)

        return render(request, "tt/output.html", context)


