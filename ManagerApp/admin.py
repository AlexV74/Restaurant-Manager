
# Register your models here.

from django import forms
from .models import MenuItems,MenuCategory
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError

from .models import Staff


class UserCreationForm(forms.ModelForm):
    """
    A form for creating new users. Includes all the required fields, plus a repeated password.
    """
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = Staff
        fields = ('STAFF_ID',)

    def clean_password2(self):
        """
        Check that the two password entries match.
        """
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        """
        Save the provided password in hashed format
        """
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """
    A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    disabled password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Staff
        fields = ('STAFF_ID', 'password', 'is_active', 'is_admin')


class UserAdmin(BaseUserAdmin):
    """
    The forms to add and change user instances
    """
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('STAFF_ID', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('STAFF_ID', 'password')}),
#        ('Personal info', {'fields': ('date_of_birth',)}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('STAFF_ID', 'password1', 'password2'),
        }),
    )
    search_fields = ('STAFF_ID',)
    ordering = ('STAFF_ID',)
    filter_horizontal = ()

class MenuCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    
# Register the Menu Category with the admin site
# This will allow administrators to add, edit, and delete Menu Category from the admin page
admin.site.register(MenuCategory, MenuCategoryAdmin)

class MenuItemsAdmin(admin.ModelAdmin):
    list_display = ('name', 'category_name', 'price', 'image')
    list_filter = ('category',)
    search_fields = ('name', 'category__name')

    def category_name(self, obj):
        return obj.category.name
    category_name.admin_order_field = 'category__name'

    
# Register the Menu model with the admin site
# This will allow administrators to add, edit, and delete Menu items from the admin site
admin.site.register(MenuItems, MenuItemsAdmin)


# Now register the new UserAdmin...
admin.site.register(Staff, UserAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)
