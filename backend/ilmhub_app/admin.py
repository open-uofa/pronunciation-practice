from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from .models import User, Tab, Chapter, Lesson, StudentLesson, ParentStudent , Parent , Student,Teacher,ContentCreator
from .forms import UserAdminChangeForm, UserAdminCreationForm


class CustomUserAdmin(UserAdmin):
    """
    A Custom admin role to fulfill the requirements of the 'admin' role within the default django admin site.

    :param UserAdmin: The default django admin site.
    """

    #https://www.codingforentrepreneurs.com/blog/how-to-create-a-custom-django-user-model/
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    # list_display = ['first_name', 'last_name', 'role', 'admin']
    list_display = ['username', 'first_name', 'last_name', 'role', 'admin']
    list_filter = ['admin', 'staff', 'role']
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name','role')}),
        ('Permissions', {'fields': ('admin', 'staff')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password', 'password_2','first_name','last_name', 'role')}
        ),
    )
    search_fields = ['username', 'first_name', 'last_name']
    ordering = ['last_name', 'username']
    filter_horizontal = ()

class CustomProxyAdmin(CustomUserAdmin):
    """
    A Custom admin proxy role to fulfill the requirements of the 'admin' role within the default django admin site.

    :param CustomUserAdmin: The customized django default admin user.
    """

    list_display = ['username', 'first_name', 'last_name']
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password', 'password_2','first_name','last_name')}
        ),
    )


# Register your models here.
#admin.site.unregister(Group)
admin.site.register(get_user_model(), CustomUserAdmin)
admin.site.register(Tab)
admin.site.register(Chapter)
admin.site.register(Lesson)
admin.site.register(StudentLesson)
admin.site.register(ParentStudent)
admin.site.register(Parent, CustomProxyAdmin)
admin.site.register(Student, CustomProxyAdmin)
admin.site.register(Teacher, CustomProxyAdmin)
admin.site.register(ContentCreator, CustomProxyAdmin)

