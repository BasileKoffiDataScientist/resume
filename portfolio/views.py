from django.shortcuts import render

# Create your views here.


def portfolio_view(request):
    return render(request, 'portfolio/portfolio.html')


def portfolio_archives_view(request):
    return render(request, 'portfolio/portfolio-archives.html')


def portfolio_details_view(request):
    return render(request, 'portfolio/portfolio-details.html')




