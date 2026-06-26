from django.db import migrations
from decimal import Decimal

PRODUCTOS_INICIALES = [
    {
        'nombre': 'Router MikroTik CCR2004 Gigabit',
        'categoria': 'Networking',
        'precio': Decimal('129990'),
        'stock': 15,
        'imagen_url': 'https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=500',
        'descripcion': 'Router empresarial para redes de alto rendimiento, ideal para gestionar conectividad en oficinas y empresas.',
    },
    {
        'nombre': 'Switch Cisco Business PoE 24P',
        'categoria': 'Switches',
        'precio': Decimal('624900'),
        'stock': 10,
        'imagen_url': 'https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=500',
        'descripcion': 'Switch Cisco de 24 puertos con soporte PoE, orientado a cámaras IP, puntos de acceso y redes empresariales.',
    },
    {
        'nombre': 'Antena Ubiquiti AirFiber 5XHD',
        'categoria': 'Inalámbrico',
        'precio': Decimal('385500'),
        'stock': 8,
        'imagen_url': 'https://images.unsplash.com/photo-1628126235206-5260b9ea6441?w=500',
        'descripcion': 'Antena para enlaces inalámbricos de largo alcance, pensada para conexiones punto a punto estables.',
    },
    {
        'nombre': 'Bobina Panduit UTP Cat 6 (305m)',
        'categoria': 'Infraestructura',
        'precio': Decimal('95000'),
        'stock': 20,
        'imagen_url': 'https://images.unsplash.com/photo-1563207153-f403bf289096?w=500',
        'descripcion': 'Bobina de cable UTP categoría 6 para instalaciones de red estructurada en oficinas y empresas.',
    },
    {
        'nombre': 'Servidor Dell PowerEdge R640',
        'categoria': 'Data Center',
        'precio': Decimal('1250000'),
        'stock': 4,
        'imagen_url': 'https://www.winpy.cl/files/w13369_440-1.jpg',
        'descripcion': 'Servidor Dell PowerEdge orientado a virtualización, servicios internos y procesamiento empresarial.',
    },
    {
        'nombre': 'Kit Certificador Fluke LinkIQ',
        'categoria': 'Herramientas',
        'precio': Decimal('340000'),
        'stock': 6,
        'imagen_url': 'https://images.unsplash.com/photo-1584432743501-8ee4424368eb?w=500',
        'descripcion': 'Herramienta para certificación y diagnóstico de cableado de red.',
    },
    {
        'nombre': 'Radio Motorola DGM8500e VHF',
        'categoria': 'Radiocomunicación',
        'precio': Decimal('180000'),
        'stock': 12,
        'imagen_url': 'https://innovarcom.cl/wp-content/uploads/2024/07/MOTOROLA-DGM8500e.png',
        'descripcion': 'Radio móvil Motorola para comunicaciones empresariales, seguridad y operación en terreno.',
    },
    {
        'nombre': 'AP Ubiquiti UniFi 6 Pro Indoor',
        'categoria': 'Inalámbrico',
        'precio': Decimal('115000'),
        'stock': 18,
        'imagen_url': 'https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=500',
        'descripcion': 'Punto de acceso WiFi 6 para mejorar cobertura inalámbrica en espacios interiores.',
    },
    {
        'nombre': 'Firewall Fortigate 60F Next-Gen',
        'categoria': 'Seguridad',
        'precio': Decimal('850000'),
        'stock': 5,
        'imagen_url': 'https://images.unsplash.com/photo-1560733685-dcc219616379?w=500',
        'descripcion': 'Firewall de nueva generación para protección de redes empresariales.',
    },
    {
        'nombre': 'UPS APC Smart-UPS 3kVA Online',
        'categoria': 'Energía',
        'precio': Decimal('1120000'),
        'stock': 3,
        'imagen_url': 'https://images.unsplash.com/photo-1518770660439-4636190af475?w=500',
        'descripcion': 'Sistema UPS para respaldo energético y continuidad operacional de equipos críticos.',
    },
    {
        'nombre': 'Patch Panel Cat6 24P Panduit',
        'categoria': 'Infraestructura',
        'precio': Decimal('75000'),
        'stock': 25,
        'imagen_url': 'https://images.unsplash.com/photo-1551703599-6b3e8379aa8b?w=500',
        'descripcion': 'Patch panel de 24 puertos para organización de cableado estructurado.',
    },
    {
        'nombre': 'NAS Synology DiskStation 4-Bay',
        'categoria': 'Almacenamiento',
        'precio': Decimal('540000'),
        'stock': 7,
        'imagen_url': 'https://images.unsplash.com/photo-1614064641938-3bbee52942c7?w=500',
        'descripcion': 'Sistema NAS de 4 bahías para respaldo, almacenamiento compartido y gestión de archivos.',
    },
]


def cargar_productos(apps, schema_editor):
    Producto = apps.get_model('web', 'Producto')
    for datos in PRODUCTOS_INICIALES:
        Producto.objects.get_or_create(nombre=datos['nombre'], defaults=datos)


def eliminar_productos(apps, schema_editor):
    Producto = apps.get_model('web', 'Producto')
    nombres = [p['nombre'] for p in PRODUCTOS_INICIALES]
    Producto.objects.filter(nombre__in=nombres).delete()


class Migration(migrations.Migration):
    dependencies = [
        ('web', '0003_producto_stock'),
    ]

    operations = [
        migrations.RunPython(cargar_productos, eliminar_productos),
    ]
