# Generated by Django 2.1 on 2018-08-29 18:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chatbothandler', '0010_auto_20180829_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='inputs',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='users', to='chatbothandler.Inputs'),
        ),
    ]
