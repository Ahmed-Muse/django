# Generated by Django 3.2.4 on 2021-07-29 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allifmaalerpsystem', '0019_alter_allifmaalhrmtable_joined'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllifmaalHRMTable2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff_number', models.CharField(blank=True, max_length=255, null=True)),
                ('first_name', models.CharField(blank=True, max_length=255, null=True)),
                ('middle_name', models.CharField(blank=True, max_length=255, null=True)),
                ('last_name', models.CharField(blank=True, max_length=255, null=True)),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=255, null=True)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('department', models.CharField(blank=True, max_length=255, null=True)),
                ('joined', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='AllifmaalHRMTable',
        ),
    ]
