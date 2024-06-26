# Generated by Django 5.0.2 on 2024-02-23 04:25
from django.contrib.contenttypes.models import ContentType
from django.core.management.sql import emit_post_migrate_signal
from django.db import migrations


def create_groups(apps, schema_migration):
    emit_post_migrate_signal(verbosity=1, interactive=False, db='default')

    User = apps.get_model('authentication', 'User')
    Group = apps.get_model('auth', 'Group')
    Permission = apps.get_model('auth', 'Permission')

    add_blog = Permission.objects.get(codename='add_blog')
    change_blog = Permission.objects.get(codename='change_blog')
    delete_blog = Permission.objects.get(codename='delete_blog')
    view_blog = Permission.objects.get(codename='view_blog')

    author_permissions = [
        add_blog,
        change_blog,
        delete_blog,
        view_blog,
    ]

    reader_permissions = [
        view_blog,
    ]

    authors = Group(name='authors')
    authors.save()
    authors.permissions.set(author_permissions)

    readers = Group(name='readers')
    readers.save()
    readers.permissions.add(reader_permissions)

    admin = Group(name='admin')
    admin.save()
    permissions = Permission.objects.all()
    admin.permissions.add(view_blog)

    for user in User.objects.all():
        if user.role == 'AUTHOR':
            authors.user_set.add(user)
        if user.role == 'READER':
            readers.user_set.add(user)
        if user.role == 'ADMIN':
            admin.user.set_add(user)


class Migration(migrations.Migration):
    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_groups)
    ]
