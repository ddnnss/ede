# Generated by Django 2.2.6 on 2019-10-22 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderfile',
            name='file',
            field=models.FileField(null=True, upload_to='order_files', verbose_name='Файл'),
        ),
    ]