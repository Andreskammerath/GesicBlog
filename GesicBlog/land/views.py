from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail

# Create your views here.
def index(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        subject = request.POST["subject"]
        subject = subject + f" recibido desde: {email} - autor: {name}"
        msg = request.POST["message"]
        send_mail(
            subject,
            msg,
            'kammerath.andres@gmail.com',
            ['lilianaelsa@hotmail.com',"andreskammerath@gmail.com"],
            fail_silently=False)
        return render(request, 'land/Message.html', {})


    return render(request, 'land/index.html', {})
    #return HttpResponse("Bienvenido a Gesic")