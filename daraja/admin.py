from django.contrib import admin


class DaraAdmin(admin.ModelAdmin):
    fields = ('description', )
