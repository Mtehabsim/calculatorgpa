# Generated by Django 3.2.4 on 2021-06-26 13:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0005_alter_materials_grade'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='materials',
            name='grade',
        ),
        migrations.RemoveField(
            model_name='materials',
            name='installed',
        ),
    ]