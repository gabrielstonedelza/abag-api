from django.contrib import admin

from .models import User, AuthenticatedPhoneAddress
admin.site.register(User)
admin.site.register(AuthenticatedPhoneAddress)
