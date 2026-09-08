from django.urls import path, include
from .views import jarima_info
from .views import Radarwiewset
from rest_framework import routers

router=routers.DefaultRouter()
router.register(r"radar",Radarwiewset)


urlpatterns=[
    path('jarima/',jarima_info,name='jarimalar'),
    path('',include(router.urls))
]