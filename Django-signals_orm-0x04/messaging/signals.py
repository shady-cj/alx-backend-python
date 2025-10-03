from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save
from .models import Message, Notification, User, MessageHistory
from django.utils import timezone

@receiver(post_save, sender=Message)
def create_notification(sender, instance, created, **kwargs):
    if created:
        # Create a notification for the receiver of the message
        Notification.objects.create(message=instance, user=instance.receiver)


@receiver(pre_save, sender=Message)
def log_edited_message(sender, instance, **kwargs):
    if instance.id is None:
        pass

    else:
        previous_message = Message.objects.get(id=instance.id)
        if previous_message.content != instance.content:
            # Log the previous content to MessageHistory
            MessageHistory.objects.create(
                message=previous_message,
                old_content=previous_message.content
            )
            instance.edited = True
            instance.edited_at = timezone.now()

        