from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def applyPage(request):
    return render(request,'ApplyPage/applyPage.html')

def signup(request):
    return render(request,'signup/signup.html')
def signin(request):
    return render(request,'signin/signin.html')