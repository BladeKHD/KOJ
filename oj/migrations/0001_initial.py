# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='compileinfo',
            fields=[
                ('solution_id', models.IntegerField(serialize=False, primary_key=True)),
                ('error', models.CharField(max_length=1024)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='contest',
            fields=[
                ('contest_id', models.IntegerField(serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('defunct', models.CharField(max_length=1)),
                ('description', models.TextField()),
                ('private', models.IntegerField()),
                ('langmask', models.IntegerField(max_length=11)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='solution',
            fields=[
                ('solution_id', models.IntegerField(max_length=10, serialize=False, primary_key=True)),
                ('problem_id', models.IntegerField(max_length=10)),
                ('user_id', models.CharField(max_length=48)),
                ('time', models.IntegerField(max_length=11)),
                ('memory', models.IntegerField(max_length=11)),
                ('in_date', models.DateTimeField()),
                ('result', models.SmallIntegerField(max_length=6)),
                ('language', models.IntegerField(max_length=10)),
                ('ip', models.CharField(max_length=10)),
                ('contest_id', models.CharField(max_length=11)),
                ('valid', models.IntegerField(max_length=4)),
                ('num', models.IntegerField(max_length=4)),
                ('code_length', models.IntegerField(max_length=11)),
                ('judgetime', models.DateTimeField()),
                ('pass_rate', models.FloatField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='source_code',
            fields=[
                ('solution_id', models.IntegerField(serialize=False, primary_key=True)),
                ('source', models.CharField(max_length=10240)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sender', models.CharField(max_length=50)),
                ('receiver', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('content', models.CharField(max_length=10240)),
                ('time', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='contest_problem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('problem_id', models.IntegerField(max_length=11)),
                ('contest_id', models.IntegerField(max_length=11)),
                ('title', models.CharField(max_length=200, blank=True)),
                ('num', models.IntegerField(max_length=11)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='problem',
            fields=[
                ('problem_id', models.IntegerField(max_length=10, serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('input', models.TextField()),
                ('output', models.TextField()),
                ('sample_input', models.TextField()),
                ('sample_output', models.TextField()),
                ('spj', models.IntegerField(max_length=2)),
                ('hint', models.TextField(blank=True)),
                ('source', models.CharField(max_length=100, blank=True)),
                ('in_date', models.DateTimeField()),
                ('time_limit', models.IntegerField(max_length=1)),
                ('memory_limit', models.IntegerField(max_length=1)),
                ('defunct', models.CharField(max_length=1)),
                ('accepted', models.IntegerField(max_length=1)),
                ('submit', models.IntegerField(max_length=1)),
                ('solved', models.IntegerField(max_length=1)),
                ('mark', models.IntegerField(default=5)),
                ('diff', models.IntegerField(default=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='runtimeinfo',
            fields=[
                ('solution_id', models.IntegerField(serialize=False, primary_key=True)),
                ('error', models.CharField(max_length=1024)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
