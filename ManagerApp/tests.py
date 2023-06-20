from django.test import TestCase
from .models import MenuCategory, MenuItems, Manager, Staff, Order, Item, Payment
from django.core.exceptions import ValidationError

class MenuCategoryTestCase(TestCase):
    def setUp(self):
        self.category = MenuCategory.objects.create(
            name="test category",
            description="test category description"
        )

    def test_menucategory_exists(self):
        menu_category = MenuCategory.objects.get(name="test category")
        self.assertEqual(menu_category, self.category)

    def test_menucategory_description_optional(self):
        menu_category = MenuCategory.objects.create(name="test category")
        self.assertEqual(menu_category.name, "test category")
        self.assertEqual(menu_category.description, "")

    def test_menucategory_str_method(self):
        expected_str = "test category"
        self.assertEqual(str(self.category), expected_str)


class MenuItemsTestCase(TestCase):
    def setUp(self):
        self.category = MenuCategory.objects.create(
            name="test category",
            description="test category description"
        )
        self.menu_item = MenuItems.objects.create(
            name="test item",
            description="test description",
            price=9.99,
            category=self.category,
            calories=500,
            ingredients="test ingredient 1, test ingredient 2",
        )

    def test_menuitem_exists(self):
        menu_item = MenuItems.objects.get(name="test item")
        self.assertEqual(menu_item, self.menu_item)

    def test_menuitem_price_not_negative(self):
        self.assertGreaterEqual(self.menu_item.price, 0)

    def test_menuitem_calories_not_negative(self):
        self.assertGreaterEqual(self.menu_item.calories, 0)
        
    def test_menuitem_calories_min_value(self):
        self.menu_item.calories = 0
        with self.assertRaises(ValidationError):
            self.menu_item.full_clean()

    def test_menuitem_calories_max_value(self):
        self.menu_item.calories = 10000
        with self.assertRaises(ValidationError):
            self.menu_item.full_clean()

    def test_menuitem_price_min_value(self):
        self.menu_item.price = 0
        with self.assertRaises(ValidationError):
            self.menu_item.full_clean()

    def test_menuitem_price_max_value(self):
        self.menu_item.price = 10000.00
        with self.assertRaises(ValidationError):
            self.menu_item.full_clean()

    def test_menuitem_str_method(self):
        expected_str = "test item - test category - £9.99"
        self.assertEqual(str(self.menu_item), expected_str)

    def test_menuitem_ingredients_not_empty(self):
        self.assertNotEqual(self.menu_item.ingredients, "")
        
        
    def test_menuitem_ingredients_max_length(self):
        self.menu_item.ingredients = "egg" * 2000 # ingredients field containing word 200 eggs exceeds limit
        with self.assertRaises(ValidationError):
            self.menu_item.clean_fields()
            
    def test_menuitem_ingredients_invalid_chars(self):
            self.menu_item.price = 2.00
            self.menu_item.ingredients = "200*131234[][][][]$%^&£$£""%()"
            with self.assertRaises(ValidationError):
                self.menu_item.full_clean()
"""
class TestLogInLogOut(TestCase):
    def init(self):
        Manager.objects.create('1001', "testingpw")
        Staff.objects.create('1002', "testingname")

    def testCreateUsers(self):
        Manager.create_user('1003', "testingpw")

    def testCreateSuperUser(self):
        Manager.create_superuser('1004', "testingpw")
"""
class TestOrder(TestCase):
    def init(self):
        Order.objects.create()

    def setOrder(self):
        o = Order.objects.create()
        print(o.str())
        o.preparing = False
    
    def deleteOrder(self):
        o = Order.objects.create()
        print(o.str())
        o.delete()
    
    def orderFiltering(self):
        o1 = Order.objects.create()
        o1.order_id = 1
        o2 = Order.objects.filter(order_id = 1)
        self.assertEqual(o1, o2)

class TestItem(TestCase):
    def init(self):
        Item.objects.create()

    def testLinkedList(self):
        i = Item.objects.create()
        i.iname = "Item1"
        j = Item.objects.create()
        j.iname = "Item2"
        k = Item.objects.create()
        k.iname = "Item3"

        for item in Item.objects.filter(previous__isnull=True):
            print(item)
            while(item.previous):
               print(item.previous)
               item = item.previous
        
class PaymentTestCase(TestCase):
    def setUp(self):
        Payment.objects.create(
            cardholder_name="John Smith",
            card_number="1234 1234 1234 1234",
            expiry_date="2023-05-01",
            cvv="000"
        )
        def test_payment(self):
            payment = Payment.objects.get(cardholder_name="John Smith")
        self.assertEqual(str(payment), "Payment 1")    
        
        
class TestViews(TestCase):

    def testwaiter(self):
        response = self.client.get('/waiter')
        self.assertEqual(response.status_code, 301)
        # 301 since you should have to login to see the waiter page
    
    def testhome(self):
        response = self.client.get('/activeorders/home/')
        self.assertEqual(response.status_code, 200)
        # 200 is html code for OK
    

    def testcheckout(self):
        response = self.client.get('/activeorders/checkout/')
        self.assertEqual(response.status_code, 200)
    

    def testabout(self):
        response = self.client.get('/activeorders/about/')
        self.assertEqual(response.status_code, 200)
    def testcontactus(self):
        response = self.client.get('/activeorders/contactus/')
        self.assertEqual(response.status_code, 200)

    def testkitchen(self):
        response = self.client.get('/activeorders')
        self.assertEqual(response.status_code, 301)
        # same reason as waiter