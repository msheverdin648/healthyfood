# Generated by Django 3.1 on 2020-12-01 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0010_auto_20201105_0003'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='created_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата создания заказа'),
        ),
        migrations.AlterField(
            model_name='questionsanswers',
            name='group',
            field=models.CharField(choices=[('products', 'Продукты'), ('tarifs', 'Тарифы'), ('weight', 'Вес')], default='products', max_length=20, verbose_name='Группа вопросов'),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='after_img',
            field=models.ImageField(blank=True, null=True, upload_to='img', verbose_name='Фото "после"'),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='age',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Возраст'),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='before_img',
            field=models.ImageField(blank=True, null=True, upload_to='img', verbose_name='Фото "до"'),
        ),
    ]
