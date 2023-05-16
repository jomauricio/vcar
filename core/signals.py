from django.contrib.auth import authenticate, get_user_model
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Profile

# from telesign.appverify import AppVerifyClient
# from telesign.messaging import MessagingClient


User = get_user_model()


@receiver(post_save, sender=User)  # add this
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        send_mail(subject="Cadastro realizado no VCAR",
                  message="Olá {}!\nVocê acabou de se cadastrar no site da VCAR com o email {}.\nSeja bem vindo!".format(
                      instance.username, instance.email),
                  from_email="noreplay@vcar.site",
                  recipient_list=[instance.email],
                  fail_silently=False,)

        authenticate(username=instance.username,
                     password=instance.password)

        # external_id = "external_id"

        # appverify = AppVerifyClient(
        #     '57ABDDA1-841F-4A69-990B-07AD33926CA5', 'xJe3RWgiGnPmJrm+Zzcu/IzZMzsw86IoHMEsEIDpuWVPfoaPE3o7HYDxLRsQZkEHuo4geuI8r9OAhsKAUL5r8g==')
        # response = appverify.status(external_id)
        # messaging = MessagingClient(
        #     settings.TELESIGN_COSTUMER_ID, settings.TELESIGN_KEY)
        # messaging.message(
        #     '86981103337', 'Cadastro realizado com sucesso. Email da conta: {}'.format(instance.email), 'ARN')

        # if response.ok:
        #     print("App Verify transaction with external_id {} has status code {} and status description {}.".format(
        #         external_id,
        #         response.json['status']['code'],
        #         response.json['status']['description']))
        # else:
        #     print("Erro de verificação!!!!!!!!!")


# @receiver(post_save, sender=User)  # add this
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()
        # messaging = MessagingClient(
        #     settings.TELESIGN_COSTUMER_ID, settings.TELESIGN_KEY)
        # response = messaging.message(phone_number, message, message_type)
