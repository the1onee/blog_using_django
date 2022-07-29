# Generated by Django 4.0.4 on 2022-07-15 14:49

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='catagry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=255)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='portfol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='title')),
                ('img', models.ImageField(upload_to='', verbose_name='img')),
                ('link', models.CharField(max_length=300, verbose_name='link')),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='title')),
                ('icon', models.CharField(max_length=300, verbose_name='icon')),
                ('body', models.TextField(verbose_name='body')),
            ],
        ),
        migrations.CreateModel(
            name='skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skil', models.CharField(max_length=50, verbose_name='nae:')),
                ('exp', models.IntegerField(verbose_name='how exp')),
            ],
        ),
        migrations.CreateModel(
            name='viewblogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='title:')),
                ('slug', models.SlugField(max_length=200, unique=True, verbose_name='slug')),
                ('img', models.ImageField(blank=True, null=True, upload_to='profile', verbose_name='img')),
                ('body', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='body')),
                ('updated_on', models.DateTimeField(auto_now=True, verbose_name='updated_on')),
                ('active', models.BooleanField(default=False)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='created ')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts', to=settings.AUTH_USER_MODEL)),
                ('catag', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='catagry', to='homes.catagry')),
            ],
        ),
        migrations.CreateModel(
            name='Mohmed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='nae:')),
                ('img', models.ImageField(blank=True, null=True, upload_to='profile', verbose_name='img')),
                ('slug', models.SlugField(blank=True, null=True, verbose_name='slug')),
                ('skis_name', models.TextField(blank=True, null=True, verbose_name='skills')),
                ('aboutme', models.TextField(blank=True, null=True, verbose_name='about me ')),
                ('phone', models.CharField(blank=True, max_length=12, null=True, verbose_name='phone')),
                ('address', models.CharField(blank=True, max_length=50, null=True, verbose_name='your address')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('dgree', models.CharField(blank=True, max_length=50, null=True, verbose_name='Dgree')),
                ('experns', models.IntegerField(blank=True, null=True, verbose_name='experns')),
                ('brith', models.DateField(blank=True, null=True, verbose_name='brithday')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'Mohmed',
                'verbose_name_plural': 'Mohmeds',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('body', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=False)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='homes.viewblogs')),
            ],
        ),
    ]