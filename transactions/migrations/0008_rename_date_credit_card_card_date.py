# Generated by Django 4.2.4 on 2023-10-12 05:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0007_alter_credit_card_month'),
    ]

    operations = [
        migrations.RenameField(
            model_name='credit_card',
            old_name='date',
            new_name='card_date',
        ),
    ]
