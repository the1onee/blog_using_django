from django.contrib import admin
from .models import Mohmed,skills\
    ,Contact,Comment,viewblogs,catagry,portfol,Services
# Register your models here.
admin.site.register(Mohmed)
admin.site.register(skills)
admin.site.register(catagry)
admin.site.register(viewblogs)
admin.site.register(Comment)
admin.site.register(portfol)
admin.site.register(Contact)
admin.site.register(Services)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)







