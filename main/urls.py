from django.urls import path
from . import views

urlpatterns = [
    path( '', views.index , name = 'index'),

    path('kia', views.kia, name='kia'),
    path('kia/k5', views.kiak5, name='kia-k5'),
    path('kia/seltos', views.seltos, name='kia-seltos'),
    path('hyundai', views.hyundai, name='hyundai'),
    path('chevrolet', views.chevrolet, name='chevrolet'),
    path('images', views.images, name='images'),
    path('contact', views.contact, name='contact'),
    path('news', views.news, name='news'),

    path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),
]