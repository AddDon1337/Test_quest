from django.urls import path
from test_api import views


urlpatterns = [
    path('test_api/', views.deal_list),
    path('test_api/<int:pk>/', views.deal_detail),
]