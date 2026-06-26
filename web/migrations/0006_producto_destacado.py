from django.db import migrations, models


def marcar_productos_destacados(apps, schema_editor):
    Producto = apps.get_model('web', 'Producto')
    for producto in Producto.objects.all().order_by('id')[:3]:
        producto.destacado = True
        producto.save(update_fields=['destacado'])


def desmarcar_productos_destacados(apps, schema_editor):
    Producto = apps.get_model('web', 'Producto')
    Producto.objects.update(destacado=False)


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_crear_usuario_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='destacado',
            field=models.BooleanField(default=False),
        ),
        migrations.RunPython(marcar_productos_destacados, desmarcar_productos_destacados),
    ]
