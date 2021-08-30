from django.contrib import admin

from .models import (MobileMoneyUsersRegistration, MobileMoneyDeposit, MobileMoneyWithDraw, AgencyBankingRegistration,
                     AgencyBankingDeposit, AgencyBankingWithDraw, Fraud, MomoPay)

admin.site.register(MobileMoneyUsersRegistration)
admin.site.register(MobileMoneyDeposit)
admin.site.register(MobileMoneyWithDraw)
admin.site.register(AgencyBankingRegistration)
admin.site.register(AgencyBankingDeposit)
admin.site.register(AgencyBankingWithDraw)
admin.site.register(Fraud)
admin.site.register(MomoPay)
