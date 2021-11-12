from django.contrib import admin

from pages.models import Matricula, Predio, Propietario


#Clases para editar el admin
class PredioAdmin(admin.ModelAdmin):
    list_display = ('cedula_catastral' ,'direccion')
    search_fileds = ('cedula_catastral' ,'direccion') 
    
class PropietarioAdmin(admin.ModelAdmin):
    list_display = ('nombre' ,'identificacion')
    search_fileds = ('nombre' ,'identificacion') 

class MatriculaAdmin(admin.ModelAdmin):
    list_display = ('propietario' ,'predio')
    search_fileds = ('propietario' ,'predio') 

# Register your models here.
admin.site.register(Predio, PredioAdmin)
admin.site.register(Propietario, PropietarioAdmin)
admin.site.register(Matricula)
