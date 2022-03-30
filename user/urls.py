
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
path("profile/<int:pk>/",views.ProfilePage,name="profile"),
path("updateprofile<int:pk>//",views.UpdateProfile,name="updateprofile"),

#############Housekeeper####################
path("housekeeperindex/",views.HousekeeperIndexPage,name="housekeeperindex"),
path("housekeeperprofile/<int:pk>/",views.HousekeeperProfilePage,name="housekeeperprofile"),
path("housekeeperupdateprofile/<int:pk>/",views.HousekeeperUpdateProfile,name="housekeeperupdateprofile"),



]

from django.conf import settings

from django.conf.urls.static import static

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)