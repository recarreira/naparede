from django.contrib import admin
from models import Author
from models import Link

class InlineLink(admin.TabularInline):
    model = Link

class AuthorAdmin(admin.ModelAdmin):
    inlines = [InlineLink]
    list_display = ('name', )

admin.site.register(Author, AuthorAdmin)