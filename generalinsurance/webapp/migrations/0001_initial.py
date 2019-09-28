# Generated by Django 2.2.4 on 2019-09-09 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GenAgentMaster',
            fields=[
                ('agent_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('agent_name', models.CharField(blank=True, max_length=120, null=True)),
                ('agent_dob', models.DateField(blank=True, null=True)),
                ('agent_qualification', models.CharField(blank=True, max_length=120, null=True)),
                ('agent_join_date', models.DateField(auto_now_add=True, null=True)),
                ('agent_start_date', models.DateField(blank=True, null=True)),
                ('agent_end_date', models.DateField(blank=True, null=True)),
                ('agent_status', models.CharField(blank=True, max_length=20, null=True)),
                ('created_date', models.DateField(auto_now_add=True, null=True)),
                ('last_updated_by', models.CharField(blank=True, max_length=200, null=True)),
                ('last_updated_date', models.DateField(auto_now_add=True, null=True)),
            ],
        ),
    ]