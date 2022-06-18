from django.urls import path
from main import views

urlpatterns = [
    path('', views.home, name='home'),
    path('hi/', views.hi),
    path('hello/', views.hello, ),
    path('create/', views.create, name='create'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('student/<int:id>/', views.read, name='read'),
]

