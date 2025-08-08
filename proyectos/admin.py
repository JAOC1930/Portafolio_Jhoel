from django.contrib import admin
from .models import Proyecto, Contacto
@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha_inicio', 'fecha_fin', 'estado', 'duracion')
    list_filter = ('estado',)
    search_fields = ('titulo', 'descripcion', 'tecnologias')
    date_hierarchy = 'fecha_inicio'
    fieldsets = (
        ('Información básica', {
            'fields': ('titulo', 'descripcion', 'empresa', 'imagen', 'video_url')
        }),
        ('Fechas', {
            'fields': ('fecha_inicio', 'fecha_fin')
        }),
        ('Detalles técnicos', {
            'fields': ('tecnologias', 'url_demo', 'url_repositorio')
        }),
    )

class ContactoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'celular', 'fecha_contacto')
    search_fields = ('nombre', 'email', 'mensaje', 'celular')
    list_filter = ('fecha_contacto',)
    date_hierarchy = 'fecha_contacto'
    readonly_fields = ('fecha_contacto',) 

admin.site.register(Contacto, ContactoAdmin)
