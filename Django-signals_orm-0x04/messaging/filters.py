from django_filters import rest_framework as filters
from .models import Message

class MessageFilter(filters.FilterSet):
    sent_before = filters.DateTimeFilter(field_name="timestamp", lookup_expr='lte')
    sent_after = filters.DateTimeFilter(field_name="timestamp", lookup_expr='gte')
    class Meta:
        model = Message
        fields = []