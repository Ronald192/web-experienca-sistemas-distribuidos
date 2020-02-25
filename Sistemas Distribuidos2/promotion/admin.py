from django.contrib import admin
from .models import Promotion

# Register your models here.

class PromotionAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created_at', 'updated_at']
    list_filter = ['created_at', 'updated_at']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Promotion, PromotionAdmin)