import secrets

from django.db import models


def _get_token():
    return secrets.token_urlsafe(32)


class Client(models.Model):

    client_id = models.CharField(
        verbose_name="ID клиента",
        max_length=128,
        unique=True,
        help_text="Уникальный идентификатор клиента",
    )
    client_secret = models.CharField(
        verbose_name="Secret клиента",
        max_length=128,
        default=_get_token,
        editable=False,
        help_text="Секретный ключ клиента",
    )
    comment = models.CharField(
        verbose_name="Комментарий",
        max_length=256,
        blank=True,
        null=True,
        help_text="Имя клиента или пояснение",
    )
    is_active = models.BooleanField(
        verbose_name="Активен",
        default=True,
        help_text="Указывает, может ли клиент посылать письма",
    )

    created_at = models.DateTimeField("Момент создания", auto_now_add=True)
    updated_at = models.DateTimeField("Момент изменения", auto_now=True)

    def __str__(self):
        return self.comment if self.comment else self.client_id
    
    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"
