from django.shortcuts import render,redirect
from .models import incidents
from .serializers import incidentSerializers
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth import logout


# Create your views here.
class Incidentviewset(viewsets.ModelViewSet):
    queryset=incidents.objects.all()
    serializer_class=incidentSerializers
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticated]
    filter_backends=[DjangoFilterBackend] 
    filterset_fields=['incident_id']
    def get_queryset(self):
        user=self.request.user
        return incidents.objects.filter(reporter_name=user)
    
    # def logout_view(request):
    #     logout(request)
    #     return redirect('api_token_auth')   
    
    def perform_create(self, serializer):
        serializer.save(reporter_name=self.request.user.username)
        
    
    