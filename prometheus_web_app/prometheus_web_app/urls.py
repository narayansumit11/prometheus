from django.contrib import admin
from django.urls import path
from myapp import views
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('signin/',views.signin, name='signin'),
    path('signout/',views.signout, name='signout'),
    path('signup/',views.signup, name='signup'),
]