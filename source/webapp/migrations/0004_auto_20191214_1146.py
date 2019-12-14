# Generated by Django 2.2 on 2019-12-14 11:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webapp', '0003_auto_20191214_0834'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='likes',
        ),
        migrations.AddField(
            model_name='photo',
            name='likes',
            field=models.IntegerField(default=0, verbose_name='Лайки'),
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='like', to='webapp.Photo', verbose_name='Фотография')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='like', to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
        ),
    ]