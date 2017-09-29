from django.contrib import admin
from . models import Add_Word

# Register your models here.

class Add_WordAdmin(admin.ModelAdmin):
    list_display = ('id','word_text','date_time')

admin.site.register(Add_Word,Add_WordAdmin)
