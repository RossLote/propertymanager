from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Team)
class TeamAdmin(admin.ModelAdmin):
    pass


@admin.register(models.TeamUser)
class TeamUserAdmin(admin.ModelAdmin):
    pass


@admin.register(models.TeamOwner)
class TeamOwnerAdmin(admin.ModelAdmin):
    pass


