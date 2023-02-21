from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.urls import reverse
from django.views import generic
from django.contrib.auth.decorators import login_required


# Create your views here.


def blog_view(request):
    return render(request, 'blog/blog.html')


def blog_details_view(request):
    return render(request, 'blog/blog-details.html')