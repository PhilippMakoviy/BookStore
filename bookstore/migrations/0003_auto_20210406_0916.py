# Generated by Django 3.1.7 on 2021-04-06 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0002_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('status', models.CharField(max_length=5)),
                ('period', models.CharField(max_length=5)),
            ],
        ),
        migrations.DeleteModel(
            name='userProfile',
        ),
    ]
