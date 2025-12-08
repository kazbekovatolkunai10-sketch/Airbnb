from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from multiselectfield.db.fields import MultiSelectField


class User(AbstractUser):
    ROLE_CHOICES = (
        ('guest', 'guest'),
        ('host', 'host'),
    )
    role = models.CharField(max_length=24, choices=ROLE_CHOICES, default='guest')
    phone_number = PhoneNumberField(null=True, blank=True)
    avatar = models.ImageField(upload_to='avatar/', null=True, blank=True)

    def __str__(self):
        return f'{self.first_name}, {self.last_name}'

class City(models.Model):
    city_name = models.CharField(max_length=64)
    city_image = models.ImageField(upload_to='city_image/')

    def __str__(self):
        return f'{self.city_name}, {self.city_image}'

class Property(models.Model):
    title = models.CharField(max_length=78)
    descriptions = models.TextField()
    price_per_night = models.PositiveIntegerField()
    PROPERTY_TYPE = (
        ('apartment', 'apartment'),
        ('house', 'house'),
        ('studio', 'studio'),
    )
    property_type = models.CharField(max_length=26, choices=PROPERTY_TYPE)
    RULES = (
        ('no_smoking', 'no_smoking'),
        ('pets_allowed', 'pets_allowed'),
    )
    rules = MultiSelectField(max_length=34, choices=RULES)
    max_guest = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(2)])
    bedrooms = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(2)])
    bathrooms = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(2)])
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    property_city = models.ForeignKey(City, on_delete=models.CASCADE)
    is_active = models.BooleanField()

    def __str__(self):
        return f'{self.title}, {self.property_city}'

    def get_avg_rating(self):
        ratings = self.property_review.all()
        if ratings.exists():
            return round(sum(i.rating for i in ratings) / ratings.count(), 2)
        return 0

    def ё(self):
        ratings = self.property_review.all()
        if ratings.exists():
            return ratings.count()
        return 0

class PropertyImage(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='property_image')
    property_image = models.ImageField(upload_to='property_image/')

    def __str__(self):
        return f'{self.property}, {self.property_image}'

class Booking(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    guest = models.ForeignKey(User, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    STATUS_CHOICES = (
        ('pending', 'pending'),
        ('approved', 'approved'),
        ('rejected', 'rejected'),
        ('cancelled', 'cancelled'),
    )
    status = models.CharField(max_length=34, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.property}, {self.created_at}'

class Review(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='property_review')
    guest = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(choices = [(i, str (i)) for i in range(1, 6)])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.property}, {self.guest}'

class Amenity(models.Model):
    amenity_name = models.CharField(max_length=64)
    icon = models.ImageField(upload_to='icon/')
    property = models.ManyToManyField(Property)

    def __str__(self):
        return f'{self.amenity_name}'





