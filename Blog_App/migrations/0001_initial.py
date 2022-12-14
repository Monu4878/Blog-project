# Generated by Django 4.0.6 on 2022-07-21 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blogging',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_heading', models.CharField(max_length=100)),
                ('blog_images', models.ImageField(upload_to='Blog_images')),
                ('blog_desc', models.CharField(max_length=1000)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('pub_name', models.CharField(max_length=100)),
            ],
        ),
    ]
