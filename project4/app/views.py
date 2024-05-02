from django.shortcuts import render
from django.http import HttpResponse
from app.models import*
# Create your views here.

def register(request):
    if request.method == 'POST':
        name = request.POST.get('nm')
        pno = request.POST.get('pno')
        eml = request.POST.get('eml')
        un = request.POST.get('un')
        pw = request.POST.get('pw')
        cpw = request.POST.get('cpw')
        if pw == cpw:
            CO = Details(nm = name, pno = pno, email = eml, un = un, pw = pw)
            CO.save()
            return render(request, 'login.html')
        return HttpResponse('Password does not match')
    return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        un = request.POST.get('un')
        pw = request.POST.get('pw')
        UO = Details.objects.all()
        for user in UO:
            if user.un == un:
                if user.pw == pw:
                    return HttpResponse('Logged in Successfull')
                return HttpResponse('Invalid Password')
        else:
            return HttpResponse('User Not Found')
    return render(request, 'login.html')