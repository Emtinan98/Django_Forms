# Generated by Django 4.0.4 on 2022-05-26 06:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='project name', max_length=100)),
                ('creation_time', models.DateField(auto_now_add=True, help_text='Date of the Project .')),
                ('completion_time', models.DateField(help_text='Completion time.', null=True)),
                ('image_field', models.ImageField(upload_to='images/')),
                ('project_logo', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Task name', max_length=100)),
                ('description', models.TextField(help_text='Task Help.')),
                ('time_estimate', models.IntegerField(help_text='Task time.')),
                ('completed', models.BooleanField(default=False)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PMApp.project')),
            ],
        ),
    ]