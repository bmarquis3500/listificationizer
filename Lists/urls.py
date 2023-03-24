from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.loginPage, name ='login'),
    path('',views.home, name ='home'),
    path('register/',views.RegisterUser, name ='register'),
    path('logout/',views.logoutUser, name ='logout'),

    path('list/<str:pk>/', views.list, name = 'list'),
    path('list/<str:pk>/delete/', views.deleteItem, name = 'item_delete'),
    path('<str:pk>/delete/', views.deleteList, name = 'list_delete'),
    
]
