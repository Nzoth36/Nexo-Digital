from django.urls import path
from . import views

app_name = 'web'

urlpatterns = [
    path('', views.auth_view, name='auth'),
    path('login/', views.login_view, name='login_view'),
    path('register/', views.register_view, name='register_view'),
    path('logout/', views.logout_view, name='logout'),
    path('inicio/', views.index, name='index'),
    path('productos/', views.productos, name='productos'),
    path('mision/', views.mision, name='mision'),
    path('pago/', views.pago, name='pago'),
    path('envios/', views.envios, name='envios'),
    path('contacto/', views.contacto, name='contacto'),
    path('garantia/', views.garantia, name='garantia'),
    path('panel-admin/', views.admin, name='admin'),
    path('panel-admin/productos/nuevo/', views.admin_producto_crear, name='admin_producto_crear'),
    path('panel-admin/productos/<int:producto_id>/editar/', views.admin_producto_editar, name='admin_producto_editar'),
    path('panel-admin/productos/<int:producto_id>/eliminar/', views.admin_producto_eliminar, name='admin_producto_eliminar'),
    path('panel-admin/mensajes/<int:mensaje_id>/leido/', views.admin_mensaje_marcar_leido, name='admin_mensaje_marcar_leido'),
    path('panel-admin/mensajes/<int:mensaje_id>/eliminar/', views.admin_mensaje_eliminar, name='admin_mensaje_eliminar'),
    path('panel-admin/usuarios/<int:user_id>/rol/', views.admin_usuario_cambiar_rol, name='admin_usuario_cambiar_rol'),
    path('panel-admin/usuarios/<int:user_id>/eliminar/', views.admin_usuario_eliminar, name='admin_usuario_eliminar'),
    path('api/buscar/', views.buscar_productos_ajax, name='buscar_productos_ajax'),
    path('producto/<int:producto_id>/', views.detalle_producto, name='detalle_producto'),
]