# Generated by Django 4.2.3 on 2023-07-23 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voter', '0005_voterlist_voter_image_alter_voterlist_dept'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voterlist',
            name='dept',
            field=models.CharField(blank=True, choices=[('Information Technology', 'information technology')], max_length=50, null=True),
        ),
    ]
