
from django.urls import path
from .import views
app_name='Basics'

urlpatterns = [
    path('calculator/',views.calculator,name='calculator'),
    path('largest/',views.largest,name='largest'),
    path('largestof3/',views.largestof3,name='largestof3'),
    path('sum/',views.Sum,name='sum'),
    
    


]
   
