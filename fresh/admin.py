from django.contrib import admin
import models


class FreshAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')

admin.site.register(models.Fresh, FreshAdmin)
