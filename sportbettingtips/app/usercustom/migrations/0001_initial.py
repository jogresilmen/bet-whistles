# Generated by Django 4.1.1 on 2022-11-12 19:49

import app.usercustom.models.models
import app.usercustom.sobre_escribir_imagen
from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserCustom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('password', models.CharField(max_length=128, verbose_name='Password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Last login')),
                ('is_superuser', models.BooleanField(db_index=True, default=False, verbose_name='Super Admin')),
                ('is_staff', models.BooleanField(db_index=True, default=False, verbose_name='Staff')),
                ('is_active', models.BooleanField(default=False, verbose_name='Active')),
                ('username', models.CharField(db_index=True, max_length=150, unique=True, verbose_name='User name')),
                ('first_name', models.CharField(max_length=30, verbose_name='Name')),
                ('last_name', models.CharField(max_length=30, verbose_name='Last name')),
                ('email', models.CharField(db_index=True, max_length=254, unique=True, verbose_name='Email')),
                ('email_secundario', models.CharField(blank=True, db_index=True, max_length=254, null=True, unique=True, verbose_name='Secondary email')),
                ('type_user', models.CharField(blank=True, choices=[('U', 'USUARIO'), ('C', 'CLIENTE'), ('A', 'ASOCIADOS')], default='U', max_length=1, null=True, verbose_name='Type User.')),
                ('telefono', models.CharField(blank=True, max_length=255, null=True, verbose_name='Phone')),
                ('celular', models.CharField(blank=True, max_length=255, null=True, verbose_name='Mobile Phone')),
                ('fecha_nacimiento', models.DateField(blank=True, null=True, verbose_name='Birthdate')),
                ('avatar', models.ImageField(blank=True, default='avatar/default_avatar.png', max_length=255, null=True, storage=app.usercustom.sobre_escribir_imagen.SobreEscribirImagen(), upload_to=app.usercustom.models.models.image_path)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('sex', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='main.sex', verbose_name='Sex')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Person',
                'verbose_name_plural': 'People',
                'db_table': 'auth_user',
                'ordering': ['first_name', 'last_name'],
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='HistoricalUserCustom',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('password', models.CharField(max_length=128, verbose_name='Password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Last login')),
                ('is_superuser', models.BooleanField(db_index=True, default=False, verbose_name='Super Admin')),
                ('is_staff', models.BooleanField(db_index=True, default=False, verbose_name='Staff')),
                ('is_active', models.BooleanField(default=False, verbose_name='Active')),
                ('username', models.CharField(db_index=True, max_length=150, verbose_name='User name')),
                ('first_name', models.CharField(max_length=30, verbose_name='Name')),
                ('last_name', models.CharField(max_length=30, verbose_name='Last name')),
                ('email', models.CharField(db_index=True, max_length=254, verbose_name='Email')),
                ('email_secundario', models.CharField(blank=True, db_index=True, max_length=254, null=True, verbose_name='Secondary email')),
                ('type_user', models.CharField(blank=True, choices=[('U', 'USUARIO'), ('C', 'CLIENTE'), ('A', 'ASOCIADOS')], default='U', max_length=1, null=True, verbose_name='Type User.')),
                ('telefono', models.CharField(blank=True, max_length=255, null=True, verbose_name='Phone')),
                ('celular', models.CharField(blank=True, max_length=255, null=True, verbose_name='Mobile Phone')),
                ('fecha_nacimiento', models.DateField(blank=True, null=True, verbose_name='Birthdate')),
                ('avatar', models.TextField(blank=True, default='avatar/default_avatar.png', max_length=255, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('sex', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='main.sex', verbose_name='Sex')),
            ],
            options={
                'verbose_name': 'historical Person',
                'verbose_name_plural': 'historical People',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
