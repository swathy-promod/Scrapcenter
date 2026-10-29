from django.shortcuts import render,redirect
from Administrator.models import*
from Guest.models import*
from User.models import*
from .models import*




def homepage(request):
    scrap=tbl_ScrapcenterReg.objects.get(id=request.session['sid'])
    return render(request,'Scrapcenter/HomePage.html',{'scrap':scrap})

    
def myprofile(request):
    data=tbl_ScrapcenterReg.objects.get(id=request.session['sid'])
    return render(request,'Scrapcenter/MyProfile.html',{'data':data})


def changepassword(request):
    scrap=tbl_ScrapcenterReg.objects.get(id=request.session['sid'])
    if request.method=='POST':
        old_password = request.POST.get("old_pw")
        new_password = request.POST.get("new_pw")
        retype_password = request.POST.get("retype_pw")
        if scrap.scrapcenterreg_password==old_password:
            if new_password == retype_password:
                scrap.scrapcenterreg_password=new_password
                scrap.save()
                return render(request,'Scrapcenter/MyProfile.html',{"msg":"Passwordchanged Successfully"}) 
            else:
                return render(request,"Scrapcenter/Changepassword.html",{"msg":"New password do not match"})
        else:
            return render(request,"Scrapcenter/Changepassword.html",{"msg":"old password incorrect"})
    else:
        return render(request,"Scrapcenter/Changepassword.html") 



def editprofile(request):
    editprofile=tbl_ScrapcenterReg.objects.get(id=request.session['sid'])
    if request.method=='POST':
        name=request.POST.get("txtname")
        email=request.POST.get("txtemail")
        contact=request.POST.get("num_number")
        address=request.POST.get("txtaddress")
        editprofile.scrapcenterreg_name=name
        editprofile.scrapcenterreg_email=email
        editprofile.scrapcenterreg_contact=contact
        editprofile.scrapcenterreg_address=address
        editprofile.save() 
        return render(request,'Scrapcenter/MyProfile.html',{'msg':"profile updated"}) 
    else:
        return render(request,'Scrapcenter/Editprofile.html',{'data':editprofile}) 



def vehiclelist(request):
    data=tbl_addvehicle.objects.all()
    return render(request,'Scrapcenter/Vehiclelist.html',{'Vehiclelist':data})


def requestscrap(request,vid):
    ScrapCount=tbl_scraprequest.objects.filter(vehicle=vid,scrapcenter=request.session['sid']).count()
    if ScrapCount>0:
        return render(request,'Scrapcenter/Request.html',{'msg':"Request Already Send"})
    else: 
        if request.method == "POST":
            prize=request.POST.get("txt_prize")
            remark=request.POST.get("txt_remark")
            
            tbl_scraprequest.objects.create(
                vehicle=tbl_addvehicle.objects.get(id=vid),
                scrapcenter=tbl_ScrapcenterReg.objects.get(id=request.session['sid']),
                request_remark=remark,
                offered_prize=prize,

            )
            return render(request,'Scrapcenter/Request.html',{'msg':"REQUEST SEND "})

        else:
            return render(request,'Scrapcenter/Request.html')


def myrequest(request):
    data=tbl_scraprequest.objects.filter(scrapcenter=request.session['sid'])
    return render(request,'Scrapcenter/MyRequest.html',{'data':data})


def payment(request,rid):
    data=tbl_scraprequest.objects.get(id=rid)
    amount = data.offered_prize
    if request.method == "POST":
        data.request_status = 3
        data.save()
        return redirect("Scrapcenter:MyRequest")
    else:
        return render(request,'Scrapcenter/Payment.html',{'amount':amount})


def Complaint(request):
    success = False
    if request.method == 'POST':
        title   = request.POST.get("txtname")
        content = request.POST.get("txt_content")
        tbl_complaint.objects.create(
            complaint_title   = title,
            complaint_content = content,
            scrap = tbl_ScrapcenterReg.objects.get(id=request.session['sid'])
        )
        success = True

    complaintdata = tbl_complaint.objects.filter(scrap=request.session['sid'])
    return render(request, "Scrapcenter/Complaint.html",{
        'Viewcomplaint': complaintdata,
        'success': success
    })



def feedback(request):
    success = False
    if request.method == 'POST':
        content = request.POST.get("txt_feed")
        tbl_feedback.objects.create(
            feedback_content = content,
            scrap = tbl_ScrapcenterReg.objects.get(id=request.session['sid'])
        )
        success = True 
        
    feedback = tbl_feedback.objects.filter(scrap=request.session['sid'])
    return render(request, "Scrapcenter/Feedback.html", {
        'Feedback': feedback,
        'success': success
    })