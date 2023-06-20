models.py
=========

*All* the tables in the database.

.. py:class:: Manager(BaseUserManager)

    The admin accounts table.

    :param BaseUserManager: From Django.

    .. py:function:: create_user(self, sid, password=None)

        The function for creating a user.

        :param sid: The user ID.
        :param password: The password for the user. Defaults to None.
        :raise ValueError: Raised if an ID isn't entered for the user.
    
    .. py:function:: create_superuser(self, STAFF_ID, password)

        The function for creating a superuser.

        :param STAFF_ID: The superuser ID.
        :param password: The password for the user.


.. py:class:: Staff(AbstractBaseUser)

    The staff accounts table.

    :param AbstractBaseUser: From Django.


.. py:class:: MenuCategory(models.Model)

    The table for the menu categories.

    :param models.Model: From Django.

    .. py:function:: __str__(self)

        Returns the name of the category.

    .. py:function:: clean(self)

        Ensure that the name is unique.

        :raise ValidationError: Raised if a name is duplicated, or at least attempted.


.. py:function:: validate_image_size(image)

    Validates that the uploaded image is no larger than 5MB and is a supported format.

    :param image: The image to be validated.
    :raise ValidationError: Raised if the image is too big or in an unsupported format.


.. py:class:: MenuItems(models.Model)

    The table for the items on the menu.

    :param models.Model: From Django.

    .. py:function:: __str__(self)

        Returns: item - category - price.

        :return: The stringified information of the item

    .. py:function:: clean(self)

        Ensure that the category exists and validates the image size.

        :raise ValidationError: Raised if the category doesn't exist and the image is too big.
    
    .. py:function:: get_absolute_url(self)

        Gets the absolute url.

        :return: Returns the absolute url.


.. py:class:: Order(models.Model)

    The table for the orders.

    :param models.Model: From Django.

    .. py:function:: __str__(self)

        Returns self.order_id.

        :return: Order ID of the order.


.. py:class:: Item(models.Model)

    The table holding information on items.

    :param models.Model: From Django.


.. py:class:: Table(models.Model)

    The table holdig the tables.

    :param models.Model: From Django.
