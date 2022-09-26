from django.contrib import admin
from .models import City, Language, Vacancy, Error, Url

class CityAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
class LanguageAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(City, CityAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(Vacancy)
admin.site.register(Error)
admin.site.register(Url)


