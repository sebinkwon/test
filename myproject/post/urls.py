from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('move/',views.move, name="move"),
    path('add/',views.add,name="add"),
    path('delete/<int:pk>', views.delete, name="delete"),
    path('edit/<int:pk>', views.edit, name="edit"),
    path('login/', auth_views.LoginView.as_view(),name="login"),
    path('logout/', auth_views.LogoutView.as_view(),name="logout"),
    path('signup/', views.sign_up,name="sign_up"),
]
