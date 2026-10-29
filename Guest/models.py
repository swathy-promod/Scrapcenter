from django.db import models
from Administrator.models import*
class tbl_userregistration(models.Model):
    userregistration_name=models.CharField(max_length=100) 
    userregistration_email=models.CharField(max_length=100)
    userregistration_contact=models.CharField(max_length=100) 
    userregistration_address=models.CharField(max_length=100) 
    userregistration_gender=models.CharField(max_length=100) 
    userregistration_dob=models.DateField(max_length=100) 
   
    place=models.ForeignKey(tbl_place,on_delete=models.CASCADE,null=True,blank=True)  
    userregistration_photo = models.FileField(upload_to = 'Assets/User/Photos/')
    userregistration_password=models.CharField(max_length=100)
    user_status=models.IntegerField(default=0)

class tbl_ScrapcenterReg(models.Model):
    scrapcenterreg_name=models.CharField(max_length=100) 
    scrapcenterreg_email=models.CharField(max_length=100)
    scrapcenterreg_contact=models.CharField(max_length=100) 
    scrapcenterreg_address=models.CharField(max_length=100)
    scrapcenterreg_lic=models.CharField(max_length=100) 
    scrapcenterreg_estd=models.DateField(max_length=100) 
    place=models.ForeignKey(tbl_place,on_delete=models.CASCADE,null=True,blank=True)  
    scrapcenterreg_photo = models.FileField(upload_to = 'Assets/Guest/Photos/')
    scrapcenterreg_password=models.CharField(max_length=100)
    scraper_status=models.IntegerField(default=0)



