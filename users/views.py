from .serializers import ProfileSerializer, UsersSerializer
from .models import Profile, User
from rest_framework import viewsets, permissions, generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .permissions import IsOwnerOrReadOnly
from django.shortcuts import get_object_or_404


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def profile(request):
    user = Profile.objects.get(user=request.user)
    serializer = ProfileSerializer(user, many=False)
    return Response(serializer.data)


@api_view(['GET', 'PUT'])
@permission_classes([permissions.IsAuthenticated, IsOwnerOrReadOnly])
def profile_update(request):
    user_profile = get_object_or_404(Profile, user=request.user)
    serializer = ProfileSerializer(user_profile, data=request.data)
    user = request.user.id
    if user_profile.user.id != user:
        return Response({"User: you are not authorized to edit this profile"})
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
