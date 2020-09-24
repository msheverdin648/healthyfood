# Generated by Django 3.1 on 2020-09-24 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0026_reviews_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionsanswers',
            name='group',
            field=models.CharField(choices=[('products', 'Продукты'), ('tarifs', 'Тарифы'), ('weight', 'Вес')], default='products', max_length=20, verbose_name='Группа вопросов'),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='text',
            field=models.TextField(verbose_name='Текст отзыва'),
        ),
    ]
