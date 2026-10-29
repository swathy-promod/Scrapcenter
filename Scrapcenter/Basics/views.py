from django.shortcuts import render,redirect
def calculator(request):
    return render(request,'Basics/calculator.html')    
def largest(request):
    if request.method =='POST':
        Number1=int(request.POST.get("txt_num1")) 
        Number2=int(request.POST.get("txt_num2"))
        if Number1>Number2:
            result= Number1
        else:
            result= Number2
            return render(request,'Basics/largest.html',{'result':result})
    else:
        return render(request,'Basics/largest.html')
      
def largestof3(request):
    if request.method =='POST':



        Number1=int(request.POST.get("txt_num1")) 
        Number2=int(request.POST.get("txt_num2"))
        Number3=int(request.POST.get("txt_num3"))
        if Number1>=Number2 and Number1>=Number3:
            result= Number1
        elif Number2>=Number1 and Number2>=Number3:
            result= Number2
        else: result=Number3
            
        

        return render(request,'Basics/largestof3.html',{'result':result})
    else:
        return render(request,'Basics/largestof3.html')
   
def Sum(request):
    if request.method=='POST':

        Number1=int(request.POST.get("txt_num1")) 
        Number2=int(request.POST.get("txt_num2"))
        result=Number1+Number2
        return render(request,'Basics/sum.html',{'result':result})
    else:
        return render(request,'Basics/sum.html')




# Create your views here.
