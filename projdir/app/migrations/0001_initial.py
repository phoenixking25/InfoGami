# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-31 11:29
from __future__ import unicode_literals

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
            name='CodehubTopicCommentModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.CharField(max_length=500)),
                ('timeStamp', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='CodehubTopicModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic_heading', models.CharField(max_length=100)),
                ('topic_detail', models.CharField(max_length=200)),
                ('topic_link', models.CharField(max_length=100)),
                ('tags', models.CharField(max_length=50)),
                ('timeStamp', models.DateTimeField()),
                ('topic_type', models.CharField(max_length=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='codehubtopiccommentmodel',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.CodehubTopicModel'),
        ),
        migrations.AddField(
            model_name='codehubtopiccommentmodel',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]