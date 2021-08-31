from django.shortcuts import get_object_or_404, render
from .serializers import (MobileMoneyRegistrationSerializer, MobileMoneyDepositSerializer,
                          MobileMoneyWithDrawSerializer, AgencyBankingSerializer, AgencyBankingDepositSerializer,
                          AgencyBankingWithDrawSerializer, FraudSerializer, MomoPaySerializer)
from .models import (MobileMoneyUsersRegistration, MobileMoneyDeposit, MobileMoneyWithDraw, AgencyBankingRegistration,
                     AgencyBankingDeposit, AgencyBankingWithDraw, Fraud, MomoPay)
from rest_framework import viewsets, permissions, generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from users.models import User


@api_view(['GET'])
def agency_bank_users(request):
    ag_users = AgencyBankingRegistration.objects.all().order_by('-date_registered')
    serializer = AgencyBankingSerializer(ag_users, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_agency_user(request, phone):
    ag_users = AgencyBankingRegistration.objects.get(phone=phone)
    serializer = AgencyBankingSerializer(ag_users, many=False)
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
def mobile_money_registration(request, agent_code):
    agent = User.objects.get(agent_code=agent_code)
    serializer = MobileMoneyRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(agent=agent)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
