# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('oj', '0003_contestant'),
    ]

    operations = [
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, to_field='id', unique=True)),
                ('submit', models.IntegerField(default=0)),
                ('solved', models.IntegerField(default=0)),
                ('team', models.IntegerField(default=1, max_length=2)),
                ('nickname', models.CharField(max_length=32)),
                ('motto', models.CharField(max_length=300)),
                ('realname', models.CharField(max_length=12)),
                ('studentid', models.CharField(max_length=12)),
                ('score1', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
