from django.contrib import admin
from .models import Profile, Contact

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = [ 'date_of_birth', 'photo',
                    'country', 'city', 'gender', 'weight',
                    'height', 'profile_description']

class ContactAdmin(admin.ModelAdmin):
    list_display = ['user_from', 'user_to']

admin.site.register(Contact, ContactAdmin)