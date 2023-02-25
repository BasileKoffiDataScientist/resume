from django.urls import path
# urls.py
from . import views


app_name = 'cvApp'


urlpatterns = [
    path('', views.index_view,name="index"),
    path('contact', views.contact_view,name="contact"),
    path('resume', views.resume_view,name="resume"),
    path('about', views.about_view,name="about"),
    path('download_cv/', views.download_cv, name='download_cv'),

]