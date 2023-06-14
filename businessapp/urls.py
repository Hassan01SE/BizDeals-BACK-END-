from django.urls import path

from . import views

app_name = 'businessapp'

urlpatterns = [
    path('listings/', views.BusinessListView.as_view(), name='business-list'),
    path('listings/<pk>', views.BusinessDetailView.as_view(), name='business-detail'),
    path('purchases/', views.PurchaseListView.as_view(), name='purchase-list'),
    
]