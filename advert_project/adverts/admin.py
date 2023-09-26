from django.contrib import admin
from django.utils.text import slugify
from .models import Advert, Category, City


class AdvertAdmin(admin.ModelAdmin):
    list_display = ('title', 'city', 'category', 'created', 'views')
    list_filter = ('city', 'category', 'created')
    search_fields = ('title', 'description')

    prepopulated_fields = {'slug': ('title',)}

    def save_model(self, request, obj, form, change):
        if not obj.slug:
            obj.slug = slugify(obj.title)
        super().save_model(request, obj, form, change)


admin.site.register(Advert, AdvertAdmin)
admin.site.register(City)
admin.site.register(Category)
