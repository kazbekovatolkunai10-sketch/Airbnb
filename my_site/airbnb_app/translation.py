from .models import User, City, Property, Review, Amenity
from modeltranslation.translator import TranslationOptions,register

@register(User)
class UserTranslationOptions(TranslationOptions):
    fields = ('first_name', 'last_name')

@register(City)
class CityTranslationOptions(TranslationOptions):
    fields = ('city_name',)

@register(Property)
class UserTranslationOptions(TranslationOptions):
    fields = ('title', 'descriptions')

@register(Review)
class ReviewTranslationOptions(TranslationOptions):
    fields = ('comment',)

@register(Amenity)
class AmenityTranslationOptions(TranslationOptions):
    fields = ('amenity_name',)


