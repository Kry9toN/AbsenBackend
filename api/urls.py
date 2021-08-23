from django.urls import path, include

from . import views

urlpatterns = [
    path('user/', views.ListUser.as_view()),
    path('<int:pk>/', views.DetailUser.as_view()),
    path('', include('rest_auth.urls')),
    path('register/', views.registration_view, name='register'),
    path('absen/', views.absen_view, name='absen')
]