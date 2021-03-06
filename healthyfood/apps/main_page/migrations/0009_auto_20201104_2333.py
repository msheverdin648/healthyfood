# Generated by Django 3.1 on 2020-11-04 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0008_auto_20201104_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='products',
            field=models.ManyToManyField(blank=True, to='main_page.Order', verbose_name='Заказанные меню'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True, verbose_name='Цена меню'),
        ),
        migrations.AlterField(
            model_name='questionsanswers',
            name='group',
            field=models.CharField(choices=[('weight', 'Вес'), ('products', 'Продукты'), ('tarifs', 'Тарифы')], default='products', max_length=20, verbose_name='Группа вопросов'),
        ),
    ]
