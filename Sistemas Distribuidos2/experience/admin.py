from django.contrib import admin
from .models import Experience

# Register your models here.
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('title',)

    class Media:
        css = {
            'all': ('pages/css/custom_ckeditor.css',)
        }


admin.site.register(Experience, ExperienceAdmin)
