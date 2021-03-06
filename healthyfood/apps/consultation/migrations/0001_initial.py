# Generated by Django 3.1 on 2020-09-27 17:33

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
            name='UserMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_text', models.TextField(verbose_name='Текст сообщения')),
                ('sending_date', models.DateTimeField(auto_now=True, verbose_name='Дата отправки данного сообщения')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор сообщения')),
            ],
            options={
                'verbose_name': 'Сообщение от пользователя',
                'verbose_name_plural': 'Сообщения от пользователей',
            },
        ),
    ]
