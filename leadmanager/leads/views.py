from rest_framework import viewsets, permissions

from leads.serializers import LeadSerializer
from leads.models import Lead


class LeadViewSet(viewsets.ModelViewSet):
    """Manage CRUD operations for Leads in the database"""
    queryset = Lead.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = LeadSerializer
