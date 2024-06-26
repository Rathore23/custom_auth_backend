# Generated by Django 3.2 on 2023-09-17 11:36

import blogs.utils.utils
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('title', models.CharField(help_text='The post title.', max_length=200, verbose_name='Title')),
                ('meta_title', models.TextField(blank=True, help_text='The meta title to be used for browser title and SEO.', null=True, verbose_name='Meta title')),
                ('slug', models.SlugField(blank=True, max_length=250, null=True, verbose_name='Slug')),
                ('published', models.BooleanField(default=False, verbose_name='Published?')),
                ('content', models.TextField(verbose_name='Post content')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_posts', to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category_posts', to='category.category')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
        migrations.CreateModel(
            name='PostPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, height_field='height', null=True, upload_to=blogs.utils.utils.get_post_photo_path, width_field='width')),
                ('width', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('height', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_photos', to='posts.post')),
            ],
        ),
    ]
