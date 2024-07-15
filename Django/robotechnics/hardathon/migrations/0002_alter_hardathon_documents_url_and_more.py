# Generated by Django 4.2.6 on 2024-07-15 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partners', '0005_alter_partner_link'),
        ('hardathon', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hardathon',
            name='documents_url',
            field=models.URLField(blank=True, verbose_name='ссылка на документы'),
        ),
        migrations.AlterField(
            model_name='hardathon',
            name='partners',
            field=models.ManyToManyField(blank=True, to='partners.partner', verbose_name='партнёры хардатона'),
        ),
        migrations.AlterField(
            model_name='hardathon',
            name='photo_album_url',
            field=models.URLField(blank=True, verbose_name='ссылка на фото-альбом'),
        ),
        migrations.AlterField(
            model_name='hardathon',
            name='social_media_mention',
            field=models.URLField(blank=True, verbose_name='упоминание в сми'),
        ),
        migrations.AlterField(
            model_name='hardathon',
            name='summing_up_date',
            field=models.DateField(blank=True, verbose_name='дата подведения итогов'),
        ),
    ]
