from django.shortcuts import get_object_or_404, render, redirect
from .serializers import (MobileMoneyRegistrationSerializer, MobileMoneyDepositSerializer,
                          MobileMoneyWithDrawSerializer, AgencyBankingSerializer, AgencyBankingDepositSerializer,
                          AgencyBankingWithDrawSerializer, FraudSerializer, MomoPaySerializer,
                          AgentAccountsStartedSerializer, AgentAccountsCompletedSerializer, TwilioSerializer)
from .models import (MobileMoneyUsersRegistration, MobileMoneyDeposit, MobileMoneyWithDraw, AgencyBankingRegistration,
                     AgencyBankingDeposit, AgencyBankingWithDraw, Fraud, MomoPay, AgentsAccountsStartedWith,
                     AgentsAccountsCompletedWith, TwilioApi)
from rest_framework import viewsets, permissions, generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from users.models import User
from users.serializers import UsersSerializer


@api_view(['GET'])
def get_twilio(request):
    twilio_details = TwilioApi.objects.all().order_by('-date_created')
    serializer = TwilioSerializer(twilio_details, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_deUser(request, username):
    user = get_object_or_404(User, username=username)
    serializer = UsersSerializer(user, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def agency_bank_users(request):
    ag_users = AgencyBankingRegistration.objects.all().order_by('-date_registered')
    serializer = AgencyBankingSerializer(ag_users, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_agency_account(request, account_number):
    ag_account = AgencyBankingRegistration.objects.get(account_number=account_number)
    serializer = AgencyBankingSerializer(ag_account, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def agency_banking_registration(request, username):
    agent = User.objects.get(username=username)
    serializer = AgencyBankingSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(agent=agent)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def momo_registration(request, username):
    agent = User.objects.get(username=username)
    serializer = MobileMoneyRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(agent=agent)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def agency_banking_deposit(request, username):
    agent = User.objects.get(username=username)
    serializer = AgencyBankingDepositSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(agent=agent)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def agency_banking_withdrawal(request, username):
    agent = User.objects.get(username=username)
    serializer = AgencyBankingWithDrawSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(agent=agent)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def add_fraud(request, username):
    agent = User.objects.get(username=username)
    serializer = FraudSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(agent=agent)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def frauds(request):
    all_fraudsters = Fraud.objects.all().order_by('-date_added')
    serializer = FraudSerializer(all_fraudsters, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def add_momo_pay(request, username):
    agent = User.objects.get(username=username)
    serializer = MomoPaySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(agent=agent)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def momo_pay_users(request):
    momo_users = MomoPay.objects.all().order_by('-date_added')
    serializer = MomoPaySerializer(momo_users, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def mobile_money_users(request):
    mm_users = MobileMoneyUsersRegistration.objects.all().order_by('-date_registered')
    serializer = MobileMoneyRegistrationSerializer(mm_users, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_mobile_user(request, phone):
    mm_user = MobileMoneyUsersRegistration.objects.get(phone=phone)
    serializer = MobileMoneyRegistrationSerializer(mm_user, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def mobile_money_deposit(request, username):
    agent = User.objects.get(username=username)
    serializer = MobileMoneyDepositSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(agent=agent)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def mobile_money_withdrawal(request, username):
    agent = User.objects.get(username=username)
    serializer = MobileMoneyWithDrawSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(agent=agent)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def abag_home(request):
    return render(request, "users/abag_home.html")


def register_success(request):
    return render(request, "users/register_success.html")


# agent mobile money transaction

@api_view(['GET'])
def agent_momo_registrations(request, username):
    user = get_object_or_404(User, username=username)
    agent = MobileMoneyUsersRegistration.objects.filter(agent=user).order_by('-date_registered')
    serializer = MobileMoneyRegistrationSerializer(agent, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def agent_momo_deposits(request, username):
    user = get_object_or_404(User, username=username)
    agent = MobileMoneyDeposit.objects.filter(agent=user).order_by('-date_deposited')
    serializer = MobileMoneyDepositSerializer(agent, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def agent_momo_withdraws(request, username):
    user = get_object_or_404(User, username=username)
    agent = MobileMoneyWithDraw.objects.filter(agent=user).order_by('-date_withdrew')
    serializer = MobileMoneyWithDrawSerializer(agent, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def agent_momo(request, username):
    user = get_object_or_404(User, username=username)
    agent = MomoPay.objects.filter(agent=user).order_by('-date_added')
    serializer = MomoPaySerializer(agent, many=True)
    return Response(serializer.data)


# agent agency banking transaction

@api_view(['GET'])
def agent_agency_banking_registrations(request, username):
    user = get_object_or_404(User, username=username)
    agent = AgencyBankingRegistration.objects.filter(agent=user).order_by('-date_registered')
    serializer = AgencyBankingSerializer(agent, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def agent_agency_banking_deposits(request, username):
    user = get_object_or_404(User, username=username)
    agent = AgencyBankingDeposit.objects.filter(agent=user).order_by('-date_deposited')
    serializer = AgencyBankingDepositSerializer(agent, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def agent_agency_banking_withdraws(request, username):
    user = get_object_or_404(User, username=username)
    agent = AgencyBankingWithDraw.objects.filter(agent=user).order_by('-date_withdrew')
    serializer = AgencyBankingWithDrawSerializer(agent, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def agent_accounts_started(request, username):
    agent = User.objects.get(username=username)
    serializer = AgentAccountsStartedSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(agent=agent)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def agent_accounts_completed(request, username):
    agent = User.objects.get(username=username)
    serializer = AgentAccountsCompletedSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(agent=agent)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def agent_accounts_started_lists(request, username):
    user = get_object_or_404(User, username=username)
    agent_accounts = AgentsAccountsStartedWith.objects.filter(agent=user).order_by('-date_started')
    serializer = AgentAccountsStartedSerializer(agent_accounts, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def agent_accounts_completed_lists(request, username):
    user = get_object_or_404(User, username=username)
    agent_accounts = AgentsAccountsCompletedWith.objects.filter(agent=user).order_by('-date_closed')
    serializer = AgentAccountsCompletedSerializer(agent_accounts, many=True)
    return Response(serializer.data)
