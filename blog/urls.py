from django.urls import path
# urls.py
from . import views


app_name = 'blog'


urlpatterns = [
    path('blog/', views.blog_view,name="blog"),
    path('blog-details/', views.blog_details_view,name="blog-details"),

]