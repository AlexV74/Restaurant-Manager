from django.db import models
from django.core.exceptions import ValidationError
from PIL import Image
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator, MaxLengthValidator, RegexValidator
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone

class Manager(BaseUserManager):
    """
    The admin accounts database
    """
    def create_user(self, sid, password=None):
        """
        For creating a user
        """
        if not sid:
            raise ValueError("Users must have an ID")

        user = self.model(STAFF_ID=sid)

        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_superuser(self, STAFF_ID, password):
        """
        For creating a cooler user
        """
      #  print(STAFF_ID + password)
        user = self.create_user(
            STAFF_ID,
            password=password,
            )
        user.is_admin = True
        user.save(using = self._db)
        return user

class Staff(AbstractBaseUser): 
    STAFF_ID = models.CharField(max_length = 4, unique = True)
    name = models.CharField(max_length = 20, default = "Unset Name")
    is_active = models.BooleanField(default = True)
    is_admin = models.BooleanField(default = False)

    USERNAME_FIELD = "STAFF_ID"

    REQUIRED_FIELDS = []

    objects = Manager()

    @property
    def is_staff(self):
        return self.is_admin

    def __str__(self):
        return self.STAFF_ID

    def has_module_perms(self, webapp):
        return True

    def has_perm(self, permission, obj=None):
        return True

    
class MenuCategory(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
    def clean(self):
        """
        Ensure that the name is unique
        """
        # Ensure that the name is unique
        existing_category = MenuCategory.objects.filter(name__iexact=self.name).exclude(pk=self.pk).exists()
        if existing_category:
            raise ValidationError("A menu category with this name already exists.")
    
    class Meta:
        verbose_name_plural = "Menu Categories"
    
def validate_image_size(image):
    """
    Validates that the uploaded image is no larger than 5MB and is a supported format
    """
    if image.file.size > 5 * 1024 * 1024:
        raise ValidationError("The uploaded image is too large (max size is 5MB).")
    
    # Also validate that the image is in a supported format
    try:
        with Image.open(image) as img:
            pass
    except:
        raise ValidationError("Unsupported image format.")
    
class MenuItems(models.Model):
    """
    The table for the items on the menu
    """
    item_id = models.AutoField(unique = False, primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(0.01)])
    category = models.ForeignKey(MenuCategory, on_delete=models.CASCADE, related_name='menu_items')
    calories = models.PositiveIntegerField(blank=True, null=True)
    ingredients = models.CharField(max_length=200, validators=[
        MaxLengthValidator(limit_value=200, message="Ingredients list is too long"),
        RegexValidator(
            regex=r'^[a-zA-Z,.\s]+$',
            message="Invalid characters in ingredients list",
        ),
    ])
    image = models.ImageField(upload_to='images/', blank=True, null=True, validators=[validate_image_size])
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} - {self.category} - £{self.price}"
    
    def clean(self):
        """
        Ensure that the category exists and validates the image size
        """
        # Ensure that the category exists
        if not MenuCategory.objects.filter(pk=self.category.pk).exists():
            raise ValidationError("This menu item has an invalid category.")
        
        # Validate the image size
        if self.image:
            validate_image_size(self.image)
    
    class Meta:
        verbose_name_plural = "Menu Items"
        
    def get_absolute_url(self):
        return reverse('menu_item_detail', args=[str(self.id)])


class Order(models.Model):
    """
    The table holding the orders
    """
    order_id = models.AutoField(unique = True, primary_key=True)
    preparing = models.BooleanField(default=True)
    table_number = models.PositiveIntegerField(null=True)

    def __str__(self):
        return self.order_id

class Item(models.Model):
    """
    The table holding information on items
    """
    item_id = models.AutoField(unique = True, primary_key=True)
    iname = models.CharField(max_length=150)
    order = models.IntegerField(null=True)
    previous = models.OneToOneField('self', null=True, blank=True,
                                    related_name="next", on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(0.01)], default = 1.00)

class Table(models.Model):
    """
    The table holding the tables
    """
    table_number = models.PositiveIntegerField(primary_key=True, validators=[MinValueValidator(1), MaxValueValidator(10)])
    need_help = models.BooleanField(default=False)
    def __str__(self):
        return str(self.table_number)
    
class Payment(models.Model):
    cardholder_name = models.CharField(max_length=255)
    card_number = models.CharField(max_length=19)
    expiry_date = models.DateField()
    cvv = models.CharField(max_length=3)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    
    def __str__(self):
        return f"Payment {self.id}"