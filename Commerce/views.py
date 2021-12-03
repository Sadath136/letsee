from django.shortcuts import render
from django.http import HttpResponse
def homepage(request):
    return render(request,'Commerce/homepage.html')
def su(request):
    if request.method=="POST":
        name = request.POST.get('username')
        phonenumber = request.POST.get('phonenumber')
        file=request.FILES.get('file_upload')
        return HttpResponse("<h1><em>You have already registered your phone number</em></h1>")
