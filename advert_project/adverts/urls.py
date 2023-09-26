from django.urls import path
from . import views

urlpatterns = [
    path('advert-list/', views.AdvertList.as_view(), name='advert-list'),
    path('advert/<int:pk>/', views.AdvertDetail.as_view(), name='advert-detail'),
]
