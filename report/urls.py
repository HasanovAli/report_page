from django.urls import path
from . import views


app_name = 'report'


urlpatterns = [
    path('readme/', views.readme, name='readme')
]
