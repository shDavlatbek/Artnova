# Generated by Django 5.0 on 2025-02-08 09:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0009_remove_socialmediaperson_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200, verbose_name='F.I.SH')),
                ('image', models.ImageField(upload_to='uploads/team/%Y/%m/%d/', verbose_name='Rasm')),
                ('position', models.CharField(max_length=200, verbose_name='Lavozimi')),
                ('description', models.TextField(verbose_name='Kichik izoh')),
                ('contact_url', models.CharField(blank=True, default='#contact', max_length=200, null=True, verbose_name="Bog'lanish URL")),
            ],
            options={
                'verbose_name': 'Jamoa',
                'verbose_name_plural': 'Jamoa',
            },
        ),
        migrations.RenameModel(
            old_name='SocialMediaPerson',
            new_name='ContactPersonSocialMedia',
        ),
        migrations.RenameModel(
            old_name='SocialMediaSite',
            new_name='SiteSocialMedia',
        ),
        migrations.CreateModel(
            name='TeamSocialMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='social_media', to='web.team')),
            ],
        ),
    ]
