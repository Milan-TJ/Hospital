# Generated by Django 5.0.3 on 2024-06-03 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TrustCareMedicalGroup', '0004_alter_doctor_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], default='Not defined', max_length=10),
        ),
    ]