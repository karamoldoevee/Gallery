from django.contrib import admin
from webapp.models import Photo, Comment


class ReviewtAdmin(admin.TabularInline):
    model = Comment
    fields = ['text', 'author']
    readonly_fields = ['created_at']
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    fields = ['image', 'signature', 'author']
    list_display = ['pk', 'image', 'signature', 'author', 'created_at']
    list_display_links = ['pk']
    inlines = [ReviewtAdmin]


admin.site.register(Photo, ProductAdmin)
admin.site.register(Comment)
