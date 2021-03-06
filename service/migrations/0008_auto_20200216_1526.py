# Generated by Django 2.2.6 on 2020-02-16 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0007_auto_20200216_1500'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicefaq',
            name='service',
        ),
        migrations.AddField(
            model_name='servicefaq',
            name='service',
            field=models.ManyToManyField(blank=True, to='service.ServiceName', verbose_name='Вопрос-Ответ для основного вида работы'),
        ),
        migrations.RemoveField(
            model_name='servicefaq',
            name='subService',
        ),
        migrations.AddField(
            model_name='servicefaq',
            name='subService',
            field=models.ManyToManyField(blank=True, to='service.SubServiceName', verbose_name='Вопрос-Ответ для подвида работы'),
        ),
        migrations.RemoveField(
            model_name='servicefeature',
            name='service',
        ),
        migrations.AddField(
            model_name='servicefeature',
            name='service',
            field=models.ManyToManyField(blank=True, to='service.ServiceName', verbose_name='Приемущество для основного вида работы'),
        ),
        migrations.RemoveField(
            model_name='servicefeature',
            name='subService',
        ),
        migrations.AddField(
            model_name='servicefeature',
            name='subService',
            field=models.ManyToManyField(blank=True, to='service.SubServiceName', verbose_name='Приемущество для подвида работы'),
        ),
        migrations.AlterField(
            model_name='subservicename',
            name='name_lower',
            field=models.CharField(blank=True, db_index=True, editable=False, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='subservicename',
            name='name_slug',
            field=models.CharField(blank=True, db_index=True, editable=False, max_length=255, null=True, unique=True),
        ),
    ]
