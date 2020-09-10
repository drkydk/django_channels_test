# Generated by Django 3.1.1 on 2020-09-07 14:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_name', models.CharField(default='', max_length=64)),
            ],
        ),
        migrations.AddField(
            model_name='message',
            name='seen',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='message',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='chat.channel'),
        ),
    ]
