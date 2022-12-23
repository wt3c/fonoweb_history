from django.urls import path
from .views import ManagerHolder

app_name = 'holder'
urlpatterns = [
    path('', ManagerHolder.as_view(), name='new'),
]
