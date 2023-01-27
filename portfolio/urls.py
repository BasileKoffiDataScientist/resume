from django.urls import path
# urls.py
from . import views


app_name = 'portfolio'


urlpatterns = [
    path('portfolio/', views.portfolio_view,name="portfolio"),
    path('portfolio-archives/', views.portfolio_archives_view,name="portfolio-archives"),
    path('portfolio-details/', views.portfolio_details_view,name="portfolio-details"),

]




