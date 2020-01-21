from django.shortcuts import render
from .models import Form

def index(request):
    return render(request, 'index.html')

def form(request):
    Name = request.POST['Name']
    Email = request.POST['Email']
    Phone = request.POST['Phone']
    Message = request.POST['Message']

    form = Form(Name=Name, Email=Email, Phone=Phone, Message=Message)
    form.save()

    return render(request, 'form.html')
