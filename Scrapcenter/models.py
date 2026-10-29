from django.db import models
from Administrator.models import*
from Guest.models import*
from User.models import*


class tbl_scraprequest(models.Model):
    request_status=models.IntegerField(default=0)
    request_date=models.DateField(auto_now_add=True)
    request_remark=models.CharField(max_length=100)
    offered_prize=models.CharField(max_length=100)
    vehicle=models.ForeignKey(tbl_addvehicle,on_delete=models.CASCADE,null=True,blank=True)  
    scrapcenter=models.ForeignKey(tbl_ScrapcenterReg,on_delete=models.CASCADE,null=True,blank=True) 
   
