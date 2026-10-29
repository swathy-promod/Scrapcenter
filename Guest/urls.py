from django.urls import path
from .import views
app_name='Guest'

urlpatterns = [
    path('userregistration/',views.userregistration,name='userregistration'),
    path('ajaxplace /',views.ajaxplace,name='ajaxplace'),
    path('Login/',views.Login,name='Login'),
    path('ScrapcenterReg/',views.scrapcenterreg,name='ScrapcenterReg'),
    path('',views.index,name='index'),
    path('forgotpassword/',views.forgotpassword,name="forgotpassword"),
    path('otp/',views.otp,name="otp"),
    path('newpass/',views.newpass,name="newpass"),

]