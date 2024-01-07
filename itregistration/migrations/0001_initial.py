# Generated by Django 4.2 on 2023-12-18 22:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Module',
            fields=[
                ('moduleid', models.AutoField(primary_key=True, serialize=False)),
                ('modulename', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('Cybersecurity', 'Cybersecurity'), ('Data Science', 'Data Science'), ('Software Development', 'Software Development'), ('Web Designing', 'Web Designing'), ('VFX and Animation', 'VFX and Animation'), ('Games Design', 'Games Design')], max_length=100)),
                ('credit', models.SmallIntegerField()),
                ('description', models.CharField(max_length=10000)),
                ('available', models.BooleanField()),
                ('date_submitted', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Module', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_registration', models.DateTimeField(default=django.utils.timezone.now)),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='itregistration.module')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coursename', models.CharField(default='Course Name', max_length=100)),
                ('description', models.CharField(max_length=10000)),
                ('modules', models.ManyToManyField(to='itregistration.module')),
            ],
        ),
    ]