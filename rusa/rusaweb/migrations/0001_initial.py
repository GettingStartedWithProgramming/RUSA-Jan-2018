# Generated by Django 2.0.1 on 2018-02-04 12:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('is_student', models.BooleanField(default=False)),
                ('college_name', models.CharField(blank=True, default='', max_length=350)),
                ('age_group', models.CharField(choices=[('AA', '10-14'), ('AB', '15-18'), ('BB', '19-23'), ('BC', 'Above 23')], default='AB', max_length=2)),
                ('joined_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('description', models.CharField(blank=True, default='', max_length=1000)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('no_of_registrations', models.PositiveIntegerField(blank=True, default=0)),
                ('no_of_tasks', models.PositiveIntegerField(blank=True, default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400)),
                ('description', models.CharField(max_length=1500)),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('no_of_submissions', models.PositiveIntegerField(blank=True, default=0)),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='rusaweb.Program')),
            ],
        ),
        migrations.CreateModel(
            name='TaskCompletion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('completion_date', models.DateTimeField(auto_now_add=True)),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='rusaweb.Participant')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rusaweb.Task')),
            ],
        ),
        migrations.AddField(
            model_name='participant',
            name='program',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='rusaweb.Program'),
        ),
        migrations.AddField(
            model_name='participant',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
