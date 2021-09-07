from django.shortcuts import get_object_or_404, render, redirect
from .serializers import (MobileMoneyRegistrationSerializer, MobileMoneyDepositSerializer,
                          MobileMoneyWithDrawSerializer, AgencyBankingSerializer, AgencyBankingDepositSerializer,
                          AgencyBankingWithDrawSerializer, FraudSerializer, MomoPaySerializer, ChatMessageSerializer)
from .models import (MobileMoneyUsersRegistration, MobileMoneyDeposit, MobileMoneyWithDraw, AgencyBankingRegistration,
                     AgencyBankingDeposit, AgencyBankingWithDraw, Fraud, MomoPay, ChatMessage)
from rest_framework import viewsets, permissions, generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from users.models import User
from users.forms import MobileMoneyForm, AgencyBankingForm
from users.serializers import UsersSerializer
import random


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


# @api_view(['POST'])
# def agency_banking_registration(request, agent_code):
#     agent = User.objects.get(agent_code=agent_code)
#     serializer = AgencyBankingSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save(agent=agent)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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


def mobile_money_registration(request, agent_code):
    agent = User.objects.get(agent_code=agent_code)
    if request.method == "POST":
        form = MobileMoneyForm(request.POST, request.FILES)
        if form.is_valid():
            network = form.cleaned_data.get('network')
            phone = form.cleaned_data.get('phone')
            name = form.cleaned_data.get('name')
            id_type = form.cleaned_data.get('id_type')
            id_number = form.cleaned_data.get('id_number')
            photo = form.cleaned_data.get('photo')
            MobileMoneyUsersRegistration.objects.create(agent=agent, network=network, phone=phone, name=name,
                                                        id_type=id_type, id_number=id_number, photo=photo)
            return redirect('register_success')
    else:
        form = MobileMoneyForm()

    context = {
        "form": form
    }

    return render(request, "users/mm_registration.html", context)


def agency_banking_registration(request, agent_code):
    agent = User.objects.get(agent_code=agent_code)
    if request.method == "POST":
        form = AgencyBankingForm(request.POST, request.FILES)
        if form.is_valid():
            bank = form.cleaned_data.get('bank')
            account_number = form.cleaned_data.get('account_number')
            phone = form.cleaned_data.get('phone')
            name = form.cleaned_data.get('name')
            id_type = form.cleaned_data.get('id_type')
            id_number = form.cleaned_data.get('id_number')
            photo = form.cleaned_data.get('photo')
            AgencyBankingRegistration.objects.create(agent=agent, bank=bank, account_number=account_number, phone=phone, name=name,
                                                     id_type=id_type, id_number=id_number, photo=photo)
            return redirect('register_success')
    else:
        form = AgencyBankingForm()

    context = {
        "form": form
    }

    return render(request, "users/agency_registration.html", context)


def register_success(request):
    return render(request, "users/register_success.html")


# agent mobile money transactions


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


# chat message
@api_view(['GET'])
def get_chat_messages(request, message_id):
    msg_id = ChatMessage.objects.filter(message_id=message_id).order_by('-date_messaged')
    serializer = ChatMessageSerializer(msg_id, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_chat(request):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i''j', 'k', 'l']
    serializer = ChatMessageSerializer(data=request.data)
    gen_code = random.randint(1, 1001)
    msgi_code = random.choice(letters) + str(gen_code)
    if serializer.is_valid():
        serializer.save(agent=request.user, message_id=msgi_code)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
