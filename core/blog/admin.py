from django.contrib import admin
from .models import Post


# Register your models here.
# Forma 1 de registrar modelos
# admin.site.register(Post)

# Forma 2 de registrar modelos
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'slug', 'author', 'created_at', 'updated_at', 'status')
    list_filter = ('status', 'created_at', 'updated_at')
    search_fields = ('title', 'subtitle', 'content')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('status', 'created_at')
    date_hierarchy = 'created_at'
    raw_id_fields = ('author',)
    # fields = ('title', 'subtitle', 'slug', 'author', 'content', 'status')
    fieldsets = (
        ('Post', {
            'fields': ('title', 'subtitle', 'slug', 'author', 'content')
        }),
        ('Status & Date', {
            'fields': ('status', 'created_at', 'updated_at')
        })
    )
