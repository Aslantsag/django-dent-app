from django.contrib.auth.models import User
from django.db import models


class UserPrice(models.Model):
    STATUS_CHOICES = [
        ('public', 'Published'),
        ('draft', 'Draft')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='userprice')
    title = models.CharField('Title', max_length=255)
    price = models.FloatField('Price')
    status = models.CharField(max_length=6, default='public', choices=STATUS_CHOICES)

    def __str__(self):
        return self.title


class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='userinfo')
    user_image = models.ImageField('Image', max_length=255, upload_to='user_image', blank=True)
    about_text = models.TextField('About text', null=True, blank=True)
    phone = models.CharField('Phone', max_length=15, blank=True)
    insta = models.CharField('Instagram', max_length=255, blank=True)
    whats = models.CharField('Whats App', max_length=255, blank=True)
    geo = models.TextField('Map url from Yandex.Maps', null=True, blank=True)
    address = models.CharField('Address', max_length=255, blank=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'User info'
        verbose_name_plural = 'User info'


class UserMedia(models.Model):
    STATUS_CHOICES = [
        ('public', 'Published'),
        ('draft', 'Draft')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usermedia')
    file = models.ImageField('file', max_length=255, upload_to='user_image')
    title = models.TextField('Title', null=True)
    status = models.CharField(max_length=6, default='public', choices=STATUS_CHOICES)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'File'
        verbose_name_plural = 'User media'
