from .models import Radar
from rest_framework import serializers

class RadarSerilazers(serializers.ModelSerializer):
    class Meta:
        model=Radar
        fields="__all__"
        # fields=[
        #     "car_number",
        #     "car_tezlik",
        # ]
