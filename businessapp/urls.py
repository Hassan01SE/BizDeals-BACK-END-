from django.urls import path

from . import views

urlpatterns = [
    path('listings/', views.businessview),
    path('listings/<pk>', views.businessdetailview),
    
]