# Generated by Django 3.2.9 on 2021-12-09 13:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('manga', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50)),
                ('date', models.DateField(auto_now_add=True)),
                ('image', models.ImageField(upload_to='')),
                ('manga', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chapter', to='manga.manga')),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='chapter', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]