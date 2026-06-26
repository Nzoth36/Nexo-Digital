# Nexo Digital

Proyecto web desarrollado con Django para una tienda de productos de telecomunicaciones.

## Tecnologías

- Python
- Django
- SQLite
- HTML
- CSS
- Bootstrap
- JavaScript

## Instalación

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## URLs principales

Sitio:

```text
http://127.0.0.1:8000/
```

Panel administrador:

```text
http://127.0.0.1:8000/panel-admin/
```

## Credenciales de prueba

```text
Correo: Admin@gmail.com
Contraseña: 1029384756
```

## Funciones principales

- Registro e inicio de sesión de usuarios.
- Redirección automática: administrador al panel-admin y usuario normal al inicio.
- Catálogo de productos conectado a base de datos.
- Detalle dinámico de productos.
- Stock visible para el usuario.
- Carrito con límite de unidades y control de stock.
- Panel administrativo propio sin barra lateral.
- Crear, editar y eliminar productos.
- Ver y eliminar usuarios.
- Cambiar rol de usuarios.
- Ver, marcar como leídos y eliminar mensajes de contacto.
- Productos iniciales cargados por migraciones.
