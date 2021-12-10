from django.urls import path
from .views import HolderCreate, holder_create

app_name = 'holder'
urlpatterns = [
    # path('', HolderCreate.as_view(), name='new')
    path('', holder_create, name='new')
]
