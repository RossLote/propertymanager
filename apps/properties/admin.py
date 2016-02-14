from django.contrib import admin
from . import models

@admin.register(models.Property)
class PropertyAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Unit)
class UnitAdmin(admin.ModelAdmin):
    pass

@admin.register(models.PropertyAttribute)
class PropertyAttributeAdmin(admin.ModelAdmin):
    pass

@admin.register(models.UnitAttribute)
class UnitAttributeAdmin(admin.ModelAdmin):
    pass
