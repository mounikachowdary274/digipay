# Generated by Django 4.2.4 on 2023-09-20 06:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import shortuuid.django_fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bankaccounts', '0004_alter_kyc_identity_image_alter_kyc_image_and_more'),
        ('transactions', '0003_alter_transaction_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='receiver_amount',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='sender_amount',
        ),
        migrations.AddField(
            model_name='transaction',
            name='receiver_account',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='receiver_account', to='bankaccounts.account'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='sender',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sender', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='transaction',
            name='sender_account',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sender_account', to='bankaccounts.account'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=12),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='description',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='receiver',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='status',
            field=models.CharField(choices=[['failed', 'FAILED'], ['completed', 'COMPLETED'], ['pending', 'PENDING'], ['processing', 'PROCESSING'], ['request_sent', 'REQUEST_SENT'], ['request_processing', 'REQUEST_PROCESSING']], default='pending', max_length=200),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='transaction_id',
            field=shortuuid.django_fields.ShortUUIDField(alphabet=None, length=15, max_length=25, prefix='TRN', unique=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='transaction_type',
            field=models.CharField(choices=[['transfer', 'TRANSFER'], ['withdraw', 'WITHDRAW'], ['refund', 'REFUND'], ['received', 'RECEIVED'], ['request', 'REQUEST'], ['none', 'NONE']], default='none', max_length=200),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='updated_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]
