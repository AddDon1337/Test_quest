# Generated by Django 3.2.5 on 2021-07-20 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_file', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='csvmodel',
            name='csv_fields',
            field=models.FilePathField(match='deals. * /. csv $', path='/test_page_root/data'),
        ),
    ]
