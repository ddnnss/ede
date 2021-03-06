# Generated by Django 2.2.6 on 2019-11-14 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_big', models.ImageField(upload_to='comments', verbose_name='Картинка отзыва большая 590 х 435 px')),
                ('image_small', models.ImageField(upload_to='comments', verbose_name='Картинка отзыва маленькая 265 х 145px')),
                ('writtenBy', models.CharField(default='', max_length=75, verbose_name='От кого отзыв')),
                ('title', models.CharField(max_length=50, verbose_name='Заголовок отзыва (50 символов)')),
                ('description', models.CharField(max_length=75, verbose_name='Короткое описание отзыва (75 символов)')),
                ('shortReview', models.CharField(max_length=180, verbose_name='Первая часть отзыва (180 символов)')),
                ('fullReview', models.TextField(verbose_name='Вторая часть отзыва, показывается при нажатии на ЧИТАТЬ ДАЛЕЕ')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
    ]
