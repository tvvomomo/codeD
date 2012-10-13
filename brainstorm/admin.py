from django.contrib import admin
from brainstorm.models import KeyWord

class KeyWordAdmin(admin.ModelAdmin):
	list_display = ('word_name', 'create_date', 'link', 'rel_word')
	search_field = ('word_name', )
	
admin.site.register(KeyWord, KeyWordAdmin)