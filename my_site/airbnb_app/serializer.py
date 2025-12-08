from rest_framework import serializers
from .models import (User, City, Property, PropertyImage, Booking, Review, Amenity)
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name',
                  'phone_number', 'role')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Неверные учетные данные")

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class UserSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']

class CityListSerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['city_name']

class CityDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['city_name', 'city_image']

class PropertyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ['property_city', 'title', 'price_per_night',
                  'property_type', 'max_guest']

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = '__all__'

class PropertyImageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyImage
        fields = ['property_image']

class PropertyImageDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyImage
        fields = ['property', 'property_image']

class BookingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['property', 'guest', 'created_at']

class BookingDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['property', 'guest', 'check_in', 'check_out', 'status', 'created_at']

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['property', 'guest', 'comment']

class ReviewDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['property', 'guest', 'rating', 'comment', 'created_at']

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class AmenitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Amenity
        fields = '__all__'

class PropertyDetailSerializer(serializers.ModelSerializer):
    property_image = PropertyImageListSerializer(many=True, read_only=True)
    property_review = ReviewListSerializer(many=True, read_only=True)
    property_city = CityListSerializer()
    owner = UserSimpleSerializer()
    get_avg_rating = serializers.SerializerMethodField
    get_count_people = serializers.SerializerMethodField
    class Meta:
        model = Property
        fields = ['property_city', 'property_image', 'title','property_type', 'owner', 'max_guest', 'descriptions',
                  'price_per_night', 'is_active', 'bedrooms', 'bathrooms', 'rules', 'property_review',
                  'get_avg_rating', 'get_count_people']

    def get_avg_rating(self, obj):
        return obj.get_avg_rating()

    def get_count_people(self, obj):
        return obj.get_count_people()
