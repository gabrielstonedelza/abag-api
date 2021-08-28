from django.contrib import admin

from .models import MobileMoneyUsersRegistration, MobileMoneyDeposit, MobileMoneyWithDraw,MobileMoneyUserId

admin.site.register(MobileMoneyUsersRegistration)
admin.site.register(MobileMoneyDeposit)
admin.site.register(MobileMoneyWithDraw)
admin.site.register(MobileMoneyUserId)
