from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Radar
# Register your models here.

class Radar_Admin(admin.ModelAdmin):

    list_displey=[
        "car_number",
        "car_tezlik",
        "car_jarima",
        "vaqt"
    ]

    ordering=[
        "-vaqt",
        "car_number",
        "-car_tezlik",
    ]

    search_fields=[
        "car_number"
    ]

    list_filter=[
        "car_number",
        "car_tezlik",
        "car_jarima",
        "vaqt",
    ]

    list_per_page = 3

admin.site.register(Radar, Radar_Admin)
