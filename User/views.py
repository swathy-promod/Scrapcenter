from django.shortcuts import render,redirect
from .models import*
from Guest.models import*
from Scrapcenter.models import*

#ml import -------------------------------------------------------------------
import os
import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
import joblib

from django.db.models import Q
from datetime import datetime 

MODEL_PATH = os.path.join("Assets", "Model", "vehicle_weight_model.pkl")
loaded_pipeline = joblib.load(MODEL_PATH)

def Priceprediction(request):
    global loaded_pipeline
    if 'uid' not in request.session:
        return redirect('Guest:Login')
    brandadata=tbl_Brand.objects.all()
    typedata=tbl_Category.objects.all()
    if 'uid' in request.session:
        if request.method=='POST':
            brand=request.POST.get('SelectBrand')
            brand=tbl_Brand.objects.get(id=brand)
            brand=brand.brand_name

            typed=request.POST.get('SelectType')
            typed=tbl_Category.objects.get(id=typed)
            typed=typed.category_name

            model=request.POST.get('SelectModel')
            model=tbl_model.objects.get(id=model)
            model=model.model_name

            fuel=request.POST.get('SelectFuelType')

            sample = pd.DataFrame([{
                "vehicle_type": typed,
                "brand": brand,
                "vehicle_name": model,
                "fuel_type": fuel
            }])
            if loaded_pipeline is None:
                loaded_pipeline = joblib.load(MODEL_PATH)
            predicted_weight = loaded_pipeline.predict(sample)
            weight = round(float(predicted_weight[0]), 2)
            price=weight*30
            return render(request, 'User/Priceprediction.html',{'bname':brand,'mname':model,'predicted_weight':weight,'price':price,'brand':brandadata,'type':typedata})
        else:
            return render(request, 'User/Priceprediction.html',{'brand':brandadata,'type':typedata})
    else:
        return redirect("Guest:Login")

#end ml section-----------------------------------------------

def HomePage(request):
    if 'uid' not in request.session:
        return redirect('Guest:Login')
    
    user = tbl_userregistration.objects.get(id=request.session['uid'])
    return render(request, 'User/HomePage.html', {'user': user})



def MyProfile(request):
    data=tbl_userregistration.objects.get(id=request.session['uid'])
    return render(request,'User/MyProfile.html',{'data':data})



def editprofile(request):
    editprofile=tbl_userregistration.objects.get(id=request.session['uid'])
    if request.method=='POST':
        name=request.POST.get("txtname")
        email=request.POST.get("txtemail")
        contact=request.POST.get("num_number")
        address=request.POST.get("txtaddress")
        editprofile.userregistration_name=name
        editprofile.userregistration_email=email
        editprofile.userregistration_contact=contact
        editprofile.userregistration_address=address
        editprofile.save() 
        return render(request,'User/MyProfile.html',{'msg':"profile updated"}) 
    else:
        return render(request,'User/EditProfile.html',{'data':editprofile}) 

  


def ChangePassword(request):
    user=tbl_userregistration.objects.get(id=request.session['uid'])
    if request.method=='POST':
        old_password = request.POST.get("txt_password")
        new_password = request.POST.get("txt_newpassword")
        retype_password = request.POST.get("txt_retypepassword")
        if user.userregistration_password==old_password:
            if new_password == retype_password:
                user.userregistration_password=new_password
                user.save()
                return render(request,'User/MyProfile.html',{"msg":"Passwordchanged Successfully"}) 
            else:
                return render(request,"User/ChangePassword.html",{"msg":"New password do not match"})
        else:
            return render(request,"User/ChangePassword.html",{"msg":"old password incorrect"})
    else:
        return render(request,"User/changepassword.html") 



def Complaint(request):
    if 'uid' not in request.session:
        return redirect('Guest:Login')
    
    success = False
    if request.method == 'POST':
        title   = request.POST.get("txtname")
        content = request.POST.get("txt_content")
        tbl_complaint.objects.create(
            complaint_title   = title,
            complaint_content = content,
            user = tbl_userregistration.objects.get(id=request.session['uid'])
        )
        success = True

    complaintdata = tbl_complaint.objects.filter(user=request.session['uid'])
    return render(request, "User/Complaint.html", {
        'Viewcomplaint': complaintdata,
        'success': success
    })

def deletecomplaint(request, id):  
    tbl_complaint.objects.get(id=id).delete()
    return redirect("User:Complaint")





def feedback(request):
    if 'uid' not in request.session:
        return redirect('Guest:Login')
    
    success = False
    if request.method == 'POST':
        content = request.POST.get("txt_feed")
        tbl_feedback.objects.create(
            feedback_content = content,
            user = tbl_userregistration.objects.get(id=request.session['uid'])
        )
        success = True

    feedback_data = tbl_feedback.objects.filter(user=request.session['uid'])
    return render(request, "User/Feedback.html", {
        'Feedback': feedback_data,
        'success': success
    })



def addvehicle(request):
    addvehicle_data=tbl_addvehicle.objects.all()
    district_data=tbl_district.objects.all()
    place_data=tbl_place.objects.all()
    model_data=tbl_model.objects.all()
    brand_data=tbl_Brand.objects.all()    
    if request.method=='POST':
        number=request.POST.get("txtno")
        fuel=request.POST.get("txtfuel")
        gear=request.POST.get("txtgear")
        cond=request.POST.get("txtcond")
        discription=request.POST.get("txtdiscription" )
        mile=request.POST.get("txtmile")
        rc=request.POST.get("rc")
        Status=request.POST.get("Status")
        Ins=request.POST.get("Ins")
        photo=request.FILES.get("txt_file")
        place = tbl_place.objects.get(id=request.POST.get("sel_place"))
        model = tbl_model.objects.get(id=request.POST.get("sel_model"))

        


        
        tbl_addvehicle.objects.create(
            vehicle_year=number,
            vehicle_fuel=fuel,
            transmission_type=gear,
            vehicle_condition=cond,
            vehicle_discription=discription,  
            vehicle_status=Status,
            vehicle_mileage=mile,
            vehicle_photo=photo,
            vehicle_RC=rc,
            insurence_status=Ins,
            place=place,
            model=model,
            user = tbl_userregistration.objects.get(id=request.session['uid'])

            
        )
    
        return render(request,'User/AddVehicle.html',{'msg':"VEHICLE ADDED"})
    else:
        return render(request,'User/AddVehicle.html',{'addvehicle_data':addvehicle_data,'place':place_data,'district':district_data,'model':model_data,'brand':brand_data})

        
              

def ajaxmodel (request):
    did=request.GET.get('did')
    model=tbl_model.objects.filter(brand=did)
    return render(request,'User/ajaxmodel.html',{'model':model})


def viewreqst(request):
    data=tbl_scraprequest.objects.all()
    return render(request,'User/ViewReqst.html',{'viewreqst': data})





def rejectscraper(request,sid):
    scraper_reject=tbl_scraprequest.objects.get(id=sid)
    scraper_reject.request_status=2
    scraper_reject.save()
    return render(request,'User/ViewReqst.html',{'msg':"Rejected"})




def scraper_accept(request,sid):
    accdata=tbl_scraprequest.objects.get(id=sid)
    accdata.request_status=1
    accdata.save()
    return render(request,'User/ViewReqst.html',{'msg':"Accepted"})


