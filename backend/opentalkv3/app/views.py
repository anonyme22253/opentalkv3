from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
from django.middleware.csrf import get_token
from django.contrib.auth.models import User
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.permissions import (AllowAny,IsAuthenticated)
from django.contrib.auth import authenticate, login
# Create your views here.
@ensure_csrf_cookie
@api_view(['GET'])
@permission_classes([AllowAny])
def get_csrf_token(request):
    token =get_token(request)
    return JsonResponse({"csrfToken": token})

@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    first_name=request.data.get('firstname')
    lastname = request.data.get('lastname')
    email = request.data.get('email')
    password = request.data.get('password')
    if User.objects.filter(email=email).exists():
        return Response({"message":"user already exists"},status=400)
    else:
        User.objects.create_user(username=lastname,email=email,password=password)
    return Response({"message":' User Created Succesfully'})
@api_view(['POST'])
@permission_classes([AllowAny])
def user_login(request):

    email= request.data.get('email')
    password = request.data.get('password')
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        return Response({"message": "Invalid email or password"}, status=400)

    user = authenticate(
        request,
        username=user.username,
        password=password
    )

    if user is not None:
        login(request, user)
        return Response({"message": "You logged in successfully"})

    return Response({"message": "Invalid email or password"}, status=400)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def add_user_to_sidebar(request):
    users = User.objects.exclude(id=request.user.id)
    users_list = []
    for user in users:
        users_list.append({
            "username": user.username,
            "email": user.email
        })

    return Response(users_list)