from .serializers import UsersSerializer
from .models import User
from rest_framework import viewsets, permissions, generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .permissions import IsOwnerOrReadOnly
from django.shortcuts import get_object_or_404


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
