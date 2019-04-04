from rest_framework import serializers

from leads.models import Lead


class LeadSerializer(serializers.ModelSerializer):
    """Serializer for Lead objects"""

    class Meta:
        model = Lead
        fields = '__all__'
        read_only_fields = ('id',)
