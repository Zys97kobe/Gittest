# Generated by Django 3.2.13 on 2022-04-30 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_auto_20220430_1126'),
    ]

    operations = [
        migrations.AddField(
            model_name='peopleinfo',
            name='description',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='peopleinfo',
            name='is_delete',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='peopleinfo',
            name='gender',
            field=models.SmallIntegerField(choices=[(2, 'feamle'), (1, 'male')], default=1),
        ),
        migrations.AlterField(
            model_name='peopleinfo',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
