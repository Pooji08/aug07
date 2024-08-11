from django.urls import path
from app1 import views
urlpatterns=[
    path('create',views.create,name="createpage"),
    path('',views.home,name="homepage"),
    path('login',views.loginv,name="loginpage"),
    path('profile',views.profile,name="profilepage"),
    path('register',views.register,name="registerpage"),
    path('single',views.single,name="singlepage"),
    path('logout',views.logoutv,name="logoutpage"),
] 