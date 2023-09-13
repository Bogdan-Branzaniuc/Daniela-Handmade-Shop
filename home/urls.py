from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home')
]

handler403 = 'home.views.handler403'
handler404 = 'home.views.handler404'
handler405 = 'home.views.handler405'
handler500 = 'home.views.handler500'

