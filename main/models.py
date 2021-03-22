from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Line(models.Model):
    STATUS_CHOICES = [
        ('public', 'Published'),
        ('draft', 'Draft')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='line')
    name = models.CharField('Name', max_length=20)
    phone = models.CharField('Phone', max_length=11)
    line_date = models.CharField('Date', max_length=20)
    line_time = models.CharField('Time', max_length=10)
    date_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=6, default='public', choices=STATUS_CHOICES)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('line', kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('line-update', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('line-delete', kwargs={'pk': self.pk})

