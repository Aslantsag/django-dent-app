# Generated by Django 3.1.6 on 2021-02-22 19:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Line',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Name')),
                ('phone', models.CharField(max_length=11, verbose_name='Phone')),
                ('line_date', models.CharField(max_length=20, verbose_name='Date')),
                ('line_time', models.CharField(max_length=10, verbose_name='Time')),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('public', 'Published'), ('draft', 'Draft')], default='public', max_length=6)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='line', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
