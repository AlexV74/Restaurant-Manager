admin.py
========

.. py:class:: UserCreationForm(forms.ModelForm)

    A form for creating new users. Includes all the required fields, plus a repeated password.

    .. py:function:: clean_password2(self)

        Check the two password entries match.

        :param forms.ModelForm: Django's form stuff 
        :raise: ValidationError: The passwords don't match.
        :return: The second password.
    
    .. py:function:: save(self, commit=True)

        Save the provided password in hashed format.

        :param commit: A switch to decide whether to save or not.
        :return: The user.


.. py:class:: UserChangeForm(forms.ModelForm)

    A form for updating users. Includes all the fields on the user, but replaces the password field with admin's
    disabled password hash display field.

    :param forms.ModelForm: Django's form stuff.


.. py:class:: UserAdmin(BaseUserAdmin)

    The forms to add and change user instances.

    :param BaseUserAdmin: Django's user stuff.


.. py:class:: MenuCategoryAdmin(admin.ModelAdmin)

    For setting up the category's in the menu.

    :param admin.ModelAdmin: from Django.


.. py:class:: MenuItemsAdmin(admin.ModelAdmin)

    For setting up the items in the menu.

    :param admin.ModelAdmin: from Django.
