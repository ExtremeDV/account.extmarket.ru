from django.db.models.signals import post_save
from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from .models import User
from django.dispatch import receiver
from .models import Profile

from .KafkaProducer import send_message

# Сигнал при создании пользователя
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        send_message(f"user.{instance.id}", {"user": instance.username, "iser_id": instance.id, "action": "create"})

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

# Сигнал при входе пользователя
@receiver(user_logged_in)
def user_logged_in(sender, user, request, **kwargs):
    send_message(f"user.{user.id}", {"user": user.username, "user_id": user.id, "action": "login"})

# Сигнал при входе пользователя
@receiver(user_logged_out)
def user_logged_out(sender, user, request, **kwargs):
    send_message(f"user.{user.id}", {"user": user.username, "user_id": user.id, "action": "logout"})

# Сигнал при неудачной попытке входа
@receiver(user_login_failed)
def log_failed_login(sender, credentials, request, **kwargs):
    # Логика обработки неудачной попытки авторизации
    username = credentials.get('username', 'Unknown')
    send_message(f'user.failed.{username}', {"user": username, "action": "login_failed"})