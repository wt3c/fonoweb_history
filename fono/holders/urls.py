from django.urls import path
from .views import New

app_name = 'holders'
urlpatterns = [
    path('', New.as_view(), name='new')
]
