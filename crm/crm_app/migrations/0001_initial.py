# Generated by Django 3.2.6 on 2022-01-04 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100, unique=True)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('type_of_activity', models.CharField(blank=True, max_length=50)),
                ('city', models.CharField(blank=True, max_length=25)),
                ('phone_number_or_fax', models.IntegerField()),
                ('address', models.TextField(blank=True, max_length=100)),
                ('e_mail', models.EmailField(max_length=100)),
                ('ynp', models.IntegerField(blank=True, max_length=9)),
                ('kpp', models.IntegerField(blank=True, max_length=9)),
                ('legal_address', models.TextField(blank=True, max_length=100)),
                ('b_s', models.CharField(blank=True, max_length=28)),
                ('bank', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('post', models.CharField(blank=True, max_length=30)),
                ('phone_number', models.IntegerField()),
                ('e_mail', models.EmailField(blank=True, max_length=50)),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(blank=True, max_length=50)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='crm_app.company')),
            ],
        ),
        migrations.CreateModel(
            name='Deal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profit', models.IntegerField()),
                ('description', models.TextField(blank=True, max_length=150)),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('documents', models.FileField(blank=True, upload_to='documents/')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('date_of_birth', models.DateField()),
                ('phone_number', models.IntegerField()),
                ('post', models.CharField(max_length=30)),
                ('e_mail', models.EmailField(max_length=100)),
                ('photo', models.ImageField(blank=True, upload_to='photos/')),
            ],
        ),
        migrations.CreateModel(
            name='Funnel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('text', models.TextField(blank=True, max_length=250)),
                ('deadline', models.DateTimeField(blank=True)),
                ('note', models.TextField(blank=True, max_length=250)),
                ('employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='crm_app.employee')),
                ('status', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='crm_app.status')),
            ],
        ),
        migrations.CreateModel(
            name='Proposal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('price', models.IntegerField()),
                ('source', models.CharField(max_length=35)),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='crm_app.company')),
                ('contacts', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='crm_app.contacts')),
                ('employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='crm_app.employee')),
                ('funnel', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='crm_app.funnel')),
                ('tasks', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='crm_app.tasks')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('price', models.IntegerField()),
                ('deal', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='crm_app.deal')),
            ],
        ),
        migrations.AddField(
            model_name='deal',
            name='proposal',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='crm_app.proposal'),
        ),
        migrations.AddField(
            model_name='deal',
            name='status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='crm_app.status'),
        ),
        migrations.AddField(
            model_name='company',
            name='responsible',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='crm_app.employee'),
        ),
    ]
