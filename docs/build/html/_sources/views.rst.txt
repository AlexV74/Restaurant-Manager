views.py
========

Holds information on all of the pages and any functionality those pages need/have.

.. py:function:: activeorders(request)

    Shows orders that have been placed and have not been completed yet.

    :param request: From Django.
    :return: Renders the actual page from the html template.


.. py:function:: ReadyToDeliver(request, id)

    Filters and shows which orders are finished cooking and are ready to be delivered.

    :return: Does the action upon activeorders.


.. py:function:: home(request)

    Shows the homepage, which is the customer facing part of the app.

    :param request: From Django.
    :return: Renders the actual page from the html template.


.. py:function:: menu_item_details(request, item_id)

    Gives more details on the specific item.

    :param request: From Django.
    :param item_id: The ID of the item for which more details will be given.
    :return: Shows the extra information.


.. py:function:: tableNumber(request)

    Sets the table number from user submitted value from post request.

    :param request: From Django.
    :return: The HTTPS response.


.. py:function:: SubmitOrder(request)

    Submit the order when the customer goes through checkout

    :param request: From Django.
    :return: The HTTPS response.


.. py:function:: addItem(request, iname, item_id)

    Adds an item to the basket (varying quantity).

    :param request: From Django.
    :param iname: The item name.
    :param item_id: The item ID.
    :return: The HTTPS response.


.. py:function:: waiter(request)

    Render the waiter page, waiter can see orders and their status.

    :param request: From Django.
    :return: Renders the actual page from the html template.


.. py:function:: about(request)

    Render the about us page

    :param request: From Django.
    :return: Renders the actual page from the html template.


.. py:function:: checkout(request)

    Renders the checkout, showing the items in the basket

    :param request: From Django.
    :return: Renders the actual page from the html template.


.. py:function:: Delivered(request, id)

    Deletes an order from the order table since the order has been delivered.

    :param request: From Django.
    :param id: The ID of the order that's been delivered.
    :return: Renders the actual page from the html template.


.. py:function:: Cancelled(request)

    Deletes an order since it's been cancelled by the customer

    :param request: From Django.
    :return: Renders the actual page from the html template.