# Generated by Django 5.1.1 on 2024-10-16 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upskill', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='course_picture',
            field=models.ImageField(blank=True, null=True, upload_to='course_picture', verbose_name='Превью курса'),
        ),
    ]
