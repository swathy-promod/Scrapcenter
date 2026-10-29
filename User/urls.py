from django.urls import path
from .import views
app_name='User'

urlpatterns = [
    path('MyProfile/',views.MyProfile,name='MyProfile'),

    path('Editprofile/',views.editprofile,name="Editprofile"),
   

    path('ChangePassword/',views.ChangePassword,name="ChangePassword"),
    path('HomePage/',views.HomePage,name="HomePage"),

    path('Complaint/',views.Complaint,name='Complaint'),
    path('Feedback/',views.feedback,name='Feedback'),
    path("Deletecomplaint/<int:id>/",views.deletecomplaint,name="Deletecomplaint"),



    path('AddVehicle/',views.addvehicle,name='AddVehicle'),
    path('ajaxmodel /',views.ajaxmodel,name='ajaxmodel'),

    path('Priceprediction/',views.Priceprediction,name='Priceprediction'),

    path("ViewReqst/",views.viewreqst,name="ViewReqst"),
    path("scraper_accept/<int:sid>",views.scraper_accept,name="scraper_accept"),
    path("rejectscraper/<int:sid>",views.rejectscraper,name="rejectscraper"),




]
