from django.urls import path
from .views import home, home_detail, blog, blog_detail

urlpatterns = [
    path('', home, name='home'),
    path('home_detail/<int:id>', home_detail, name='home_detail'),
    path('blog/', blog, name='blog'),
    path('blog_detail/<int:id>', blog_detail, name='blog_detail'),

]