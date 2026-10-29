from django.urls import path
from .import views
app_name='Scrapcenter'


urlpatterns = [
    path ('MyProfile/',views.myprofile,name='MyProfile'),
    path('HomePage/',views.homepage,name="HomePage"),
    path('Changepassword/',views.changepassword,name="Changepassword"),
    path('Editprofile/',views.editprofile,name="Editprofile"),
    path('Vehiclelist/',views.vehiclelist,name="Vehiclelist"),
    path("requestscrap/<int:vid>/",views.requestscrap,name="requestscrap"),
    path("MyRequest/",views.myrequest,name="MyRequest"),
    path('Payment/<int:rid>',views.payment,name="Payment"),


    path('Complaint/',views.Complaint,name='Complaint'),
    path('Feedback/',views.feedback,name='Feedback'),

]