# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('oj', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='article',
            fields=[
                ('article_id', models.IntegerField(serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('content', models.CharField(max_length=10240)),
                ('time', models.DateTimeField()),
                ('clicked', models.IntegerField(default=0)),
                ('user_id', models.ForeignKey(to=settings.AUTH_USER_MODEL, to_field='id')),
                ('parent_id', models.IntegerField(blank=True)),
                ('variety', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
