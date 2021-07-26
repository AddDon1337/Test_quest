from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import home_view


urlpatterns = [

    path('api_file/', home_view),

]

urlpatterns = format_suffix_patterns(urlpatterns)