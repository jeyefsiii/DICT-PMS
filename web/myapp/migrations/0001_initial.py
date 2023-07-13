# Generated by Django 4.2.3 on 2023-07-13 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CPMS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('program', models.CharField(max_length=255)),
                ('info', models.JSONField(default=[{'Accomplishment': None, 'Activity': '', 'Indicator': '', 'Remarks': '', 'Target': None}])),
            ],
        ),
        migrations.CreateModel(
            name='Examinees',
            fields=[
                ('no', models.AutoField(primary_key=True, serialize=False)),
                ('province', models.CharField(max_length=255)),
                ('component', models.CharField(choices=[('Hands-on Exam', 'Hands-on Exam'), ('Diagnostic Exam', 'Diagnostic Exam'), ('User Assessment', 'User Assessment')], max_length=15)),
                ('name', models.CharField(max_length=255)),
                ('venue', models.CharField(blank=True, max_length=255)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('date', models.DateField(null=True)),
                ('time', models.CharField(choices=[('AM', 'am'), ('PM', 'pm')], max_length=2)),
                ('status', models.CharField(choices=[('Passed', 'Passed'), ('Failed', 'Failed'), ('For checking', 'For checking'), ('For transmittal', 'For transmittal')], max_length=20)),
                ('remarks', models.CharField(blank=True, max_length=255)),
                ('batch', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='OJTInput',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('province', models.CharField(choices=[('Cavite', 'Cavite'), ('Laguna', 'Laguna'), ('Batangas', 'Batangas'), ('Rizal', 'Rizal'), ('Quezon', 'Quezon'), ('RO', 'RO')], max_length=30)),
                ('category', models.CharField(choices=[('accepted at DICT Office', 'accepted at DICT Office'), ('endorsed by partners', 'endorsed by partners')], max_length=255)),
                ('suc', models.CharField(blank=True, max_length=255)),
                ('duration', models.IntegerField(blank=True)),
                ('school_address', models.CharField(blank=True, max_length=400)),
                ('representative', models.CharField(blank=True, max_length=255)),
                ('representative_contact', models.CharField(blank=True, max_length=15)),
                ('student_name', models.CharField(max_length=255)),
                ('sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('student_contact', models.CharField(blank=True, max_length=15)),
                ('start_date', models.DateField(null=True)),
                ('end_date', models.DateField(null=True)),
                ('mode', models.CharField(choices=[('Physical Reporting', 'Physical Reporting'), ('Online', 'Online'), ('Hybrid', 'Hybrid')], max_length=20)),
                ('resume', models.BooleanField()),
                ('endorsement', models.BooleanField()),
                ('moa', models.BooleanField()),
                ('remarks', models.CharField(blank=True, max_length=255)),
            ],
        ),
    ]
