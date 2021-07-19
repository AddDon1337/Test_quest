from django.urls import path
from test_api import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('test_api/', views.DealList.as_view()),
    path('test_api/<int:pk>/', views.DealDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)