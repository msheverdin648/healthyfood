# Generated by Django 3.1 on 2020-09-20 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0016_auto_20200920_0430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buy',
            name='status',
            field=models.CharField(choices=[('new', 'Новый заказ'), ('in_progress', 'Заказ в обработке'), ('ready', 'Заказ готов'), ('completed', 'Заказ выполнен')], default='new', max_length=100, verbose_name='Статус заказа'),
        ),
        migrations.AlterField(
            model_name='questionsanswers',
            name='group',
            field=models.CharField(choices=[('weight', 'Вес'), ('products', 'Продукты'), ('tarifs', 'Тарифы')], default='products', max_length=20, verbose_name='Группа вопросов'),
        ),
    ]