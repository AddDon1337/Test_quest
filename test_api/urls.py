from django.urls import path
from test_api import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('test_api/', views.deal_list),
    path('test_api/<int:pk>/', views.deal_detail)
]

urlpatterns = format_suffix_patterns(urlpatterns)