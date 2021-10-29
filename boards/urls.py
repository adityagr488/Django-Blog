from django.urls import path
from boards import views
urlpatterns = [
    path("",views.home,name="home"),
    path("myblog",views.myblog,name="myblog"),
    path("registration",views.registration,name="registration"),
    path("loginuser",views.loginuser,name="login"),
    path("logoutuser",views.logoutuser,name="logout")
]