from django.db import models
from Guest.models import*
from Administrator.models import*



class tbl_complaint(models.Model):
    complaint_title=models.CharField(max_length=100)
    complaint_content=models.CharField(max_length=100) 
    complaint_date=models.DateField(auto_now_add=True)
    complaint_status=models.IntegerField(default=0)
    complaint_reply=models.CharField(max_length=100)
    user=models.ForeignKey(tbl_userregistration,on_delete=models.CASCADE,null=True,blank=True)  
    scrap=models.ForeignKey(tbl_ScrapcenterReg,on_delete=models.CASCADE,null=True,blank=True) 
 
class tbl_feedback(models.Model):
    feedback_content=models.CharField(max_length=100) 
    feedback_date=models.DateField(auto_now_add=True)
    user=models.ForeignKey(tbl_userregistration,on_delete=models.CASCADE,null=True,blank=True)
    scrap=models.ForeignKey(tbl_ScrapcenterReg,on_delete=models.CASCADE,null=True,blank=True)


class tbl_addvehicle(models.Model):
    vehicle_year=models.CharField(max_length=100)
    listed_date=models.DateField(auto_now_add=True)
    vehicle_fuel=models.CharField(max_length=100)
    transmission_type=models.CharField(max_length=100) 
    vehicle_condition=models.CharField(max_length=100)
    vehicle_discription=models.CharField(max_length=100) 
    vehicle_status=models.CharField(max_length=100)
    vehicle_mileage=models.CharField(max_length=100) 
    vehicle_RC=models.CharField(max_length=100) 
    insurence_status=models.CharField(max_length=100)
    vehicle_photo = models.FileField(upload_to = 'Assets/User/Photos/')
    place=models.ForeignKey(tbl_place,on_delete=models.CASCADE,null=True,blank=True)  
    model=models.ForeignKey(tbl_model,on_delete=models.CASCADE,null=True,blank=True) 
    user=models.ForeignKey(tbl_userregistration,on_delete=models.CASCADE,null=True,blank=True)

