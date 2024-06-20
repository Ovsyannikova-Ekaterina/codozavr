import json

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets

from .models import CustomUser, Parent, Student, Teacher
from .serializers import CustomUserSerializer, ParentSerializer, StudentSerializer, TeacherSerializer


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class ParentViewSet(viewsets.ModelViewSet):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


@login_required
def profile_view(request):
    return render(request, 'profile.html')


@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            print("Received login data:", data)  # Debug line
            username = data.get('username')
            password = data.get('password')
            if not username or not password:
                print("Missing username or password")  # Debug line
                return JsonResponse({'status': 'error', 'message': 'Username and password are required'}, status=400)
            print(f"Authenticating user: {username}")  # Debug line
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                print("Login successful")  # Debug line
                return JsonResponse({'status': 'ok', 'message': 'Login successful'})
            else:
                print(f"Invalid credentials for user: {username}")  # Debug line
                return JsonResponse({'status': 'error', 'message': 'Invalid credentials'}, status=400)
        except json.JSONDecodeError as e:
            print("Invalid JSON:", str(e))  # Debug line
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON'}, status=400)
        except Exception as e:
            print("Exception:", str(e))  # Debug line
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)


@csrf_exempt
def register_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            print("Received registration data:", data)  # Debug line
            username = data.get('username')
            email = data.get('email')
            password = data.get('password')
            if not username or not email or not password:
                print("Missing username, email, or password")  # Debug line
                return JsonResponse({'status': 'error', 'message': 'Username, email, and password are required'},
                                    status=400)
            if CustomUser.objects.filter(username=username).exists():
                print("Username already exists")  # Debug line
                return JsonResponse({'status': 'error', 'message': 'Username already exists'}, status=400)
            if CustomUser.objects.filter(email=email).exists():
                print("Email already exists")  # Debug line
                return JsonResponse({'status': 'error', 'message': 'Email already exists'}, status=400)
            user = CustomUser.objects.create_user(username=username, email=email, password=password, user_type=1)
            Parent.objects.create(user=user)
            print("User and Parent created successfully")  # Debug line
            return JsonResponse({'status': 'ok', 'message': 'User created successfully'})
        except json.JSONDecodeError as e:
            print("Invalid JSON:", str(e))  # Debug line
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON'}, status=400)
        except Exception as e:
            print("Exception:", str(e))  # Debug line
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)


@csrf_exempt
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return JsonResponse({'status': 'ok'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)
