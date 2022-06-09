# Generated by Django 3.2.13 on 2022-06-08 23:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0002_alter_menuitem_restaurant'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReservaItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('qty', models.CharField(max_length=45)),
                ('description', models.CharField(max_length=250)),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menus.restaurant')),
            ],
        ),
    ]
