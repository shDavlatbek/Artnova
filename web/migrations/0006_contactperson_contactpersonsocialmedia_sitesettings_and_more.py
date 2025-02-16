# Generated by Django 5.0 on 2025-02-03 22:30

import django.db.models.deletion
import tinymce.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_medicine_description_sm_en_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactPerson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nomi')),
                ('name_uz', models.CharField(max_length=200, null=True, verbose_name='Nomi')),
                ('name_ru', models.CharField(max_length=200, null=True, verbose_name='Nomi')),
                ('name_en', models.CharField(max_length=200, null=True, verbose_name='Nomi')),
                ('phone', models.CharField(blank=True, max_length=200, null=True, verbose_name='Telefon raqam')),
                ('email', models.CharField(blank=True, max_length=200, null=True, verbose_name='Elektron pochta')),
            ],
            options={
                'verbose_name': 'Kontakt person',
                'verbose_name_plural': 'Kontakt personlar',
            },
        ),
        migrations.CreateModel(
            name='ContactPersonSocialMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.contactperson')),
            ],
        ),
        migrations.CreateModel(
            name='SiteSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=200, verbose_name='Telefon raqam')),
                ('email', models.CharField(max_length=200, verbose_name='Elektron pochta')),
                ('address', models.CharField(max_length=200, verbose_name='Manzil')),
                ('address_uz', models.CharField(max_length=200, null=True, verbose_name='Manzil')),
                ('address_ru', models.CharField(max_length=200, null=True, verbose_name='Manzil')),
                ('address_en', models.CharField(max_length=200, null=True, verbose_name='Manzil')),
            ],
            options={
                'verbose_name': 'Sayt sozlamalari',
                'verbose_name_plural': 'Sayt sozlamalari',
            },
        ),
        migrations.CreateModel(
            name='SiteSettingsSocialMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_settings', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.sitesettings')),
            ],
        ),
        migrations.CreateModel(
            name='SocialMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nomi')),
                ('icon', models.CharField(help_text='Ikonka nomini https://fontawesome.com/v6/search?ic=free dan oling, misol uchun: fab fa-telegram', max_length=200, verbose_name='Ikonka')),
                ('link', models.URLField(verbose_name='Havola')),
            ],
            options={
                'verbose_name': 'Ijtimoiy tarmoqlar',
                'verbose_name_plural': 'Ijtimoiy tarmoqlar',
            },
        ),
        migrations.DeleteModel(
            name='Medicine',
        ),
        migrations.AlterField(
            model_name='news',
            name='content',
            field=tinymce.models.HTMLField(verbose_name='Matn'),
        ),
        migrations.AlterField(
            model_name='news',
            name='content_en',
            field=tinymce.models.HTMLField(null=True, verbose_name='Matn'),
        ),
        migrations.AlterField(
            model_name='news',
            name='content_ru',
            field=tinymce.models.HTMLField(null=True, verbose_name='Matn'),
        ),
        migrations.AlterField(
            model_name='news',
            name='content_uz',
            field=tinymce.models.HTMLField(null=True, verbose_name='Matn'),
        ),
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(upload_to='assets/images/news_images/', verbose_name='Rasm'),
        ),
        migrations.AlterField(
            model_name='news',
            name='slug',
            field=models.SlugField(default='', unique=True, verbose_name='Qisqa link'),
        ),
        migrations.AlterField(
            model_name='news',
            name='views',
            field=models.IntegerField(default=0, editable=False, verbose_name="Ko'rishlar soni"),
        ),
        migrations.AddField(
            model_name='sitesettingssocialmedia',
            name='social_media',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.socialmedia'),
        ),
        migrations.AddField(
            model_name='sitesettings',
            name='social_medias',
            field=models.ManyToManyField(related_name='site_settings', through='web.SiteSettingsSocialMedia', to='web.socialmedia'),
        ),
        migrations.AddField(
            model_name='contactpersonsocialmedia',
            name='social_media',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.socialmedia'),
        ),
        migrations.AddField(
            model_name='contactperson',
            name='social_medias',
            field=models.ManyToManyField(related_name='contact_persons', through='web.ContactPersonSocialMedia', to='web.socialmedia'),
        ),
    ]
