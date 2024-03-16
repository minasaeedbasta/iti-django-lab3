# Generated by Django 5.0.3 on 2024-03-16 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100, null=True, unique=True)),
                ('price', models.IntegerField(default=10, null=True)),
                ('no_of_pages', models.IntegerField(default=10, null=True)),
                ('image', models.ImageField(null=True, upload_to='books/images/')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]