from django.urls import path
from .views import *

urlpatterns = [ 
    path('home/', home),
    path('about/', about),
    path('contact/', contact),
    path('services/', services),
    path('mainapp/', mainapp_view),
    path('mainapp_show/', mainapp_show),
    path('deleteproduct/<str:pk>/', deleteproduct),
]