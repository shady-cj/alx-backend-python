from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Message, Notification, User

@receiver(post_save, sender=Message)
def create_notification(sender, instance, created, **kwargs):
    if created:
        # Create a notification for the receiver of the message
        Notification.objects.create(message=instance, user=instance.receiver)
        