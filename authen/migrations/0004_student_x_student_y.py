# Generated by Django 4.0.4 on 2022-05-02 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authen', '0003_remove_student_semester'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='x',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='student',
            name='y',
            field=models.IntegerField(default=1),
        ),
    ]
