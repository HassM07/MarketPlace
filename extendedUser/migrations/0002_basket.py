# Generated by Django 4.2.2 on 2023-06-23 13:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('extendedUser', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items', models.ManyToManyField(to='extendedUser.item')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='extendedUser.extendeduser')),
            ],
        ),
    ]
