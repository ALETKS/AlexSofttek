from django.urls import path
from .views import SeasonView
urlpatterns = [
    path('season/', SeasonView.as_view(), name='season_list'),
    path('dataframe/', SeasonView.as_view(),name='dataframe')
]