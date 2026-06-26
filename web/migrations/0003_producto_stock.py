# Generated manually for Nexo Digital
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_producto'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='stock',
            field=models.PositiveIntegerField(default=10),
        ),
    ]
