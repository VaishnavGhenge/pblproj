# Generated by Django 4.0.3 on 2022-05-02 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserFiles',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user', models.CharField(max_length=200)),
                ('js', models.TextField(blank=True)),
                ('html', models.TextField(blank=True)),
                ('css', models.TextField(blank=True)),
            ],
        ),
    ]
