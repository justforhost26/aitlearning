import random

from django.contrib import messages
from django.core.mail import EmailMessage
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.db.models import Q
#home page function
from django.template.loader import get_template

from faculty.models import Faculty_by_admin, Faculty, Video, Contact
from faculty.views import home


def index(request):
    obj = Video.objects.all().order_by('-id')
    paginator = Paginator(obj, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,"index.html",{"datas":page_obj})

# function for search
def search_main(request):
        obj=Video.objects.all().order_by('-id')
        paginator=Paginator(obj,6)
        page_number=request.GET.get('page')
        page_obj=paginator.get_page(page_number)
        if request.method=="POST":
            search=request.POST['search']
            search_data=Video.objects.filter(Q(topic_name__contains=search) | Q(subject_name__contains=search) | Q(faculty_name__contains=search))
            return render(request,"index.html",{"datas":page_obj,'search':search_data})


#contact page function
def contact(request):
    return render(request,"contact.html")
#funtcion for Contact in Main module
def contact_us(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        message=request.POST['message']
        obj=Contact(name=name,email=email,message=message)
        obj.save()
        messages.success(request,"message send successfully")
        return render(request,'contact.html')
    else:
        messages.error(request,"something went wrong ")
        return redirect(contact)

#faculty page function
def faculty(request):
    obj = Faculty.objects.all().order_by('id')
    paginator = Paginator(obj, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,"faculty.html",{'datas':page_obj})
#about page function
def about(request):
    return render(request,"about.html")
#faculty_login page function
def faculty_login(request):
    if 'email' in request.session:
        messages.success(request, "You are Already Login")
        return redirect(home)
    else:
        return render(request,"faculty_login.html")
#do_faculty_login page function
def do_faculty_login(request):
    if 'email' in request.session:
        messages.success(request, "You are Already Login")
        return redirect(home)
    else:
        if request.method=="POST":
            email=request.POST['email']
            password=request.POST['password']
            if Faculty.objects.filter(email=email,password=password).exists():
                request.session['email']=email
                messages.success(request,"Succesfully Login")
                obj = Video.objects.filter(faculty_email=email).order_by('-id')
                paginator = Paginator(obj, 6)
                page_number = request.GET.get('page')
                page_obj = paginator.get_page(page_number)
                return render(request, "faculty/faculty_home.html", {'email': email, "datas": page_obj})
            else:
                messages.success(request, "Invalid Details")
                return render(request, "faculty_login.html")
        else:
            messages.success(request, "Invalid Details")
            return render(request, "faculty_login.html.html")



#faculty_register page function
def faculty_register(request):
    if 'email' in request.session:
        messages.success(request, "You are Already Login")
        return redirect(home)
    else:
        return render(request,"faculty_register.html")
#do_faculty_register page function
def do_faculty_register(request):
    if 'email' in request.session:
        messages.success(request,"You are Already Login")
        return redirect(home)
    else:
        if request.method=="POST":
            name=request.POST['name']
            mobile_number=request.POST['mobile_number']
            email=request.POST['email']
            department=request.POST['department']
            branch=request.POST['branch']
            password=request.POST['password']
            if Faculty_by_admin.objects.filter(mobile_number=mobile_number,email=email,status="active").exists():
                if Faculty.objects.filter(mobile_number=mobile_number,email=email).exists():
                    messages.success(request,"You Are Already Register")
                    return render(request,"faculty_login.html")
                else:
                    obj=Faculty(name=name,email=email,mobile_number=mobile_number,department=department,branch=branch,password=password)
                    #mail code start
                    otp=random.randint(10000,99999)
                    ctx = {
                        'name': name,
                        'otp':otp,
                    }
                    message = get_template('email_tamplate.html').render(ctx)
                    msg = EmailMessage(
                        'AIT Learning Registration',
                        message,
                        'Alpine Insitude Of Techonology',
                        [email],

                    )
                    msg.content_subtype = "html"
                    msg.send()
                    request.session['email']=email
                    request.session['name'] = name
                    request.session['mobile_number'] = mobile_number
                    request.session['department'] = department
                    request.session['branch'] = branch
                    request.session['password'] =password
                    request.session['otp']=otp
                    content={
                        'email':email,
                        'name': name,
                        'mobile_number': mobile_number,
                        'department': department,
                        'password':password,
                        'branch': branch,
                        'otp': otp,
                    }

                    #mail code end
                    messages.success(request,"Otp Send to your Email, Enter OTP ")
                    return render(request,'otp.html',{"data":content})

            else:
                messages.success(request,"Your Are not a Faculty of AIT")
                return redirect(faculty_register)
        else:
            messages.error(request, "Something went Wrong ,please try again")
            return render(request, 'faculty_register.html')

#Function for verify otp
def verify_otp(request):
        if request.method=="POST":
            name=request.session['name']
            mobile_number=request.session['mobile_number']
            email=request.session['email']
            department=request.session['department']
            branch=request.session['branch']
            password=request.session['password']
            sotp=request.session['otp']
            eotp=request.POST['otp']
            if str(sotp)==str(eotp):
                obj = Faculty(name=name, email=email, mobile_number=mobile_number, department=department, branch=branch,password=password)
                obj.save()
                request.session.flush()
                messages.success(request,'Registered Successful')
                return render(request,'faculty_login.html')
            else:
                messages.success(request,"Invalid OTP")
                content={
                    'email':email
                }
                return render(request,'otp.html',{"data":content})



