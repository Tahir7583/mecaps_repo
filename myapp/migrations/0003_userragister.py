# Generated by Django 5.0.3 on 2024-08-21 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_applicant_skill_applicant_ids'),
    ]

    operations = [
        migrations.CreateModel(
            name='userRagister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
