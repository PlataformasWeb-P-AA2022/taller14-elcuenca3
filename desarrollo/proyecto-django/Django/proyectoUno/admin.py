from django.contrib import admin

# Importar las clases del modelo
from proyectoUno.models import Edificio, Departamento

# Edificio
class EdificioAdmin(admin.ModelAdmin):

    list_display = ('nombre', 'edad', )
    search_fields = ('nombre',)

admin.site.register(Edificio, EdificioAdmin)


class DepartamentoAdmin(admin.ModelAdmin):

    list_display = ('costo',)
    raw_id_fields = ('propietario',)

admin.site.register(Departamento, DepartamentoAdmin)