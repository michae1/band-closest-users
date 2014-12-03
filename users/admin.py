from django.contrib import admin
from users.models import SocialUser, SocialGroup

class SocialUserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'social_id')
    list_filter = ()

class SocialGroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'social_id')
    list_filter = ()
    
    # search_fields = ('email',)
    # ordering = ('email',)


admin.site.register(SocialUser, SocialUserAdmin)
admin.site.register(SocialGroup, SocialGroupAdmin)
