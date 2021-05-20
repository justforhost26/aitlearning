from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect

# Create your views here.
#function for Faculty Dashboard
from faculty.models import Faculty, Video, Contact


def home(request):
    if 'email' in request.session:
        email=request.session['email']
        obj=Video.objects.filter(faculty_email=email).order_by('-id')
        paginator=Paginator(obj,6)
        page_number=request.GET.get('page')
        page_obj=paginator.get_page(page_number)
        return render(request,"faculty/faculty_home.html",{'email':email,"datas":page_obj})
    else:
        messages.error(request,"Session is Out, please Login Again")
        return render(request,'faculty_login.html')

# function for search
def search(request):
    if 'email' in request.session:
        email=request.session['email']
        obj=Video.objects.filter(faculty_email=email).order_by('-id')
        paginator=Paginator(obj,6)
        page_number=request.GET.get('page')
        page_obj=paginator.get_page(page_number)
        if request.method=="POST":
            search=request.POST['search']
            search_data=Video.objects.filter(Q(topic_name__contains=search) | Q(subject_name=search))
            print(search_data)
            if search_data=="":
                msg="No Data Found"
                return render(request, "faculty/faculty_home.html",{'email': email, "datas": page_obj, 'msg': msg })
        return render(request,"faculty/faculty_home.html",{'email':email,"datas":page_obj,'search':search_data})
    else:
        messages.error(request,"Session is Out, please Login Again")
        return render(request,'faculty_login.html')

# function for Add Video By Faculty
def add_video(request):
    if 'email' in request.session:
        email=request.session['email']
        obj=Faculty.objects.get(email=email)
        return render(request,"faculty/add_video.html",{'email':email,"data":obj})
    else:
        messages.error(request,"Session is Out, please Login Again")
        return render(request,'faculty_login.html')
# function for DO Add Video By Faculty
def do_add_video(request):
    if 'email' in request.session:
        email=request.session['email']
        obj = Faculty.objects.get(email=email)
        if request.method=="POST":
            topic_name=request.POST['topic_name']
            subject_name=request.POST['subject_name']
            faculty_name=request.POST['faculty_name']
            faculty_email=request.POST['faculty_email']
            notes=request.FILES['notes']
            video=request.FILES['video']
            print(notes,video)
            vid=Video(topic_name=topic_name,subject_name=subject_name,faculty_name=faculty_name,faculty_email=faculty_email,notes=notes,video=video)
            vid.save()
            messages.success(request,"video added Successful")
            return render(request,'faculty/add_video.html',{'email':email,"data":obj})
        else:
            messages.error(request, "video Not added ")
            return render(request, 'faculty/add_video.html', {'email': email,"data":obj})
    else:
        messages.error(request,"Session is Out, please Login Again")
        return render(request,'faculty_login.html')

#function for delete video
def delete_video(request,id):
    if 'email' in request.session:
        dlt_obj=Video.objects.get(id=id)
        dlt_obj.delete()
        messages.success(request,"Video Deleted Succesful")
        return redirect(home)
    else:
        messages.error(request,"session is out , please login")

#function for Edit video
def edit_video(request,id):
    if 'email' in request.session:
        edt_obj=Video.objects.get(id=id)
        return render(request,'faculty/edit_video.html',{"data":edt_obj})
    else:
        messages.error(request,"session is out , please login")
        return render(request,'faculty_login.html')

#function for Edit video
def do_edit_video(request,id):
    if 'email' in request.session:
        edt_obj=Video.objects.get(id=id)
        edt_obj.topic_name=request.POST['topic_name']
        edt_obj.subject_name=request.POST['subject_name']
        edt_obj.notes=request.FILES['notes']
        edt_obj.save()
        messages.success(request,"Video Update Successful")
        return redirect(home)
    else:
        messages.error(request,"session is out , please login")
        return render(request,'faculty_login.html')


#function for Faculty Profile
def profile(request):
    if 'email' in request.session:
        email=request.session['email']
        obj=Faculty.objects.get(email=email)
        return render(request,"faculty/profile.html",{'data':obj})
    else:
        messages.error(request,"Session is Out, please Login Again")
        return render(request,'faculty_login.html')
#function for Edit Profile
def edit(request,id):
    if 'email' in request.session:
        obj=Faculty.objects.get(id=id)
        return render(request,"faculty/update_profile.html",{'data':obj})
    else:
        messages.error(request,"Session is Out, please Login Again")
        return render(request,'faculty_login.html')

#function for Update Profile
def update_profile(request,id):
    if 'email' in request.session:
        if request.method=="POST":
            obj=Faculty.objects.get(id=id)
            obj.name=request.POST['name']
            obj.mobile_number = request.POST['mobile_number']
            obj.email = request.POST['email']
            obj.department = request.POST['department']
            obj.branch = request.POST['branch']
            obj.save()
            if obj.email==request.session['email']:
                return redirect(profile)
            else:
                request.session.flush()
                messages.warning(request,"You Change your email so please Login again")
                return render(request, 'faculty_login.html')
        else:
            obj = Faculty.objects.get(id=id)
            messages.error(request,"Something went wrong")
            return render(request, 'faculty/update_profile.html',{"data":obj})


    else:
        messages.error(request,"Session is Out, please Login Again")
        return render(request,'faculty_login.html')
#function for Update Profile_pic
def update_profile_pic(request,id):
    if 'email' in request.session:
        obj = Faculty.objects.get(id=id)
        return render(request, "faculty/update_profile_pic.html", {'data': obj})
    else:
        messages.error(request,"Session is Out, please Login Again")
        return render(request,'faculty_login.html')


#function for do Update Profile_pic
def do_update_profile_pic(request,id):
    if 'email' in request.session:
        if request.method=="POST":
            obj=Faculty.objects.get(id=id)
            obj.pic = request.FILES['pic']
            obj.save()
            return redirect(profile)
        else:
            obj = Faculty.objects.get(id=id)
            messages.error(request,"Something went wrong")
            return render(request,"faculty/update_profile_pic.html",{"data":obj})
    else:
        messages.error(request,"Session is Out, please Login Again")
        return render(request,'faculty_login.html')

#function for Update password
def update_password(request,id):
    if 'email' in request.session:
        obj = Faculty.objects.get(id=id)
        return render(request, "faculty/update_password.html", {'data': obj})
    else:
        messages.error(request,"Session is Out, please Login Again")
        return render(request,'faculty_login.html')


#function for do Update password
def do_update_password(request,id):
    if 'email' in request.session:
        if request.method=="POST":
            obj = Faculty.objects.get(id=id)
            old_password=request.POST['old_password']
            new_password=request.POST['new_password']
            confirm_new_password = request.POST['confirm_new_password']
            if Faculty.objects.filter(id=id,password=old_password).exists():
                if old_password==new_password:
                    messages.error(request,"your new password is same as old password ,try something else")
                    return render(request,"faculty/update_password.html",{"data":obj})
                else:
                    if new_password==confirm_new_password:
                        obj.password = request.POST['new_password']
                        obj.save()
                        messages.success(request,"password Change successfull")
                        return redirect(profile)
                    else:
                        messages.error(request, "new password & confirm password does not Match")
                        return render(request, "faculty/update_password.html",{"data":obj})
            else:
                messages.error(request, "Wrong Password")
                return render(request, "faculty/update_password.html",{"data":obj})
        else:
            obj = Faculty.objects.get(id=id)
            messages.error(request,"Something went wrong")
            return render(request,"faculty/update_password.html",{"data":obj})
    else:
        messages.error(request,"Session is Out, please Login Again")
        return render(request,'faculty_login.html')

#function for Faculty Logout
def logout(request):
    if 'email' in request.session:
        request.session.flush()
        messages.success(request,"Logout successfull")
        return render(request,'faculty_login.html')
    else:
        messages.error(request,"Session is Out, please Login Again")
        return render(request,'faculty_login.html')

#funtcion for Contact in faculty module
def contact_faculty(request):
    if 'email' in request.session:
        email=request.session['email']
        obj=Faculty.objects.get(email=email)
        return render(request, 'faculty/faculty_contact.html',{'data':obj})
    else:
        messages.error(request, "Session is Out, please Login Again")
        return render(request, 'faculty_login.html')

#funtcion for Contact in faculty module
def contact_us(request):
    if 'email' in request.session:
        if request.method=="POST":
            name=request.POST['name']
            email=request.POST['email']
            message=request.POST['message']
            obj=Contact(name=name,email=email,message=message)
            obj.save()
            messages.success(request,"message send successfully")
            return redirect(home)
        else:
            messages.error(request,"something went wrong ")
            return redirect(contact_faculty)
    else:
        messages.error(request, "Session is Out, please Login Again")
        return render(request, 'faculty_login.html')
