from django.contrib import admin
from Meetings.models import Usuarios

# Register your models here.
class UsuariosAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'usuario', 'email', 'tel')
    list_filter = ('codigo_postal',) #Filtro derecha
    search_fields = ('nombre', 'apellido', 'email') #casilla de busqueda

admin.site.register(Usuarios, UsuariosAdmin)
