from django.contrib import admin
from firstapp.models import Memo

# Register your models here.
class MemoAdmin(admin.ModelAdmin):

    List_display = ('content','last_modified')

admin.site.register(Memo, MemoAdmin)