from django.contrib import admin
from django.utils.safestring import mark_safe
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model
#from .models import Skill

from users.forms import UserChangeForm, UserCreationForm

User = get_user_model()


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):

    form = UserChangeForm
    add_form = UserCreationForm
    fieldsets = (("User", {"fields": ("image",)}),) + auth_admin.UserAdmin.fieldsets
    list_display = ["username", "first_name", "is_superuser"]
    search_fields = ["first_name"]
    readonly_fields = ['avatar_admin']

    list_display = auth_admin.UserAdmin.list_display + ('avatar_admin',)

    def avatar_admin(self, obj):
        return mark_safe(
            f'<figure><img width="100px" height="100px" src="{obj.get_avatar}"></figure>'
        ) # noqa

    avatar_admin.allow_tags = True
    avatar_admin.short_description = 'Avatar'
    fieldsets = (
        ('User Profile', {'fields': (
            'avatar_admin','avatar',
        )}),
    ) + auth_admin.UserAdmin.fieldsets

#admin.site.register(Skill)

"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.safestring import mark_safe

from .models import UserProfile


class UserProfileAdmin(UserAdmin):

    list_display = UserAdmin.list_display + ('avatar_admin',)

    def avatar_admin(self, obj):
        return mark_safe('<figure><img width="60px" height="60px" src="{}"></figure>'.format(obj.avatar.url)) # noqa

    avatar_admin.allow_tags = True
    avatar_admin.short_description = 'Avatar'
    fieldsets = UserAdmin.fieldsets + (
        ('User Profile', {'fields': (
            'avatar',
        )}),
    )


admin.site.register(UserProfile, UserProfileAdmin)
"""

"""
from django.contrib import admin 
from django.contrib.auth.models import User 
from django.utils.safestring import mark_safe
from django.contrib.auth.admin import UserAdmin 
from .models import Profile 
 
 
class UserProfileInline(admin.StackedInline): 
    model = Profile 
 
 
class NewUserAdmin(UserAdmin): 
    inlines = [UserProfileInline] 
    list_display = UserAdmin.list_display + ('avatar_admin',)

    def avatar_admin(self, obj):
        return mark_safe('<figure><img width="60px" height="60px" src="{}"></figure>'.format(obj.avatar.url)) # noqa

    avatar_admin.allow_tags = True
    avatar_admin.short_description = 'Avatar'
    fieldsets = UserAdmin.fieldsets + (
        ('User Profile', {'fields': (
            'avatar',
        )}),
    )
 
 
admin.site.unregister(User) 
admin.site.register(User, NewUserAdmin) 
"""