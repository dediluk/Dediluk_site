from django.contrib import admin
from books.models import Book, Editor

def make_validated(modeladmin, request, queryset):
    queryset.update(validated=True)
make_validated.short_description = "Mark selected books as validated"

class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title', 'editor', 'asin', 'site', 'validated', 'start_publication_on', 'end_publication_on')
    list_filter = ('site','editor', 'validated', 'start_publication_on', 'end_publication_on')
    search_fields = ('title',)
    actions = [make_validated]
    
admin.site.register(Book, BookAdmin)

class EditorAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    
admin.site.register(Editor, EditorAdmin)