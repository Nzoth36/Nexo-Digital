from django.db import migrations


ADMIN_USERNAME = 'Admin'
ADMIN_EMAIL = 'Admin@gmail.com'
ADMIN_PASSWORD_HASH = 'pbkdf2_sha256$1200000$yhagCHLF0t2EaqFpJmV4Wy$oTDfTd18OpTv669z8iTeE2nLUKiRY7RzbghtNMZ+aJM='


def crear_usuario_admin(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    UserProfile = apps.get_model('web', 'UserProfile')

    user = User.objects.filter(email=ADMIN_EMAIL).first()

    if user is None:
        user = User.objects.create(
            username=ADMIN_USERNAME,
            email=ADMIN_EMAIL,
            password=ADMIN_PASSWORD_HASH,
            is_staff=True,
            is_superuser=True,
            is_active=True,
        )
    else:
        user.username = user.username or ADMIN_USERNAME
        user.password = ADMIN_PASSWORD_HASH
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save()

    profile, _ = UserProfile.objects.get_or_create(user=user)
    profile.role = 'admin'
    profile.save()


def revertir_usuario_admin(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    User.objects.filter(email=ADMIN_EMAIL).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_cargar_productos_iniciales'),
    ]

    operations = [
        migrations.RunPython(crear_usuario_admin, revertir_usuario_admin),
    ]
