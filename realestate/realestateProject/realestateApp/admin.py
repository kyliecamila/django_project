from django.contrib import admin
from .models import Article,Category,Memo
# Register your models here.

admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Memo)