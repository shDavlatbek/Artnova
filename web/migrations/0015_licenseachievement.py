# Generated by Django 5.0 on 2025-02-09 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0014_sitesettings_about_us_sitesettings_about_us_en_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='LicenseAchievement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='uploads/license_achievement/%Y/%m/%d/', verbose_name='Rasm')),
                ('title', models.CharField(max_length=200, verbose_name='Sarlavha')),
                ('title_uz', models.CharField(max_length=200, null=True, verbose_name='Sarlavha')),
                ('title_ru', models.CharField(max_length=200, null=True, verbose_name='Sarlavha')),
                ('title_en', models.CharField(max_length=200, null=True, verbose_name='Sarlavha')),
                ('achievement_type', models.CharField(choices=[('license', 'Litsensiya'), ('achievement', 'Yutuq')], max_length=200, verbose_name='Turi')),
            ],
        ),
    ]
