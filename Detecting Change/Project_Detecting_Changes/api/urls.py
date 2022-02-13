from django.urls import path
from .views import WeatherView

urlpatterns =[
    path('weather/', WeatherView.as_view(),name='weather_list'),
    path('weather/<int:id>', WeatherView.as_view(),name='weather_proces'),
    path('dataframe/', WeatherView.as_view(),name='dataframe')
]