# Generated by Django 3.2.4 on 2021-07-27 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allifmaalerpsystem', '0010_auto_20210727_0014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allifmaalstocktable1',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
