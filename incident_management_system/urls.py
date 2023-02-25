
from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from api import views

from rest_framework.authtoken.views import obtain_auth_token



from django.contrib.auth.views import  LogoutView





router=DefaultRouter()
router.register('incidentapi',views.Incidentviewset,basename='incidents')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('logout/', views.logout, name='api_logout'),
] 
