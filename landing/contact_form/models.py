from django.db import models


class ContactForm(models.Model):
    """
    Contact form.
    """

    name = models.CharField('Имя', max_length=100)
    phone_number = models.CharField('Номер телефона', max_length=30)
    message = models.TextField('Сообщение', null=True, blank=True)

    created = models.DateTimeField('Дата создания', auto_now_add=True)

    def __str__(self) -> str:
        """
        Get instance string representation.
        """
        return f'Заявка №{self.id} от {self.created.strftime("%d.%m.%Y %H:%M")}'

    def save(self, *args, **kwargs):

        super().save()
        self.inform_admins()

    def inform_admins(self):
        """
        Inform admins about new instance creation.
        """
        pass
