from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
import csv

def index(request):
    return redirect(reverse('bus_stations'))

def bus_stations(request):
    with open('data-398-2018-08-30.csv', newline='', encoding="utf8") as csvfile:
        reader = csv.DictReader(csvfile)
        stations = []
        for row in reader:
            stations.append(
                {'Name': row['Name'],
                 'Street': row['Street'],
                 'District': row['District']})
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    page_number = int(request.GET.get('page', 1))
    pagi = Paginator(stations, 10)
    page = pagi.get_page(page_number)
    context = {
            'bus_stations': page.object_list,
            'page': page,
    }    
    return render(request, 'stations/index.html', context)
