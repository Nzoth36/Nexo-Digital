# Generated manually to add Producto model

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('categoria', models.CharField(max_length=100)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=12)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('imagen_url', models.URLField(blank=True, max_length=500, null=True)),
            ],
        ),
    ]
