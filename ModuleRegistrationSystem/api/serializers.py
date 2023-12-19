from rest_framework.serializers import ModelSerializer, ReadOnlyField
from itregistration.models import Module,Course,Registration

class Meta:
    model = Module
    fields = ['moduleid', 'modulename', 'category', 'credit', 'description', 'available', 'author', 'date_submitted',]

author = ReadOnlyField(source='author.username')