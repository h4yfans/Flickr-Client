from django.contrib import admin
from tags.models import Tag, Search, Like


class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'count', 'created_at', 'searched_at')
    readonly_fields = ('created_at', 'searched_at')
    ordering = ('-searched_at',)


class SearchAdmin(admin.ModelAdmin):
    list_display = ('searched_tag', 'searched_by')
    readonly_fields = ('user',)

    def searched_tag(self, obj):
        return obj.tag.name

    def searched_by(self, obj):
        return obj.user.username

    searched_tag.empty_value_display = '???'
    searched_by.empty_value_display = '???'


class LikeAdmin(admin.ModelAdmin):
    list_display = ('names', 'image_url')

    def names(self, obj):
        users = [user.username for user in obj.users.all()]
        return ', '.join(users)

    def image_url(self, obj):
        return obj.image_url

    image_url.empty_value_display = '???'
    names.empty_value_display = '???'


admin.site.register(Tag, TagAdmin)
admin.site.register(Search, SearchAdmin)
admin.site.register(Like, LikeAdmin)
