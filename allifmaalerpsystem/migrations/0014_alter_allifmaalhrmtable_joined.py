# Generated by Django 3.2.4 on 2021-07-28 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allifmaalerpsystem', '0013_auto_20210727_2131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allifmaalhrmtable',
            name='joined',
            field=models.DateTimeField(blank=True, max_length=255, null=True),
        ),
    ]
