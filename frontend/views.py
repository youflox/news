from django.shortcuts import render

import requests

def homepage(request):
    url = 'http://homz.pythonanywhere.com/api/list'
    data = requests.get(url).json()

    url = 'http://homz.pythonanywhere.com/api/list/'
    data = requests.get(url).json()
    carousel=[]
    top_list=[]
    main_list=[]
    for n in range(len(data)):
        if n in range(0,2):
            carousel.append(data[n])
        elif n in range(2,6):
            top_list.append(data[n])
        else:
            main_list.append(data[n])

    context = {'carousel': carousel,'top_list': top_list, 'main_list': main_list }

    return render(request, "homepage.html", context)

