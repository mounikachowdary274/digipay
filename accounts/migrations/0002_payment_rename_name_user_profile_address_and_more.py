# Generated by Django 4.2.4 on 2023-08-17 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
            ],
        ),
        migrations.RenameField(
            model_name='user_profile',
            old_name='Name',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='user_profile',
            old_name='Phone',
            new_name='age',
        ),
        migrations.AddField(
            model_name='user_profile',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AddField(
            model_name='user_profile',
            name='name',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user_profile',
            name='phone',
            field=models.BigIntegerField(default=1),
            preserve_default=False,
        ),
    ]
