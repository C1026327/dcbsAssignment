from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from itregistration.models import Module
from .serializers import ModuleSerializer

from rest_framework.permissions import IsAuthenticatedOrReadOnly
# Create your views here.

class ModuleViewSet(ModelViewSet):
    queryset = Module.objects.all().order_by('date_submitted')
    serializer_class = ModuleSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)