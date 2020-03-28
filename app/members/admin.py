from django.contrib import admin

from members.models import User, UserProfile


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'profile'


class UserAdmin(admin.ModelAdmin):
    inlines = (UserProfileInline,)

    fields = [
        'username',
        'email',
        'gender',
        'age',
        'average_point',
        'job',
        'major',
        'birth_date',
        'result',
        'status',
        'chance',
    ]


class UserProfileAdmin(admin.ModelAdmin):
    fields = [
        'author_id',
        'religion',
        'media',
    ]


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(User, UserAdmin)
