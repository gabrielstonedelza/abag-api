from django.shortcuts import get_object_or_404, render, redirect
from .serializers import (MobileMoneyRegistrationSerializer, MobileMoneyDepositSerializer,
                          MobileMoneyWithDrawSerializer, AgencyBankingSerializer, AgencyBankingDepositSerializer,
                          AgencyBankingWithDrawSerializer, FraudSerializer, MomoPaySerializer,
                          AgentAccountsStartedSerializer, AgentAccountsCompletedSerializer)
from .models import (MobileMoneyUsersRegistration, MobileMoneyDeposit, MobileMoneyWithDraw, AgencyBankingRegistration,
                     AgencyBankingDeposit, AgencyBankingWithDraw, Fraud, MomoPay, AgentsAccountsStartedWith,
                     AgentsAccountsCompletedWith)
from rest_framework import viewsets, permissions, generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from users.models import User
from users.serializers import UsersSerializer


@api_view(['GET'])
def get_deUser(request, agent_code):
    user = get_object_or_404(User, agent_code=agent_code)
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
def agency_banking_registration(request, agent_code):
    agent = User.objects.get(agent_code=agent_code)
    serializer = AgencyBankingSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(agent=agent)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def momo_registration(request, agent_code):
    agent = User.objects.get(agent_code=agent_code)
    serializer = MobileMoneyRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(agent=agent)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def agency_banking_deposit(request, agent_code):
    agent = User.objects.get(agent_code=agent_code)
    serializer = AgencyBankingDepositSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(agent=agent)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def agency_banking_withdrawal(request, agent_code):
    agent = User.objects.get(agent_code=agent_code)
    serializer = AgencyBankingWithDrawSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(agent=agent)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def add_fraud(request, agent_code):
    agent = User.objects.get(agent_code=agent_code)
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
def add_momo_pay(request, agent_code):
    agent = User.objects.get(agent_code=agent_code)
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
def mobile_money_deposit(request, agent_code):
    agent = User.objects.get(agent_code=agent_code)
    serializer = MobileMoneyDepositSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(agent=agent)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def mobile_money_withdrawal(request, agent_code):
    agent = User.objects.get(agent_code=agent_code)
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
def agent_momo_registrations(request, agent_code):
    user = get_object_or_404(User, agent_code=agent_code)
    agent = MobileMoneyUsersRegistration.objects.filter(agent=user)
    serializer = MobileMoneyRegistrationSerializer(agent, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def agent_momo_deposits(request, agent_code):
    user = get_object_or_404(User, agent_code=agent_code)
    agent = MobileMoneyDeposit.objects.filter(agent=user)
    serializer = MobileMoneyDepositSerializer(agent, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def agent_momo_withdraws(request, agent_code):
    user = get_object_or_404(User, agent_code=agent_code)
    agent = MobileMoneyWithDraw.objects.filter(agent=user)
    serializer = MobileMoneyWithDrawSerializer(agent, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def agent_momo(request, agent_code):
    user = get_object_or_404(User, agent_code=agent_code)
    agent = MomoPay.objects.filter(agent=user)
    serializer = MomoPaySerializer(agent, many=True)
    return Response(serializer.data)


# agent agency banking transaction

@api_view(['GET'])
def agent_agency_banking_registrations(request, agent_code):
    user = get_object_or_404(User, agent_code=agent_code)
    agent = AgencyBankingRegistration.objects.filter(agent=user)
    serializer = AgencyBankingSerializer(agent, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def agent_agency_banking_deposits(request, agent_code):
    user = get_object_or_404(User, agent_code=agent_code)
    agent = AgencyBankingDeposit.objects.filter(agent=user)
    serializer = AgencyBankingDepositSerializer(agent, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def agent_agency_banking_withdraws(request, agent_code):
    user = get_object_or_404(User, agent_code=agent_code)
    agent = AgencyBankingWithDraw.objects.filter(agent=user)
    serializer = AgencyBankingWithDrawSerializer(agent, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def agent_accounts_started(request, agent_code):
    agent = User.objects.get(agent_code=agent_code)
    serializer = AgentAccountsStartedSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(agent=agent)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def agent_accounts_completed(request, agent_code):
    agent = User.objects.get(agent_code=agent_code)
    serializer = AgentAccountsCompletedSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(agent=agent)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def agent_accounts_started_lists(request, agent_code):
    user = get_object_or_404(User, agent_code=agent_code)
    agent_accounts = AgentsAccountsStartedWith.objects.filter(agent=user).order_by('-date_started')
    serializer = AgentAccountsStartedSerializer(agent_accounts, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def agent_accounts_completed_lists(request, agent_code):
    user = get_object_or_404(User, agent_code=agent_code)
    agent_accounts = AgentsAccountsCompletedWith.objects.filter(agent=user).order_by('-date_closed')
    serializer = AgentAccountsCompletedSerializer(agent_accounts, many=True)
    return Response(serializer.data)


@api_view(['GET', 'PUT'])
def account_update(request,agent_code,id):
    user = get_object_or_404(User, agent_code=agent_code)
    account_started = get_object_or_404(AgentsAccountsStartedWith, id=id)
    serializer = AgentAccountsStartedSerializer(account_started,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
