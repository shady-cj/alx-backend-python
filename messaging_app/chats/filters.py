from django_filters import rest_framework as filters
from .models import Message

class MessageFilter(filters.Filterset):
    sent_before = filters.DateTimeFilter(field_name="sent_at", lookup_expr='lte')
    sent_after = filters.DateTimeFilter(field_name="sent_at", lookup_expr='gte')
    class Meta:
        model = Message
        fields = []