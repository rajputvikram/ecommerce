from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('detail/<int:pk>', views.ProductDetail.as_view(), name='detail'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
