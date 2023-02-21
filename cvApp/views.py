from django.shortcuts import render

# Create your views here.


def index_view(request):
    return render(request, 'cvApp/index.html')


def contact_view(request):
    return render(request, 'cvApp/contact.html')


def resume_view(request):
    return render(request, 'cvApp/resume.html')


def about_view(request):
    return render(request, 'cvApp/about.html')