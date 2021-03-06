# Generated by Django 3.2.6 on 2021-08-23 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('detail', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name': 'Frequently_ask',
                'verbose_name_plural': 'Frequently_asks',
                'db_table': 'Frequently_ask',
            },
        ),
        migrations.CreateModel(
            name='ContactModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=50)),
                ('full_name', models.CharField(max_length=150)),
                ('subject', models.CharField(max_length=100)),
                ('message', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'contact',
                'verbose_name_plural': 'contact',
                'db_table': 'contact',
            },
        ),
        migrations.CreateModel(
            name='Pricing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan_name', models.CharField(max_length=35)),
                ('price', models.IntegerField()),
                ('detail1', models.CharField(max_length=50)),
                ('detail2', models.CharField(max_length=50)),
                ('detail3', models.CharField(max_length=50)),
                ('detail4', models.CharField(max_length=50)),
                ('detail5', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Pricing',
                'verbose_name_plural': 'Prices',
                'db_table': 'Pricing',
            },
        ),
        migrations.CreateModel(
            name='TeamMembers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='team-images')),
                ('full_name', models.CharField(max_length=40)),
                ('jobs', models.CharField(max_length=25)),
                ('information', models.CharField(max_length=60)),
                ('socialmedia_twitter', models.CharField(max_length=35)),
                ('socialmedia_facebook', models.CharField(max_length=35)),
                ('socialmedia_instagram', models.CharField(max_length=35)),
                ('socialmedia_linkedin', models.CharField(max_length=35)),
            ],
            options={
                'verbose_name': 'Team Member',
                'verbose_name_plural': 'Team Members',
                'db_table': 'Team Member',
            },
        ),
    ]
