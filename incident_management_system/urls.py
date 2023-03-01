
from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from api import views

# from rest_framework.authtoken.views import obtain_auth_token



# from django.contrib.auth.views import  LogoutView





router=DefaultRouter()
router.register('incidentapi',views.Incidentviewset,basename='incidents')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('auth/',include('rest_framework.urls',namespace='rest_framework')),
   
] 
