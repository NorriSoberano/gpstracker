from django.urls import path
from .views import GPSDataListCreateView

urlpatterns = [
    path('gpsdata/', GPSDataListCreateView.as_view(), name='gpsdata-list-create'),
]
