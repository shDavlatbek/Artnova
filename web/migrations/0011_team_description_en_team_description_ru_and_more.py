# Generated by Django 5.0 on 2025-02-08 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0010_team_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='description_en',
            field=models.TextField(null=True, verbose_name='Kichik izoh'),
        ),
        migrations.AddField(
            model_name='team',
            name='description_ru',
            field=models.TextField(null=True, verbose_name='Kichik izoh'),
        ),
        migrations.AddField(
            model_name='team',
            name='description_uz',
            field=models.TextField(null=True, verbose_name='Kichik izoh'),
        ),
        migrations.AddField(
            model_name='team',
            name='full_name_en',
            field=models.CharField(max_length=200, null=True, verbose_name='F.I.SH'),
        ),
        migrations.AddField(
            model_name='team',
            name='full_name_ru',
            field=models.CharField(max_length=200, null=True, verbose_name='F.I.SH'),
        ),
        migrations.AddField(
            model_name='team',
            name='full_name_uz',
            field=models.CharField(max_length=200, null=True, verbose_name='F.I.SH'),
        ),
        migrations.AddField(
            model_name='team',
            name='position_en',
            field=models.CharField(max_length=200, null=True, verbose_name='Lavozimi'),
        ),
        migrations.AddField(
            model_name='team',
            name='position_ru',
            field=models.CharField(max_length=200, null=True, verbose_name='Lavozimi'),
        ),
        migrations.AddField(
            model_name='team',
            name='position_uz',
            field=models.CharField(max_length=200, null=True, verbose_name='Lavozimi'),
        ),
    ]
