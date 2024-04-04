from django.shortcuts import render,redirect
from images.models import Img
from django.contrib import auth,messages
from django.contrib.auth.models import User
from teachers.models import Teachers
from subjects.models import subjects
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
from news.models import News
from events.models import Events
from contact.models import Contact


def Home(req):
    img=Img.objects.all()
    context={
        'img':img
    }
    return render(req,'home.html',context)

def academics(req):
    subject=subjects.objects.all()
    context={
        'subjects':subject,
    }
    return render(req,'pages/academics.html',context)

def Subject(req,s_id):
    subject=subjects.objects.get(id=s_id)
    context={
        'subject':subject
    }
    return render(req,'pages/subject.html',context)

def About(req):
    teachers=Teachers.objects.all()
    context={
        'teachers':teachers
    }
    return render(req,'pages/about.html',context)

def news(req):
    news=News.objects.all()
    return render(req,'pages/news.html',{'news':news})

def Blog(req,id):
    blog=News.objects.get(id=id)
    return render(req,'pages/blog.html',{'blog':blog})

def events(req):
    event=Events.objects.all()
    return render(req,'pages/events.html',{'ev':event})

def student(req):
    return render(req,'pages/student.html')

def festival(req,id):
    Festival=Events.objects.get(id=id)    
    context={
        'festival':Festival,
    }
    return render(req,'pages/festival.html',context)

def parents(req):
    return render(req,'pages/parents.html')

def admission(req):
    return render(req,'pages/admission.html')

def contact(req):
    if req.method=='POST':
        firstname=req.POST['first_name']
        lastname=req.POST['lastname']
        email=req.POST['email']
        phone=req.POST['phone']
        textarea=req.POST['textarea']

        contact=Contact.objects.create(first_name=firstname,last_name=lastname,email=email,phone=phone,messages=textarea)
        contact.save()

        domain_name=get_current_site(req)
        mail_subject='Alert Please Contact us'
        message=f'http://{domain_name}/admin/'

        to_email='prawalkardam029@gmail.com'
        send_mail=EmailMessage(mail_subject,message,to=[to_email])
        send_mail.send()
    return render(req,'pages/contact.html')

def Login(req):
    if req.method=='POST':
        username=req.POST['username']
        password=req.POST['password']

        user=auth.authenticate(username=username,password=password)

        if user:
            auth.login(req,user)
            messages.add_message(req,messages.SUCCESS,'Login Successfully')
            return redirect('/')
        else:
            messages.add_message(req,messages.ERROR,'User Dose not Exists',extra_tags='danger')

    return render(req,'accounts/login.html')

def Logout(req):
    auth.logout(req)
    messages.success(req,'Logout Succefully')
    return redirect('/')

def Signup(req):
    if req.method=='POST':
        first_name=req.POST['firstname']
        email=req.POST['email']
        username=req.POST['username']
        password=req.POST['password']
        Confirm_password=req.POST['confirm_password']

        def xyz(first_name,password,Confirm_password,email,username):
            if User.objects.filter(email=email).exists():
             messages.add_message(req,messages.ERROR,'Email Already Exists',extra_tags='danger')
            elif password != Confirm_password:
                messages.add_message(req,messages.ERROR,'Password are not Match',extra_tags='danger')
            elif User.objects.filter(username=username).exists():
                messages.add_message(req,messages.ERROR,'Username Are Already Exists',extra_tags='danger')
            else:
                user=User.objects.create_user(first_name=first_name,email=email,username=username,password=password)
                user.save()
                domain_name=get_current_site(req)
                subject='Please Activate Your Account'
                user_id=urlsafe_base64_encode(force_bytes(user.pk))
                token=default_token_generator.make_token(user)
                message=f'http://{domain_name}/activate/account/{user_id}/{token}'
                to_email=email
                send_email=EmailMessage(subject,message,to=[to_email])
                send_email.send()
                messages.add_message(req,messages.SUCCESS,'Register Successfully')

        xyz(first_name,password,Confirm_password,email,username)
    return render(req,'accounts/signup.html')

def activate(req,u_id,token):
    try:
        id=urlsafe_base64_decode(u_id)
        user=User.objects.get(id=id)
        if default_token_generator.check_token(user,token):
            user.is_active=True
            user.save()
    except:
        messages.add_message(req,messages.SUCCESS,'Invalid Candidate')
    return redirect('/login')

from django.core.exceptions import ObjectDoesNotExist
def forgot(req):
    if req.method=='POST':
        email=req.POST['email']

        try:
            user=User.objects.get(email=email)
            domain_name=get_current_site(req)
            subject='Forgot Password'
            user_id=urlsafe_base64_encode(force_bytes(user.pk))
            token=default_token_generator.make_token(user)
            message=f'http://{domain_name}/forgot-password/{user_id}/{token}'
            to_email=email
            send_mail=EmailMessage(subject,message,to=[to_email])
            send_mail.send()

            messages.add_message(req,messages.SUCCESS,'Check Mail Box')
        except ObjectDoesNotExist:
            messages.add_message(req,messages.ERROR,'Email Are Not Exists',extra_tags='danger')
    return render(req,'accounts/forgot.html')

def ResetPassword(req,u_id,token):
    if req.method=='POST':
        password=req.POST['password']
        confirm_password=req.POST['confirm_password']

        if password != confirm_password:
            messages.add_message(req,messages.ERROR,'Password are Not Match',extra_tags='danger')
        else:
            id=urlsafe_base64_decode(u_id)
            user=User.objects.get(id=id)

            if default_token_generator.check_token(user,token):
                user.set_password(password)
                user.save()

                messages.add_message(req,messages.SUCCESS,'Password Reset Succefully')
                return redirect('/login')
            else:
                messages.add_message(req,messages.ERROR,'Invalid Candidate',extra_tags='danger')

    return render(req,'accounts/resetpassword.html')