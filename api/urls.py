from django.urls import path

from . import views

urlpatterns = [
    # normal request links
    path('', views.abag_home, name='index'),
    path('register_success/', views.register_success, name="register_success"),
    # api links
    path('deuser/<str:agent_code>/', views.get_deUser),
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
    path('agency-banking-account/<str:phone>/', views.get_agency_account),

    #  others
    path('frauds/', views.frauds),
    path('add-fraud/<str:agent_code>/', views.add_fraud),
    path('momo-pay-users/', views.momo_pay_users),
    path('add-momo-pay/<str:agent_code>/', views.add_momo_pay),

    # agent transactions summary mobile money
    path('momo-registration-summary/<str:agent_code>/', views.agent_momo_registrations),
    path('momo-deposit-summary/<str:agent>/', views.agent_momo_deposits),
    path('momo-withdraws-summary/<str:agent>/', views.agent_momo_withdraws),
    path('momo-pay-summary/<str:agent>/', views.agent_momo),

    # agent agency banking summary
    path('agency-banking-registration-summary/<str:agent>/', views.agent_agency_banking_registrations),
    path('agency-banking-deposit-summary/<str:agent>/', views.agent_agency_banking_deposits),
    path('agency-banking-withdraws-summary/<str:agent>/', views.agent_agency_banking_withdraws),
]
