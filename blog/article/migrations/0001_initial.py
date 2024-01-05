# Generated by Django 5.0.1 on 2024-01-05 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('author', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_title', models.CharField(max_length=255)),
                ('article_content', models.TextField()),
                ('article_date', models.DateTimeField()),
                ('article_author', models.ManyToManyField(to='author.author')),
            ],
        ),
    ]
