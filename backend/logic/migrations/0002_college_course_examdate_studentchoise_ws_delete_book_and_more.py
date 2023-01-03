# Generated by Django 4.1.1 on 2022-10-30 12:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('logic', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('college', models.CharField(blank=True, max_length=256, null=True)),
            ],
            options={
                'ordering': ['college'],
            },
        ),
        migrations.CreateModel(
            name='course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=256, null=True)),
                ('professor', models.CharField(blank=True, max_length=256, null=True)),
                ('group', models.IntegerField(blank=True, null=True)),
                ('unit', models.IntegerField(blank=True, null=True)),
                ('code', models.IntegerField(blank=True, null=True)),
                ('capacity', models.IntegerField(blank=True, null=True)),
                ('requirement', models.CharField(blank=True, default='ندارد', max_length=256)),
                ('synthesis', models.CharField(blank=True, default='ندارد', max_length=256)),
                ('ps', models.CharField(blank=True, default='ندارد', max_length=256)),
                ('college', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='logic.college')),
            ],
        ),
        migrations.CreateModel(
            name='ExamDate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('start', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='studentChoise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseId', models.IntegerField(blank=True, null=True)),
                ('title', models.CharField(blank=True, max_length=256, null=True)),
                ('professor', models.CharField(blank=True, max_length=256, null=True)),
                ('group', models.IntegerField(blank=True, null=True)),
                ('unit', models.IntegerField(blank=True, null=True)),
                ('code', models.IntegerField(blank=True, null=True)),
                ('ps', models.CharField(blank=True, default='ندارد', max_length=256, null=True)),
                ('examDate', models.DateField(blank=True, null=True)),
                ('examStart', models.FloatField(blank=True, null=True)),
                ('student', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ws',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day1', models.IntegerField(blank=True, null=True)),
                ('day2', models.IntegerField(blank=True, null=True)),
                ('start', models.FloatField(blank=True, null=True)),
                ('time', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='book',
        ),
        migrations.AddField(
            model_name='course',
            name='examDate',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='backExam', to='logic.examdate'),
        ),
        migrations.AddField(
            model_name='course',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='course',
            name='ws',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='backWeek', to='logic.ws'),
        ),
    ]
