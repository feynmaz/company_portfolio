# Generated by Django 3.2.5 on 2021-07-04 21:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_usercompanyrelationship_role'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Role',
        ),
        migrations.AlterModelOptions(
            name='usercompanyrelationship',
            options={'verbose_name': 'Связь', 'verbose_name_plural': 'Связи'},
        ),
    ]