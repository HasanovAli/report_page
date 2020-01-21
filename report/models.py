from django.conf import settings
from django.db import models
from django.urls import reverse


class Entry(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField(db_index=True)
    distance = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.DurationField()

    def __str__(self):
        return 'Entry for user {}'.format(self.user.username)

    def get_absolute_url(self):
        return reverse('report:entry_create', args=[])
