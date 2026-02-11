from django.shortcuts import render,redirect

from .models import FormStudent
from django.contrib import messages

from django.core.mail import send_mail,EmailMessage
from django.template.loader import render_to_string
from datetime import datetime

# Create your views here.
def home(request):
    searched= request.GET.get("trysearch")
    if searched:
        data=FormStudent.objects.filter(name__icontains=searched)
    else:
        data= FormStudent.objects.filter(is_delete=False)
    return render(request,'crud_app/home.html',{'data':data})



def form(request):
    if request.method=='POST' and request.FILES:
        name= request.POST.get('name')
        age= request.POST.get('age')
        email = request.POST.get('email')
        address = request.POST.get('address')
        message= request.POST.get('message')
        image= request.FILES.get('image')
        video= request.FILES.get('video')

        try:
            user= FormStudent(name= name, age= age, email= email,address=address,message=message,image= image,video= video)
            user.full_clean()
            user.save()

            subject = "Form Confirmation : Django Form"
            message= render_to_string('crud_app/mail_msg.html',{'name':name,'date':datetime.now()})
            from_email='anish0li751106@gmail.com'
            recipient_list=[email,'anisholi751106@gmail.com']

            # send_mail(subject=subject, message=message,from_email=from_email,recipient_list=recipient_list,fail_silently=False)
            mail_msg= EmailMessage(subject=subject,from_email=from_email,to=recipient_list,body=message)
            mail_msg.attach_file('crud_app/static/pdf/English.pdf')
            mail_msg.send(fail_silently=False)

            messages.success(request, 'Form submitted successfully !!! Check your mail')
            return redirect('form')
        except Exception as e:
            messages.error(request, e)
            return redirect('form')
        
    return render(request,'crud_app/form.html')


def services(request):
    return render(request,'crud_app/service.html')
def blog(request):
    return render(request,'crud_app/blog.html')


def delete_data(request,id):
    data= FormStudent.objects.get(id=id)
    data.is_delete= True
    data.save()
    return redirect('home')


def update_data(request,id):
    data= FormStudent.objects.get(id= id)

    if request.method == "POST":
        data= FormStudent.objects.get(id=id)
        data.name= request.POST.get('name')
        data.age= request.POST.get('age')
        data.email= request.POST.get('email')
        data.address= request.POST.get('address')
        data.message= request.POST.get('message')
        data.save()
        return redirect('home')

    
    return render(request, 'crud_app/edit.html',{'data':data})



def recycle(request):
    data= FormStudent.objects.filter(is_delete= True)
    return render(request,'crud_app/recycle.html',{'data':data})


def restore_data(request,id):
    data= FormStudent.objects.get(id=id)
    data.is_delete=False
    data.save()
    return redirect('home')


def counter(request):
    total = 0  # define default

    if request.method == "POST":
        message = request.POST.get('message', '').strip()
        if message:
            total = len(message.split())

    return render(request, 'crud_app/counter.html', {'total': total})