# Generated by Django 3.2.4 on 2021-06-25 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0002_materials_grade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materials',
            name='grade',
            field=models.CharField(choices=[('D', 'D'), ('P', 'P'), ('M', 'M'), ('U', 'U')], default='U', max_length=50),
        ),
    ]
