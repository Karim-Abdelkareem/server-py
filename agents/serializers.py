from rest_framework import serializers
from .models import Agent
from shipments.models import Shipment

class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = ['id', 'user', 'city', 'total_earnings']

class ShipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipment
        fields = ['id', 'origin', 'destination', 'status', 'cost', 'assigned_agent', 'created_at']
