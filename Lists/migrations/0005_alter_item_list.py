# Generated by Django 4.1.7 on 2023-03-22 16:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Lists', '0004_remove_item_user_alter_item_list'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='list',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='Lists.list'),
            preserve_default=False,
        ),
    ]
