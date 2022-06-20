from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.


def login(request):
    if request.method == "POST":
        email = request.POST.get('loginEmail')
        password = request.POST.get('loginPassword')
    return render(request, 'login.html')
