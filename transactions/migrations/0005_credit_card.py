# Generated by Django 4.2.4 on 2023-10-12 05:28

from django.db import migrations, models
import django.db.models.deletion
import shortuuid.django_fields


class Migration(migrations.Migration):

    dependencies = [
        ('bankaccounts', '0004_alter_kyc_identity_image_alter_kyc_image_and_more'),
        ('transactions', '0004_remove_transaction_receiver_amount_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Credit_Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('card_id', shortuuid.django_fields.ShortUUIDField(alphabet='0123456789', length=12, max_length=16, prefix='', unique=True)),
                ('month', models.IntegerField()),
                ('year', models.IntegerField()),
                ('cvv', shortuuid.django_fields.ShortUUIDField(alphabet='0123456789', length=3, max_length=3, prefix='', unique=True)),
                ('card_type', models.CharField(choices=[['master', 'MASTER'], ['visa', 'VISA'], ['rupay', 'RUPAY'], ['platinum', 'PLATINUM']], default='none', max_length=200)),
                ('card_status', models.CharField(choices=[['active', 'ACTIVE'], ['in-active', 'IN-ACTIVE']], default='pending', max_length=200)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='bankaccounts.account')),
            ],
        ),
    ]