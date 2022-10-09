from django.urls import path
from .views import generate_password, password, sorry

app_name = 'generator'

urlpatterns = [
    path('', generate_password, name='gen'),
    path('password/', password, name='pwd'),
    path('oh_my_god/', sorry, name='sorry')
]