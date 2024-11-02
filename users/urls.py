from django.urls import path
from .views import user_login, user_signup, home_view

urlpatterns = [
    path('userlogin/', user_login, name='user_login'),
    path('usersignup/', user_signup, name='user_signup'),
    path('', home_view, name='home'),  # Add your home view here

]
