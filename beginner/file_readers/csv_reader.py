import csv
from django.shortcuts import render

def csv_view(request):
    with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        data = list(reader)
    
    return render(request, 'csv_template.html', {'data': data})
