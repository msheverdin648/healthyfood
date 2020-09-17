# Generated by Django 3.1 on 2020-09-17 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0006_auto_20200917_2241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='final_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9, verbose_name='Общая цена заказа'),
        ),
        migrations.AlterField(
            model_name='food',
            name='discount',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=9, null=0, verbose_name='Цена со скидкой, если есть'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='food',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Цена блюда'),
        ),
        migrations.AlterField(
            model_name='questionsanswers',
            name='group',
            field=models.CharField(choices=[('weight', 'Вес'), ('tarifs', 'Тарифы'), ('products', 'Продукты')], default='products', max_length=20, verbose_name='Группа вопросов'),
        ),
    ]