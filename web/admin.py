from django.contrib import admin
from .models import ContactMessage, UserProfile, Producto

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'created_at', 'read')
    list_filter = ('created_at', 'read')
    search_fields = ('full_name', 'email', 'message')
    readonly_fields = ('created_at',)

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role', 'created_at')
    list_filter = ('role', 'created_at')
    search_fields = ('user__username', 'user__email')
    readonly_fields = ('created_at',)


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'precio', 'stock', 'destacado')
    list_filter = ('categoria', 'destacado')
    search_fields = ('nombre', 'categoria', 'descripcion')