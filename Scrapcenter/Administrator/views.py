from django.shortcuts import render,redirect
from .models import*
from User.models import*
from Scrapcenter.models import*
from Guest.models import*
from django.contrib import messages 

def district(request):
    district_data=tbl_district.objects.all()
    if request.method=='POST':
        district = request.POST.get("txtname")
        tbl_district.objects.create(
            district_name=district
        )
        return redirect("Administrator:District")
    else:
        return render(request,'Administrator/District.html',{'district':district_data})
def deletedistrict(request, id):  
    tbl_district.objects.get(id=id).delete()
    return redirect("Administrator:District")
def editdistrict(request,id):
    editdistrict=tbl_district.objects.get(id=id)
    if request.method=='POST':
        name=request.POST.get("txtname")
        editdistrict.district_name=name
        editdistrict.save() 
        return redirect("Administrator:District")
    else:
        return render(request,'Administrator/District.html',{'data':editdistrict})   

def category(request):
    category_data=tbl_Category.objects.all()
    if request.method=='POST':
        category = request.POST.get("txtname")
        tbl_Category.objects.create(
            category_name=category
        )
        return redirect("Administrator:Category")
    else:
        return render(request,'Administrator/Category.html',{'category':category_data})
def deletecategory(request, id):  
    tbl_Category.objects.get(id=id).delete()
    return redirect("Administrator:Category")        
def editcategory(request,id):
    editcategory=tbl_Category.objects.get(id=id)
    if request.method=='POST':
        name=request.POST.get("txtname")
        editcategory.category_name=name
        editcategory.save() 
        return redirect("Administrator:Category")
    else:
        return render(request,'Administrator/Category.html',{'data':editcategory})   

def place(request):
    district_data=tbl_district.objects.all()
    place_data=tbl_place.objects.all()
    if request.method== 'POST':
        place = request.POST.get("txtplace")
        district_id = request.POST.get("sel_dis")
        district_obj=tbl_district.objects.get(id=district_id)
        tbl_place.objects.create(
            place_name=place,
            district=district_obj
        )
        return redirect("Administrator:Place")
    else:
        return render(request,'Administrator/Place.html',{'place':place_data,'district':district_data})

def editplace(request,id):
    district_data=tbl_district.objects.all()
    editplace=tbl_place.objects.get(id=id)
    if request.method== 'POST':
        place = request.POST.get("txtname")
        editplace.place_name=place
        district_id = request.POST.get("sel_dis")
        district_obj=tbl_district.objects.get(id=district_id)
        editplace.district = district_obj
        editplace.save()
        return redirect("Administrator:Place")
    else:
        return render(request,'Administrator/Place.html',{'data':editplace,'district':district_data})


def deleteplace(request,id):  
    tbl_place.objects.get(id=id).delete()
    return redirect("Administrator:District")
def adminregistration(request):
    adminregistration_data=tbl_adminregistration.objects.all()
    if request.method=='POST':
        name=request.POST.get("txtname")
        email=request.POST.get("txt_email")
        password=request.POST.get("txt_password")
        tbl_adminregistration.objects.create(
            adminregistration_name=name,
            adminregistration_email=email,
            adminregistration_password=password
        )
        return redirect("Administrator:AdminRegistration")
    else:
        return render(request,'Administrator/AdminRegistration.html',{'adminregistration':adminregistration_data})
def deleteadminregistration(request, id):  
    tbl_adminregistration.objects.get(id=id).delete()
    return redirect("Administrator:AdminRegistration")
def editadminregistration(request,id):
    editadminregistration=tbl_adminregistration.objects.get(id=id)
    if request.method=='POST':
        name=request.POST.get("txtname")
        email=request.POST.get("txt_email")
        password=request.POST.get("txt_password")
        editadminregistration.adminregistration_name=name
        editadminregistration.adminregistration_email=email
        editadminregistration.adminregistration_password=password

        editadminregistration.save() 
        return redirect("Administrator:AdminRegistration")
    else:
        return render(request,'Administrator/AdminRegistration.html',{'data':editadminregistration})   

def subcategory(request):
    category_data=tbl_Category.objects.all()
    subcategory_data=tbl_subcategory.objects.all()
    if request.method== 'POST':
        subcategory = request.POST.get("txtname")
        category_id= request.POST.get("sel_qus")
        category_data=tbl_Category.objects.get(id=category_id)
        tbl_subcategory.objects.create(
            subcategory_name=subcategory,
            category=category_data

        )
        return redirect("Administrator:SubCategory")
    else:
        return render(request,'Administrator/SubCategory.html',{'subcategory':subcategory_data,'category':category_data})

def editsubcategory(request,id):
    category_data=tbl_Category.objects.all()
    editsubcategory=tbl_subcategory.objects.get(id=id)
    if request.method=='POST':
        name=request.POST.get("txtname")
        editsubcategory.subcategory_name=name
        category_id = request.POST.get("sel_qus")
        category_obj=tbl_subcategory.objects.get(id=id)
        editsubcategory.tbl_Category= category_obj
        editsubcategory.save() 
        return redirect("Administrator:SubCategory")
    else:
        return render(request,'Administrator/SubCategory.html',{'data':editsubcategory,'category':category_data})
    
       
        
def deletesubcategory(request, id):  
    tbl_subcategory.objects.get(id=id).delete()
    return redirect("Administrator:SubCategory") 

def Type(request):
    if request.method=='POST':
        Type = request.POST.get("txtname")
        tbl_Category.objects.create(
            Type_name=Type
        )
        return redirect("Administrator:Type")
    else:
        return render(request,'Administrator/Type.html')


def AdminLogout(request):
    request.session.flush()
    return redirect('Guest:Login')


def adminprofile(request):
    admin_id = request.session.get('aid')
    if not admin_id:
        return redirect('Guest:Login')
    try:
        admin = tbl_adminregistration.objects.get(id=admin_id)
    except tbl_adminregistration.DoesNotExist:
        return redirect('Guest:Login')
    return render(request, 'Administrator/AdminProfile.html', {'admin': admin})


def changepassword(request):
    admin_id = request.session.get('aid')
    if not admin_id:
        return redirect('Guest:Login')

    try:
        admin = tbl_adminregistration.objects.get(id=admin_id)
    except tbl_adminregistration.DoesNotExist:
        request.session.flush()
        return redirect('Guest:Login')

    msg = None
    msg_type = 'danger'  # bootstrap alert color

    if request.method == 'POST':
        old_password     = request.POST.get('old_password', '').strip()
        new_password     = request.POST.get('new_password', '').strip()
        confirm_password = request.POST.get('confirm_password', '').strip()

        # ── Validation ───────────────────────────────────────────────────────
        if not old_password or not new_password or not confirm_password:
            msg = 'All fields are required.'

        elif admin.adminregistration_password != old_password:
            msg = 'Old password is incorrect.'

        elif new_password == old_password:
            msg = 'New password must be different from the old password.'

        elif len(new_password) < 6:
            msg = 'New password must be at least 6 characters.'

        elif new_password != confirm_password:
            msg = 'New password and confirm password do not match.'

        else:
            try:
                admin.adminregistration_password = new_password
                admin.save()
                msg = 'Password changed successfully!'
                msg_type = 'success'
            except Exception as e:
                msg = f'An error occurred while saving: {str(e)}'

    return render(request, 'Administrator/ChangePassword.html', {
        'admin':    admin,
        'msg':      msg,
        'msg_type': msg_type,
    })
def HomePage(request):
    # ── Auth guard ──────────────────────────────────────────────────────────
    admin_id = request.session.get('aid')
    if not admin_id:
        return redirect('Guest:Login')

    try:
        admin = tbl_adminregistration.objects.get(id=admin_id)
    except tbl_adminregistration.DoesNotExist:
        return redirect('Guest:Login')

    # ── Recent Verifications ─────────────────────────────────────────────────
    recent_verifications = []

    for u in tbl_userregistration.objects.order_by('-id')[:3]:
        recent_verifications.append({
            'name':     u.userregistration_name,
            'type':     'User',
            'district': u.place.district.district_name if u.place and u.place.district else '-',
            'date':     '-',
            'status':   'Approved' if u.user_status == 1 else 'Pending',
        })

    for s in tbl_ScrapcenterReg.objects.order_by('-id')[:3]:
        recent_verifications.append({
            'name':     s.scrapcenterreg_name,
            'type':     'Scrap Center',
            'district': s.place.district.district_name if s.place and s.place.district else '-',
            'date':     '-',
            'status':   'Approved' if s.scraper_status == 1 else 'Pending',
        })

    # ── Recent Activity ──────────────────────────────────────────────────────
    recent_activity = []

    for u in tbl_userregistration.objects.order_by('-id')[:2]:
        recent_activity.append({
            'color':   'blue',
            'icon':    'account-plus',
            'message': f"New user registered: {u.userregistration_name}",
            'time':    'Recently',
        })

    for s in tbl_ScrapcenterReg.objects.order_by('-id')[:2]:
        recent_activity.append({
            'color':   'green',
            'icon':    'recycle',
            'message': f"Scrap center registered: {s.scrapcenterreg_name}",
            'time':    'Recently',
        })

    for c in tbl_complaint.objects.order_by('-complaint_date')[:2]:
        recent_activity.append({
            'color':   'red',
            'icon':    'alert-circle',
            'message': f"New complaint: {c.complaint_title}",
            'time':    str(c.complaint_date),
        })

    for v in tbl_addvehicle.objects.order_by('-listed_date')[:2]:
        recent_activity.append({
            'color':   'amber',
            'icon':    'car',
            'message': f"Vehicle listed: {v.model} ({v.vehicle_year})",
            'time':    str(v.listed_date),
        })

    context = {
        'admin': admin,

        # Stat cards
        'total_users':        tbl_userregistration.objects.count(),
        'total_scrapcenters': tbl_ScrapcenterReg.objects.count(),
        'total_vehicles':     tbl_addvehicle.objects.count(),
        'pending_complaints': tbl_complaint.objects.filter(complaint_status=0).count(),

        # Summary
        'total_districts': tbl_district.objects.count(),
        'total_places':    tbl_place.objects.count(),
        'total_brands':    tbl_Brand.objects.count(),
        'total_models':    tbl_model.objects.count(),

        # Table + feed
        'recent_verifications': recent_verifications,
        'recent_activity':      recent_activity,
    }

    return render(request, 'Administrator/HomePage.html', context)

def userlist(request):
    data=tbl_userregistration.objects.all()
    return render(request,'Administrator/userlist.html',{'userregistration': data})

def useraccept(request,uid):
    accdata=tbl_userregistration.objects.get(id=uid)
    accdata.user_status=1
    accdata.save()
    return render(request,'Administrator/userlist.html',{'msg':"Accepted"})

def rejectuser(request,uid):
    userreject=tbl_userregistration.objects.get(id=uid)
    userreject.user_status=2
    userreject.save()
    return render(request,'Administrator/userlist.html',{'msg':"Rejected"})
# Create your views here.



def reply(request, id):
    complaint = tbl_complaint.objects.get(id=id)
    
    if request.method == 'POST':
        reply = request.POST.get("txt_reply")
        complaint.complaint_reply = reply
        complaint.complaint_status = 1
        complaint.save()
        return redirect('Administrator:Viewcomplaint')
    else:
        return render(request, 'Administrator/Reply.html', {'complaint': complaint})



def viewcomplaint(request):
    viewcomplaint=tbl_complaint.objects.all()
    return render(request,'Administrator/Viewcomplaint.html',{'Viewcomplaint': viewcomplaint})


def viewfeedback(request):
    viewfeedback=tbl_feedback.objects.all()
    return render(request,'Administrator/ViewFeedback.html',{'viewfeedback': viewfeedback})


def scrapcenterlist(request):
    data=tbl_ScrapcenterReg.objects.all()
    return render(request,'Administrator/scrapcenterlist.html',{'scrapcenterlist': data})


def scraper_accept(request,sid):
    accdata=tbl_ScrapcenterReg.objects.get(id=sid)
    accdata.scraper_status=1
    accdata.save()
    return render(request,'Administrator/scrapcenterlist.html',{'msg':"Accepted"})

def rejectscraper(request,sid):
    scraper_reject=tbl_ScrapcenterReg.objects.get(id=sid)
    scraper_reject.scraper_status=2
    scraper_reject.save()
    return render(request,'Administrator/scrapcenterlist.html',{'msg':"Rejected"})


def brand(request):
    brand_data=tbl_Brand.objects.all()
    if request.method=='POST':
        brand = request.POST.get("txtname")
        tbl_Brand.objects.create(
            brand_name=brand
        )
        return redirect("Administrator:Brand")
    else:
        return render(request,'Administrator/Brand.html',{'Brand':brand_data})


def editbrand(request,id):
    editbrand=tbl_Brand.objects.get(id=id)
    if request.method=='POST':
        name=request.POST.get("txtname")
        editbrand.brand_name=name
        editbrand.save() 
        return redirect("Administrator:Brand")
    else:
        return render(request,'Administrator/Brand.html',{'data':editbrand})   


def deletebrand(request,id):
    tbl_Brand.objects.get(id=id).delete()
    return redirect("Administrator:Brand")


def model(request):
    brand_data=tbl_Brand.objects.all()
    model_data=tbl_model.objects.all()
    if request.method== 'POST':
        model = request.POST.get("txtname")
        brand_id = request.POST.get("sel_brand")
        brand_obj=tbl_Brand.objects.get(id=brand_id)
        tbl_model.objects.create(
            model_name=model,
            brand=brand_obj
        )
        return redirect("Administrator:Model")
    else:
        return render(request,'Administrator/Model.html',{'Model':model_data,'brand':brand_data})
    
def editmodel(request,id):
    brand_data=tbl_Brand.objects.all()
    editmodel=tbl_model.objects.get(id=id)
    if request.method=='POST':
        name=request.POST.get("txtname")
        editmodel.model_name=name
        brand_id = request.POST.get("sel_brand")
        brand_obj=tbl_model.objects.get(id= id)
        editmodel.tbl_Brand= brand_obj
        editmodel.save() 
        return redirect("Administrator:Model")
    else:
        return render(request,'Administrator/Model.html',{'data':editmodel,'brand':brand_data})


def deletemodel(request,id):
    tbl_model.objects.get(id=id).delete()
    return redirect("Administrator:Model")
