from django.urls import path

from . import views

urlpatterns = [
    # normal request links
    path('', views.abag_home, name='index'),
    path('register_success/', views.register_success, name="register_success"),
    # api links
    path('mobile-money-users/', views.mobile_money_users),
    path('mobile-money-registration/<str:agent_code>/', views.mobile_money_registration),
    path('mobile-money-deposit/<str:agent_code>/', views.mobile_money_deposit),
    path('mobile-money-withdraw/<str:agent_code>/', views.mobile_money_withdrawal),
    path('mobile-money-user/<str:phone>/', views.get_mobile_user),

    #     agency banking
    path('agency-banking-users/', views.agency_bank_users),
    path('agency-banking-registration/<str:agent_code>/', views.agency_banking_registration),
    path('agency-banking-deposit/<str:agent_code>/', views.agency_banking_deposit),
    path('agency-banking-withdraw/<str:agent_code>/', views.agency_banking_withdrawal),
    path('agency-banking-account/<str:account_number>/', views.get_agency_account),

    #  others
    path('frauds/', views.frauds),
    path('add-fraud/<str:agent_code>/', views.add_fraud),
    path('momo-pay-users/', views.momo_pay_users),
    path('add-momo-pay/<str:agent_code>/', views.add_momo_pay)
]
