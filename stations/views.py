from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
import csv

def index(request):
    return redirect(reverse('bus_stations'))

def bus_stations(request):
    with open('data-398-2018-08-30.csv', newline='', encoding="utf8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            stations = (row['Name'], row['Street'], row['District'])
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    page_number = int(request.GET.get('page', 1))
    CONTENT = [str(i) for i in range(10000)]
    paginator = Paginator(CONTENT, 10)
    page = paginator.get_page(page_number)
    context = {
            'bus_stations': stations,
            'page': page,
    }    
    return render(request, 'stations/index.html', context)
