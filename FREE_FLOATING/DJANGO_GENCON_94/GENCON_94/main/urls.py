from django.urls import path
from . import views

urlpatterns = [
    path('', views.start_page, name='start_page'),
    path('about', views.about, name='about'),
    path('fixing', views.fixing, name='fixing')
]