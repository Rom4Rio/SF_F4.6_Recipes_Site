# Generated by Django 3.2.18 on 2023-09-22 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='category',
            field=models.CharField(choices=[('Супы', 'Супы'), ('Гарниры', 'Гарниры'), ('Главное блюдо', 'Главное блюдо'), ('Салаты', 'Салаты')], default='Супы', max_length=14),
        ),
    ]
