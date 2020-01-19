from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views

app_name = 'report'

urlpatterns = [
    path('entries/', login_required(views.EntryView.as_view()), name='entry_list'),
    path('entries/<int:entry_id>', login_required(views.EntryView.as_view()), name='entry_list'),
    # path('entries/<pk>/', views.EntryDetailView.as_view(), name='entry_detail'),
]
