# Generated by Django 4.2.4 on 2024-01-20 04:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ctracker', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_consumed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ctracker.food')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
