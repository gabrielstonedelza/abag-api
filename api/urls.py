from django.urls import path

from . import views

urlpatterns = [
    path('', views.abag_home, name='index'),
    path('mobile-money-users/', views.mobile_money_users),
    path('mobile-money-registration/<str:agent_code>/', views.mobile_money_registration),
    path('mobile-money-id-add/<str:agent_code>/', views.mobile_money_id),
    path('mobile-money-deposit/', views.mobile_money_deposit),
    path('mobile-money-withdraw/', views.mobile_money_withdrawal),
    path('mobile-money-user/<str:phone>/', views.get_mobile_user),
]
