# Nexo Digital - Mejoras Implementadas

## 1. ✅ Nombre del Cliente en la Navbar
- Se agregó la visualización del nombre del cliente registrado en la barra de navegación superior
- Ahora aparece junto a un ícono de persona cuando el usuario está autenticado
- Se usa `user.first_name` (nombre completo del cliente)

## 2. ✅ Control de Acceso con JWT
- Se instaló `djangorestframework` y `djangorestframework-simplejwt`
- Se configuró Django REST Framework con autenticación JWT
- Endpoints de token:
  - `POST /api/token/` - Obtener token de acceso
  - `POST /api/token/refresh/` - Renovar token
- Se creó modelo `UserProfile` con roles:
  - **visitor** - Visitante
  - **client** - Cliente (rol por defecto al registrarse)
  - **admin** - Administrador

## 3. ✅ Formulario de Contacto Funcional
- Se creó modelo `ContactMessage` para almacenar mensajes
- Endpoint API: `POST /api/contact/`
- El formulario ahora es completamente funcional y envía datos a la base de datos
- Los mensajes pueden ser consultados desde el panel de administración Django
- Se agregó `contact.js` para manejo del formulario con validación

## 4. ✅ Rediseño de Envíos y Devoluciones
- **Envíos**: 
  - Se mejoró el diseño con tablas claras
  - Se agregaron colores de badge para diferentes tiempos
  - Se removieron emojis para un diseño más profesional
  - Se añadió una tercera FAQ sobre rastreo
- **Garantía y Devoluciones**:
  - Rediseño con tarjetas más organizadas
  - Tablas con información clara
  - Mejor presentación de información de contacto
  - Íconos profesionales

## 5. ✅ Barra de Búsqueda Funcional
- Se creó `search.js` con funcionalidad completa
- La búsqueda:
  - Filtra productos por nombre y categoría
  - Muestra resultados en tiempo real
  - Aparece en dropdown debajo de la barra
  - Se cierra al perder el foco
- Base de 5 productos de ejemplo que se pueden expandir

## Archivos Modificados/Creados:

### Backend (Python/Django):
- `nexo_backend/settings.py` - Configuración de REST Framework y JWT
- `nexo_backend/urls.py` - Endpoints de API
- `web/models.py` - Modelos ContactMessage y UserProfile
- `web/views.py` - Creación de UserProfile al registrarse
- `web/serializers.py` - **NUEVO** - Serializers para API
- `web/api.py` - **NUEVO** - ViewSets de API
- `web/admin.py` - Registro de modelos en admin

### Frontend (HTML/JS):
- `web/templates/web/base.html` - Mostrar nombre de cliente en navbar
- `web/templates/web/index.html` - Mejorar formulario de contacto
- `web/templates/web/envios.html` - Rediseño completo
- `web/templates/web/garantia.html` - Rediseño completo
- `static/js/contact.js` - **NUEVO** - Manejo de formulario de contacto
- `static/js/search.js` - **NUEVO** - Búsqueda de productos

## Cómo Usar:

### Registrarse como Cliente:
1. Ir a la página de autenticación
2. Llenar formulario de registro
3. Se crea automáticamente un perfil con rol "client"
4. El nombre aparecerá en la navbar

### Enviar Mensaje de Contacto:
1. Scroll hasta la sección "Envíanos un mensaje"
2. Completar formulario con nombre, email y mensaje
3. El mensaje se guarda en la base de datos
4. Puede ser consultado desde `/admin/web/contactmessage/`

### Buscar Productos:
1. Hacer clic en la barra de búsqueda
2. Escribir nombre o categoría del producto
3. Se mostrarán resultados en dropdown
4. Click en resultado para ir a productos

## API Endpoints Disponibles:

```
POST /api/contact/ - Crear mensaje de contacto
GET  /api/profile/me/ - Obtener perfil del usuario autenticado
POST /api/token/ - Obtener JWT token
POST /api/token/refresh/ - Renovar JWT token
```

## Próximas Mejoras Sugeridas:

- Conectar búsqueda a la página de productos con filtros
- Implementar más categorías de productos
- Agregar notificaciones por email al contacto
- Sistema de órdenes y rastreo
- Carrito persistente en base de datos
