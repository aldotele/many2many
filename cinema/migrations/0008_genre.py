# Generated by Django 3.2.7 on 2021-10-21 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0007_plot'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(max_length=30)),
                ('movies', models.ManyToManyField(to='cinema.Movie')),
            ],
        ),
    ]
