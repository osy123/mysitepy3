# Generated by Django 2.0.6 on 2018-10-23 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_no', models.CharField(max_length=50)),
                ('order_no', models.CharField(max_length=50)),
                ('reg_date', models.DateField(auto_now=True)),
                ('title', models.CharField(max_length=5)),
                ('content', models.TextField(max_length=200)),
                ('hit', models.IntegerField(null=True)),
                ('depth', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]
