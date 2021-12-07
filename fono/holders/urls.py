from django.urls import path
from .views import HolderCreate

app_name = 'holder'
urlpatterns = [
    path('', HolderCreate.as_view(), name='new')
]
