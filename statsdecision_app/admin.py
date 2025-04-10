from django.contrib import admin
from django.contrib.auth.models import User
from .models import Video, Evenement, Document,ImportantLinkCategory, ImportantLink, Category, MessageContact

#admin.site.register(User)
admin.site.register(Video)
admin.site.register(Evenement)
admin.site.register(Document)
admin.site.register(Category)
admin.site.register(MessageContact)
#admin.site.register(CustomUser)

@admin.register(ImportantLinkCategory)
class ImportantLinkCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'color')
    search_fields = ('name',)

@admin.register(ImportantLink)
class ImportantLinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url', 'is_featured', 'click_count')
    list_filter = ('category', 'is_featured')
    search_fields = ('title', 'url', 'description')
    readonly_fields = ('created_at', 'updated_at', 'click_count', 'last_clicked')
    fieldsets = (
        (None, {
            'fields': ('title', 'url', 'description', 'category', 'is_featured')
        }),
        ('Statistiques', {
            'fields': ('click_count', 'last_clicked'),
            'classes': ('collapse',)
        }),
    )