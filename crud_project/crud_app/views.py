from django.shortcuts import render,redirect

from .models import FormStudent
from django.contrib import messages

# Create your views here.
def home(request):
    searched= request.GET.get("trysearch")
    if searched:
        data=FormStudent.objects.filter(name__icontains=searched)
    else:
        data= FormStudent.objects.all()
    return render(request,'crud_app/home.html',{'data':data})



def form(request):
    if request.method=='POST':
        name= request.POST.get('name')
        age= request.POST.get('age')
        email = request.POST.get('email')
        address = request.POST.get('address')
        message= request.POST.get('message')

        try:
            user= FormStudent(name= name, age= age, email= email,address=address,message=message)
            user.full_clean()
            user.save()
            messages.success(request, 'Form submitted successfully !!!')
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
    data.delete()
    return redirect('home')
