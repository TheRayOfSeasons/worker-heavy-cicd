# Generated by Django 3.1.6 on 2021-02-12 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('display_name', models.CharField(max_length=150, unique=True)),
                ('email', models.EmailField(error_messages={'unique': 'A user with this email already exists.'}, max_length=254, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('is_cms_admin', models.BooleanField(default=False, help_text='Designates whether user can edit site content through the custom CMS.')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]