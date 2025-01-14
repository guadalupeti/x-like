# Generated by Django 5.1.1 on 2024-11-26 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('x', '0003_post_creation_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profile_pic',
            field=models.ImageField(blank=True, default='profile_pics/egg.jpg', null=True, upload_to='profile_pics/'),
        ),
        migrations.CreateModel(
            name='Hashtag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=240, unique=True)),
                ('posts', models.ManyToManyField(related_name='hashtags', to='x.post')),
            ],
        ),
    ]
