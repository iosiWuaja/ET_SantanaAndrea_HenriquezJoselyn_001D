# Generated by Django 5.0.6 on 2024-07-14 20:27

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patitas', '0004_alter_producto_imagen_carrito'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='carrito',
            unique_together={('usuario', 'producto')},
        ),
    ]
