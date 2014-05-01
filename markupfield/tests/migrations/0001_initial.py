# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations
import markupfield.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name=b'Concrete',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                (b'content', markupfield.fields.MarkupField()),
                (b'content_markup_type', models.CharField(default=None, max_length=30, choices=[(b'', b'--'), (b'markdown', b'markdown'), (b'ReST', b'ReST'), (b'plain', b'plain')])),
                (b'_content_rendered', models.TextField(editable=False)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name=b'Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                (b'normal_field', markupfield.fields.MarkupField()),
                (b'markup_choices_field', markupfield.fields.MarkupField()),
                (b'normal_field_markup_type', models.CharField(default=None, max_length=30, choices=[(b'', b'--'), (b'markdown', b'markdown'), (b'ReST', b'ReST'), (b'plain', b'plain')])),
                (b'markup_choices_field_markup_type', models.CharField(default=None, max_length=30, choices=[(b'', b'--'), (b'pandamarkup', b'pandamarkup'), (b'nomarkup', b'nomarkup')])),
                (b'default_field', markupfield.fields.MarkupField()),
                (b'_normal_field_rendered', models.TextField(editable=False)),
                (b'_markup_choices_field_rendered', models.TextField(editable=False)),
                (b'default_field_markup_type', models.CharField(default=b'markdown', max_length=30, choices=[(b'', b'--'), (b'markdown', b'markdown'), (b'ReST', b'ReST'), (b'plain', b'plain')])),
                (b'markdown_field', markupfield.fields.MarkupField()),
                (b'_default_field_rendered', models.TextField(editable=False)),
                (b'markdown_field_markup_type', models.CharField(default=b'markdown', max_length=30, editable=False, choices=[(b'', b'--'), (b'markdown', b'markdown'), (b'ReST', b'ReST'), (b'plain', b'plain')])),
                (b'_markdown_field_rendered', models.TextField(editable=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name=b'Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                (b'title', models.CharField(max_length=50)),
                (b'body', markupfield.fields.MarkupField(verbose_name=b'body of post')),
                (b'body_markup_type', models.CharField(default=None, max_length=30, choices=[(b'', b'--'), (b'markdown', b'markdown'), (b'ReST', b'ReST'), (b'plain', b'plain')])),
                (b'comment', markupfield.fields.MarkupField()),
                (b'_body_rendered', models.TextField(editable=False)),
                (b'comment_markup_type', models.CharField(default=b'markdown', max_length=30, choices=[(b'', b'--'), (b'markdown', b'markdown'), (b'ReST', b'ReST'), (b'plain', b'plain')])),
                (b'_comment_rendered', models.TextField(editable=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
