from django.db import models
from  django.contrib.auth.models import User 
# Create your models here.


class Chat(models.Model):
    """Model definition for Chat."""

    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='user_chat')
    message = models.TextField()
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for Chat."""

        verbose_name = 'Chat'
        verbose_name_plural = 'Chats'

    def __str__(self):
        """Unicode representation of Chat."""
        return '{}'.format(self.user.username) # TODO
