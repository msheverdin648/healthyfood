# Generated by Django 3.1 on 2020-09-21 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0017_auto_20200920_0431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionsanswers',
            name='group',
            field=models.CharField(choices=[('tarifs', 'Тарифы'), ('weight', 'Вес'), ('products', 'Продукты')], default='products', max_length=20, verbose_name='Группа вопросов'),
        ),
    ]
