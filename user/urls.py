
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
path("",views.IndexPage,name = "index"),
path("about/",views.AboutPage,name="about"),
path("service/",views.ServicePage,name="service"),
path("project/",views.ProjectPage,name="project"),
path("contact/",views.ContactPage,name="contact"),
path("signup/",views.SignupPage,name="signup"),
path("register/",views.RegisterUser,name="register"),
path("otppage/",views.OtpPage,name="otppage"),
path("otpverify/",views.OtpVerify,name="otpverify"),
path("login/",views.LoginPage,name="loginpage"),
path("loginuser/",views.LoginUser,name="login"),

]
