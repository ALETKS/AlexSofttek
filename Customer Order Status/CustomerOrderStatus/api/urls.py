from django.urls import path
from .views import OrderView
urlpatterns = [
    path('orders/', OrderView.as_view(), name='order_list'),
    path('dataframe/', OrderView.as_view(),name='dataframe')
]