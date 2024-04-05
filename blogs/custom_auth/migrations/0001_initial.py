# Generated by Django 3.2 on 2023-09-17 11:36

import blogs.custom_auth.managers
import blogs.custom_auth.utils
import blogs.utils.utils
from django.conf import settings
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import phonenumber_field.modelfields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('photo', models.ImageField(blank=True, height_field='height_photo', null=True, upload_to=blogs.utils.utils.get_user_photo_random_filename, width_field='width_photo')),
                ('width_photo', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('height_photo', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, error_messages={'unique': 'A user with that uuid already exists.'}, help_text='Required. A 32 hexadecimal digits number as specified in RFC 4122.', unique=True, verbose_name='uuid')),
                ('username', models.CharField(blank=True, error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, null=True, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('email', models.EmailField(blank=True, error_messages={'unique': 'A user with that email already exists.'}, max_length=254, null=True, unique=True, verbose_name='email address')),
                ('is_email_verified', models.BooleanField(default=True, verbose_name='email verified')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('fullname', models.CharField(blank=True, help_text='Full name as it was returned by social provider', max_length=300, verbose_name='full name')),
                ('about', models.TextField(blank=True, max_length=1000, verbose_name='about me')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='last modified')),
                ('last_user_activity', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last activity')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, error_messages={'unique': 'A user with that phone already exists.'}, max_length=128, null=True, region=None, unique=True, verbose_name='Phone')),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], default='male', max_length=10)),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='date of birth')),
                ('city', models.CharField(blank=True, max_length=100, null=True, verbose_name='city')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
            managers=[
                ('objects', blogs.custom_auth.managers.ApplicationUserManager()),
            ],
        ),
        migrations.CreateModel(
            name='PasswordResetId',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, primary_key=True, serialize=False)),
                ('expiration_time', models.DateTimeField(default=blogs.custom_auth.utils.set_password_reset_expiration_time)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Password reset id',
            },
        ),
    ]
