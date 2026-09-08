from django.shortcuts import render
from .models import Radar
from rest_framework import viewsets
from .siralazers import RadarSerilazers

def jarima_info(request):
    jarimalar=Radar.objects.all()
    # jarimalar=Radar.objects.filter(car_number='777')
    # jarimalar=Radar.objects.exclude(car_number='455')
    # jarimalar=Radar.objects.get(car_number='255')
    return render(request, 'Jarimalar.html',{'jarimalar':jarimalar})

class Radarwiewset(viewsets.ModelViewSet):
    queryset = Radar.objects.all()
    serializer_class = RadarSerilazers