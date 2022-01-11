from django.shortcuts import render
from crm_app.models import Contacts, Proposal
from django.db.models import Count, Q
import json


def dashboard(request):
    data_set = Proposal.objects.filter(time_create__range=['2020-01-01', '2022-01-08']).values('funnel__name') \
        .annotate(funnel_1=Count('funnel__name', filter=Q(funnel=1)),
                  funnel_2=Count('funnel__name', filter=Q(funnel=2)),
                  funnel_3=Count('funnel__name', filter=Q(funnel=3)),
                  funnel_4=Count('funnel__name', filter=Q(funnel=4)),
                  funnel_5=Count('funnel__name', filter=Q(funnel=5)),
                  funnel_6=Count('funnel__name', filter=Q(funnel=6)),
                  funnel_7=Count('funnel__name', filter=Q(funnel=7)))

    categories = list()
    funnel_1_data = list()
    funnel_2_data = list()
    funnel_3_data = list()
    funnel_4_data = list()
    funnel_5_data = list()
    funnel_6_data = list()
    funnel_7_data = list()

    for entry in data_set:
        categories.append(entry['funnel__name'])
        funnel_1_data.append(entry['funnel_1'])
        funnel_2_data.append(entry['funnel_2'])
        funnel_3_data.append(entry['funnel_3'])
        funnel_4_data.append(entry['funnel_4'])
        funnel_5_data.append(entry['funnel_5'])
        funnel_6_data.append(entry['funnel_6'])
        funnel_7_data.append(entry['funnel_7'])

    print({'data_set': data_set})

    funnel_1 = {
        'name': 'Не обработана',
        'data': funnel_1_data,
        'color': 'gray'
    }

    funnel_2 = {
        'name': 'Квалификация',
        'data': funnel_2_data,
        'color': 'blue'
    }
    funnel_3 = {
        'name': 'Переговоры',
        'data': funnel_3_data,
        'color': 'yellow'
    }
    funnel_4 = {
        'name': 'Согласование документов',
        'data': funnel_4_data,
        'color': 'orange'
    }
    funnel_5 = {
        'name': 'Счёт выставлен',
        'data': funnel_5_data,
        'color': 'black'
    }
    funnel_6 = {
        'name': 'Выиграна',
        'data': funnel_6_data,
        'color': 'green'
    }
    funnel_7 = {
        'name': 'Проиграна',
        'data': funnel_7_data,
        'color': 'red'
    }

    chart = {
        'chart': {'type': 'column'},
        'title': {'text': 'Количество заявок по воронке продаж'},
        'xAxis': {'categories': categories},
        'series': [funnel_1, funnel_2, funnel_3, funnel_4, funnel_5, funnel_6, funnel_7]
    }

    dump = json.dumps(chart)

    return render(request, 'chart.html', {'chart': dump})
