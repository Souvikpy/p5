from django.urls import path
from myapp import views
app_name="myapp"

urlpatterns = [
   
    path('profile/',views.profile,name="profile"),
     path('sample1/',views.sample1,name='sample1'),
     path('sample2/',views.sample2,name='sample2'),
]
