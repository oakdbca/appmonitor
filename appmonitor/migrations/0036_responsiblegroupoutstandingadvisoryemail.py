# Generated by Django 3.2.23 on 2024-01-09 04:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appmonitor', '0035_responsiblegroupadvisoryemail'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResponsibleGroupOutstandingAdvisoryEmail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('responsible_group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='appmonitor.responsiblegroup')),
            ],
        ),
    ]
