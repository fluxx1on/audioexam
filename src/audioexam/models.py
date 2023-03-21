from django.db import models
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import pre_save, post_save, post_init, m2m_changed

class Document(models.Model):
    name = models.CharField("Название", max_length=127)
    text = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Уведомление"
        verbose_name_plural = "Уведомления"

@receiver(post_save, sender=Document)
def postRequestFields(sender, instance, created, **kwargs):
    if created:
        instance.name = instance.text[0:127]
        instance.save()

class Audio(models.Model):
    audio_file = models.FileField("Аудио", upload_to='audio_files/')
    document = models.OneToOneField(Document, on_delete=models.CASCADE)

    def __str__(self):
        return self.document.name

    class Meta:
        verbose_name = "Уведомление"
        verbose_name_plural = "Уведомления"