# Generated by Django 4.2.6 on 2024-07-15 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partners', '0004_alter_partner_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partner',
            name='link',
            field=models.URLField(blank=True, verbose_name='ссылка на сайт'),
        ),
    ]