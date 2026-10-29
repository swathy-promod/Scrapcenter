
from django.urls import path
from .import views
app_name='Administrator'

urlpatterns = [
    path('District/',views.district,name='District'),
    path("Districtdelete/<int:id>/",views.deletedistrict,name="Districtdelete"),
    path("Districtedit/<int:id>/",views.editdistrict,name="Districtedit"),

    path('Category/',views.category,name='Category'),
    path("Categorydelete/<int:id>/",views.deletecategory,name="Categorydelete"),
    path("Categoryedit/<int:id>/",views.editcategory,name="Categoryedit"),

    path('Place/',views.place,name='Place'),
    path("Placedelete/<int:id>/",views.deleteplace,name="Placedelete"),
    path("placeedit/<int:id>/",views.editplace,name="placeedit"),

    path('AdminRegistration/',views.adminregistration,name='AdminRegistration'),
    path("AdminRegistrationdelete/<int:id>/",views.deleteadminregistration,name="AdminRegistrationdelete"),
    path("AdminRegistrationedit/<int:id>/",views.editadminregistration,name="AdminRegistrationedit"),


    path('SubCategory/',views.subcategory,name='SubCategory'),
    path("SubCategorydelete/<int:id>/",views.deletesubcategory,name="SubCategorydelete"),
    path("SubCategoryedit/<int:id>/",views.editsubcategory,name="SubCategoryedit"),
    
    
    path('Brand/',views.brand,name='Brand'),
    path('editbrand/<int:id>/',views.editbrand,name='editbrand'),
    path('deletebrand/<int:id>/',views.deletebrand,name='deletebrand'),

    
    
    path('Type/',views.Type,name='Type'),

    path('HomePage/',views.HomePage,name="HomePage"),
    path('AdminProfile/', views.adminprofile, name='AdminProfile'),
    path('ChangePassword/', views.changepassword, name='ChangePassword'),
    path('AdminLogout/', views.AdminLogout, name='AdminLogout'),
    path("userlist/",views.userlist,name="userlist"),
    path("acceptuser/<int:uid>",views.useraccept,name="acceptuser"),
    path("rejectuser/<int:uid>",views.rejectuser,name="rejectuser"),
    path("Viewcomplaint/",views.viewcomplaint,name="Viewcomplaint"),
    path("ViewFeedback/",views.viewfeedback,name="ViewFeedback"),
    path("Reply/<int:id>/",views.reply,name="Reply"),


    path("scrapcenterlist/",views.scrapcenterlist,name="scrapcenterlist"),
    path("scraper_accept/<int:sid>",views.scraper_accept,name="scraper_accept"),
    path("rejectscraper/<int:sid>",views.rejectscraper,name="rejectscraper"),


    path('Model/',views.model,name='Model'),
    path('editmodel/<int:id>/',views.editmodel,name='editmodel'),
    path('deletemodel/<int:id>/',views.deletemodel,name='deletemodel'),
    


]
   
