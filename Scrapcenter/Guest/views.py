from django.shortcuts import render,redirect
from .models import*
from Administrator.models import*
from Guest.models import*
import random
from django.core.mail import send_mail
from django.conf import settings


def userregistration(request):
    userregistration_data=tbl_userregistration.objects.all()
    district_data=tbl_district.objects.all()
    place_data=tbl_place.objects.all()
    if request.method=='POST':
        name=request.POST.get("txt_name")
        email=request.POST.get("txt_email")
        contact=request.POST.get("txt_contact")
        address=request.POST.get("txt_address")
        gender=request.POST.get("rd_gender")
        dob=request.POST.get("date_DOB")
        photo=request.FILES.get("file_photo")
        password=request.POST.get("pswd_password")
        place = tbl_place.objects.get(id=request.POST.get("sel_place"))
        


        
        tbl_userregistration.objects.create(
            userregistration_name=name,
            userregistration_email=email,
            userregistration_contact=contact,
            userregistration_address=address,
            userregistration_gender=gender,
            userregistration_dob=dob,         
            userregistration_photo=photo,
            userregistration_password=password,
            place=place
            
        )
    
        return render(request,'Guest/UserRegistration.html',{"msg":"REGISTRATION COMPLETE"})
    else:
        return render(request,'Guest/UserRegistration.html',{'userregistration':userregistration_data,'place':place_data,'district':district_data})

def ajaxplace (request):
    did=request.GET.get('did')
    place=tbl_place.objects.filter(district=did)
    return render(request,'Guest/Ajaxplace.html',{'place':place})

    

def Login(request):
    if request.method == 'POST':
        email = request.POST.get("txt_Email")
        password = request.POST.get("pswd_password")

        UserCount = tbl_userregistration.objects.filter(
            userregistration_email=email,
            userregistration_password=password
        ).count()
        AdminCount = tbl_adminregistration.objects.filter(
            adminregistration_email=email,
            adminregistration_password=password
        ).count()
        ScrapcenterCount = tbl_ScrapcenterReg.objects.filter(
            scrapcenterreg_email=email,
            scrapcenterreg_password=password
        ).count()

        if UserCount > 0:
            userdata = tbl_userregistration.objects.get(
                userregistration_email=email,
                userregistration_password=password
            )
            if userdata.user_status == 0:
                return render(request, 'Guest/Login.html', {"msg": "Registration Pending"})
            elif userdata.user_status == 2:
                return render(request, 'Guest/Login.html', {"msg": "Registration Rejected"})
            else:
                request.session["uid"] = userdata.id
                return redirect("User:HomePage")

        elif ScrapcenterCount > 0:
            scrapdata = tbl_ScrapcenterReg.objects.get(
                scrapcenterreg_email=email,
                scrapcenterreg_password=password
            )
            if scrapdata.scraper_status == 0:
                return render(request, 'Guest/Login.html', {"msg": "Registration Pending"})
            elif scrapdata.scraper_status == 2:
                return render(request, 'Guest/Login.html', {"msg": "Registration Rejected"})
            else:
                request.session["sid"] = scrapdata.id
                return redirect("Scrapcenter:HomePage")

        elif AdminCount > 0:
            admindata = tbl_adminregistration.objects.get(
                adminregistration_email=email,
                adminregistration_password=password
            )
            request.session["aid"] = admindata.id
            return redirect("Administrator:HomePage")

        else:
            return render(request, 'Guest/Login.html', {"msg": "User Does not Exist"})

    else:
        return render(request, 'Guest/Login.html')





def scrapcenterreg(request):
    scrapcenterreg_data=tbl_ScrapcenterReg.objects.all()
    district_data=tbl_district.objects.all()
    place_data=tbl_place.objects.all()
    if request.method=='POST':
        name=request.POST.get("txt_name")
        email=request.POST.get("txt_email")
        contact=request.POST.get("txt_contact")
        address=request.POST.get("txt_address")
        estd=request.POST.get("date_DOB" )
        licensenumber=request.POST.get("txt_lisence")
        photo=request.FILES.get("file_photo")
        password=request.POST.get("pswd_password")
        place = tbl_place.objects.get(id=request.POST.get("sel_place"))
        


        
        tbl_ScrapcenterReg.objects.create(
            scrapcenterreg_name=name,
            scrapcenterreg_email=email,
            scrapcenterreg_contact=contact,
            scrapcenterreg_address=address,
            scrapcenterreg_lic=licensenumber,  
            scrapcenterreg_estd=estd,
            scrapcenterreg_photo=photo,
            scrapcenterreg_password=password,
            place=place
            
        )
    
        return render(request,'Guest/ScrapcenterReg.html',{"msg":"REGISTRATION COMPLETE"})
    else:
        return render(request,'Guest/ScrapcenterReg.html',{'scrapcenterreg':scrapcenterreg_data,'place':place_data,'district':district_data})

def index(request):
    return render(request,'Guest/index.html')


def forgotpassword(request):
    if request.method == "POST":
        email = request.POST.get("txt_email")
        user = tbl_userregistration.objects.get(userregistration_email=email)
        otp = random.randint(111111,999999)
        request.session["otp"] = otp
        request.session["uid"] = user.id
        send_mail(
            'Forgot password OTP', #subject
            "\rHello \r" + str(otp) +"\n This is the OTP to reset ur password.\n If you didn't ask to reset your password, you can ignore this email. \r\n Thanks. \r\n Your D MARKET team.",#body
            settings.EMAIL_HOST_USER,
            [email],
        )
        return render(request,"Guest/ForgotPassword.html",{"msg":email})
    else:
        return render(request,"Guest/ForgotPassword.html")



def otp(request):
    if request.method == "POST":
        inp_otp = int(request.POST.get("txt_otp"))
        if inp_otp == request.session["otp"]:
            return redirect("Guest:newpass")
        else:
            return render(request,"Guest/OTP.html",{"msg":"OTP Does not Matches..!!"})
    else:
        return render(request,"Guest/OTP.html")

def newpass(request):
    if request.method == "POST":
        user = tbl_userregistration.objects.get(id=request.session["uid"])
        if request.POST.get("txt_new_pass") == request.POST.get("txt_con_pass"):
            user.user_password = request.POST.get("txt_con_pass")
            user.save()
            return render(request,"Guest/NewPassword.html",{"msg1":"Password Updated Sucessfully...."})
        else:
            return render(request,"Guest/NewPassword.html",{"msg":"Error in confirm password..!!!"})
    else:
        return render(request,"Guest/NewPassword.html")