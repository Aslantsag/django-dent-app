from django.contrib.auth.models import User
from django.db import models

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
