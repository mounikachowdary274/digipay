# Generated by Django 4.2.4 on 2023-08-21 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_payment_rename_name_user_profile_address_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_profile',
            name='password',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user_profile',
            name='username',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
