from django.urls import path
from . import views
    
"""
The current home page is 127.0.0.1:8000 which is represented as '', and where 
we want to send the user to i.e views.homepage (views is the file and homepage is the function)
Whatever name we give to the path (in this case name='count') should be the same that we pass to the form action (<form action="{% url 'count' %}">)
"""

urlpatterns = [
    path('', views.homepage, name='home'),
    path('count/', views.count, name = 'count'),
    path('about/', views.about, name='about')
]