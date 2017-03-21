from django.contrib import admin
from article import models


# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    fieldsets = [
        # (None, {'fields': ['Article_text', 'Article_url', 'Article_image', 'abstract']}),
        (None, {'fields': ['Article_text', 'Article_url', 'img_url']}),
        (None, {'fields': ['cat', 'pub_date']}),
    ]

    list_display = ('Article_text', 'cat','pub_date')
    search_fields = ['Article_text','cat__Categary_text']# cat__Categary_text 外键



# admin.site.register(models.Question, QuestionAdmin)
admin.site.register(models.Article, ArticleAdmin)
admin.site.register(models.Categary)

