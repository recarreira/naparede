from django.contrib import admin
from models import Painting
from models import Image

class InlineImage(admin.TabularInline):
 	model = Image

class PaintingAdmin(admin.ModelAdmin):
    inlines = [InlineImage]
    list_display = ('title', )

admin.site.register(Painting, PaintingAdmin)