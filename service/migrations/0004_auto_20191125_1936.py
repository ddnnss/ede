# Generated by Django 2.2.6 on 2019-11-25 16:36

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0003_auto_20191118_1937'),
    ]

    operations = [
        migrations.CreateModel(
            name='SeoTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('indexTitle', models.CharField(blank=True, max_length=255, null=True, verbose_name='Тег Title для главной')),
                ('indexDescription', models.CharField(blank=True, max_length=255, null=True, verbose_name='Тег Description для главной')),
                ('indexKeywords', models.TextField(blank=True, null=True, verbose_name='Тег Keywords для главной')),
                ('servicesTitle', models.CharField(blank=True, max_length=255, null=True, verbose_name='Тег Title для страницы со всеми услугами')),
                ('servicesDescription', models.CharField(blank=True, max_length=255, null=True, verbose_name='Тег Description для страницы со всеми услугам')),
                ('servicesKeywords', models.TextField(blank=True, null=True, verbose_name='Тег Keywords для страницы со всеми услугам')),
                ('postsTitle', models.CharField(blank=True, max_length=255, null=True, verbose_name='Тег Title для страницы со всеми статьями')),
                ('postsDescription', models.CharField(blank=True, max_length=255, null=True, verbose_name='Тег Description для страницы со всеми статьями')),
                ('postsKeywords', models.TextField(blank=True, null=True, verbose_name='Тег Keywords для страницы со всеми статьями')),
                ('contactTitle', models.CharField(blank=True, max_length=255, null=True, verbose_name='Тег Title для страницы контакты')),
                ('contactDescription', models.CharField(blank=True, max_length=255, null=True, verbose_name='Тег Description для страницы контакты')),
                ('contactKeywords', models.TextField(blank=True, null=True, verbose_name='Тег Keywords для страницы контакты')),
                ('homeDefaultText', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Текст для главной страницы, если не указан иной')),
            ],
            options={
                'verbose_name': 'Теги для статических страниц',
                'verbose_name_plural': 'Теги для статических страниц',
            },
        ),
        migrations.AddField(
            model_name='servicename',
            name='defaultText',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Текст для вставки на страницу услуги, если не указан иной'),
        ),
    ]
