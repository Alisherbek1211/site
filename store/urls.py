from django.urls import path
from .views import home,single_news


urlpatterns = [
    path('',home),
    path('1/',single_news),
]