from .serializers import UsersSerializer, AuthenticatedPhoneAddressSerializer
from .models import User, AuthenticatedPhoneAddress
from rest_framework import viewsets, permissions, generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import filters


class AllAgents(generics.ListAPIView):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UsersSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['agent_display_code']


@api_view(['GET'])
def agents(request):
    all_agents = User.objects.all().order_by('-date_joined')
    serializer = UsersSerializer(all_agents, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def profile(request, agent_code):
    agent = User.objects.get(agent_code=agent_code)
    serializer = UsersSerializer(agent, many=False)
    return Response(serializer.data)


@api_view(['GET', 'PUT'])
def profile_update(request, agent_code):
    user_profile = get_object_or_404(User, agent_code=agent_code)
    serializer = UsersSerializer(user_profile, data=request.data)
    if user_profile.agent_code != agent_code:
        return Response({"User: you are not authorized to edit this profile"})
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def check_auth_phone(request, agent_code):
    agent = get_object_or_404(User, agent_code=agent_code)
    auth_phone = AuthenticatedPhoneAddress.objects.filter(agent=agent)
    serializer = AuthenticatedPhoneAddressSerializer(auth_phone, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def add_agent_auth_phone(request, agent_code):
    agent = get_object_or_404(User, agent_code=agent_code)
    serializer = AuthenticatedPhoneAddressSerializer(data=request.data)
    if not AuthenticatedPhoneAddress.objects.filter(agent=agent).exists():
        if serializer.is_valid():
            serializer.save(agent=agent, authenticated_phone=True)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response({"Agent: Agent with this code has already been authenticated"})
