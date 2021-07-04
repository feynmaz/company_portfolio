from django.contrib import admin

from .models import *


class UserProfileAdmin(admin.ModelAdmin):
    model = UserProfile
    list_display = (
        'username',
        'email',
        'is_staff',
    )
    fields = (
        ('username', 'email'),
        ('first_name', 'last_name'),
        ('is_staff', 'is_superuser'),
        ('last_login', 'date_joined')
    )
    readonly_fields = ('last_login', 'date_joined')


admin.site.register(UserProfile, UserProfileAdmin)



class UserCompanyRelationshipAdmin(admin.ModelAdmin):
    model = UserCompanyRelationship
    list_display = ('company',)
    fields = (
        ('company', 'user',), 
    )

    
admin.site.register(UserCompanyRelationship, UserCompanyRelationshipAdmin)