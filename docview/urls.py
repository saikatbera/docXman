from django.urls import path
from . import views
# Create your tests here.
app_name = 'docview'
urlpatterns = [
    path('',views.index, name='index'),
    path('signup.html',views.signUpView, name='signup'),
    path('main.html',views.mainView, name='main'),
    
]
