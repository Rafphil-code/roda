from django.db.models.signals import post_save
from django.conf import settings
from django.dispatch import receiver
from .models import OtpToken
from django.core.mail import send_mail
from django.utils import timezone

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def createtoken(sender, instance, created, **kwargs):
    print("signals called")
    if created:
        if instance.is_superuser:
            pass
        else:
            OtpToken.objects.create(user=instance, otp_expires_at=timezone.now() + timezone.timedelta(minutes=5))
            instance.is_active = False
            instance.save()

            otp = OtpToken.objects.filter(user=instance).last()
            subject = "Vérification d'Email"
            message = f"""
                        Bonjour {instance.username}, Voici votre code de vérification : {otp.otp_code}
                        Ce code a une validité de 5min, Utilisez le lien suivant pour la vérification
                        http://127.0.0.1:8000/verify_email/{instance.username}

                        """
            sender = settings.EMAIL_HOST_USER
            receiver = [instance.email]
            send_mail(
                subject,
                message,
                sender,
                receiver,
                fail_silently=True
            )